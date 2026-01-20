#!/usr/bin/env python3
"""Generate Referenced By sections in framework files, per heading."""

import json
import re
from pathlib import Path
from collections import defaultdict

def parse_markdown_structure(content):
    """Parse markdown to find all headings and their positions."""
    headings = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        if line.startswith('# ') or line.startswith('## '):
            level = line.count('#', 0, 2)
            title = line.lstrip('#').strip()
            headings.append({
                'line': i,
                'level': level,
                'title': title,
                'content_start': i + 1
            })

    # Calculate content_end for each heading (start of next heading at same or higher level)
    for i, heading in enumerate(headings):
        # Find next heading at same or higher level
        for j in range(i + 1, len(headings)):
            if headings[j]['level'] <= heading['level']:
                heading['content_end'] = headings[j]['line']
                break
        else:
            heading['content_end'] = len(lines)

    return headings, lines

def remove_existing_referenced_by(lines, start, end):
    """Remove any existing 'Referenced By' sections in the range."""
    new_lines = []
    skip_until = None

    for i in range(start, end):
        if skip_until is not None:
            if i < skip_until:
                continue
            else:
                skip_until = None

        if i < len(lines) and ('**Referenced By:**' in lines[i] or lines[i].strip() == '## Referenced By'):
            # Skip this line and subsequent lines until we hit another heading or end
            skip_until = end
            for j in range(i + 1, end):
                if j < len(lines) and (lines[j].startswith('#') or lines[j].strip() == '---'):
                    skip_until = j
                    break
            continue

        if i < len(lines):
            new_lines.append(lines[i])

    return new_lines

def insert_referenced_by(lines, heading_end, backlinks):
    """Insert Referenced By section before heading_end position."""
    if not backlinks:
        return lines

    # Build the Referenced By section
    ref_lines = [
        '',
        '## Referenced By',
        ''
    ]

    for backlink in sorted(backlinks, key=lambda x: x['source_path']):
        ref_lines.append(f"- [{backlink['title']}]({backlink['relative_link']}) ^[{backlink['annotation']}]")

    ref_lines.append('')

    # Insert before the heading_end position
    return lines[:heading_end] + ref_lines + lines[heading_end:]

def process_framework_file(file_path, backlinks_for_file):
    """Process a single framework file and add Referenced By sections."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    headings, lines = parse_markdown_structure(content)

    if not headings:
        return False

    # Group backlinks by heading (if they reference a specific section, otherwise goes at end)
    backlinks_by_section = defaultdict(list)

    for backlink in backlinks_for_file:
        # For now, put all backlinks at the end of the file
        # TODO: Parse anchors from links to determine specific sections
        backlinks_by_section['__end__'].append(backlink)

    # Process from end to start to maintain line numbers
    modified = False

    if backlinks_by_section['__end__']:
        # Add at the very end of the file
        # First, remove any existing Referenced By sections in the main content
        cleaned_lines = []
        skip = False
        for i, line in enumerate(lines):
            if '**Referenced By:**' in line or line.strip() == '## Referenced By':
                skip = True
                modified = True
            elif skip and (line.startswith('#') or (i == len(lines) - 1)):
                skip = False
                if not line.startswith('#'):
                    continue

            if not skip:
                cleaned_lines.append(line)

        # Now add the new Referenced By section at the end
        while cleaned_lines and not cleaned_lines[-1].strip():
            cleaned_lines.pop()

        cleaned_lines.append('')
        cleaned_lines.append('---')
        cleaned_lines.append('')
        cleaned_lines.append('## Referenced By')
        cleaned_lines.append('')

        for backlink in sorted(backlinks_by_section['__end__'], key=lambda x: x['source_path']):
            cleaned_lines.append(f"- [{backlink['title']}]({backlink['relative_link']}) ^[{backlink['annotation']}]")

        cleaned_lines.append('')

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned_lines))

        return True

    return modified

def extract_backlinks_from_controls():
    """Extract all backlinks from control files to framework files."""
    repo_root = Path(__file__).parent.parent.parent
    controls_dir = repo_root / 'docs' / 'controls'

    backlinks = defaultdict(list)

    # Pattern to match framework links with annotations
    # Example: - [CC6.1](../../frameworks/soc2/cc61.md) ^[annotation text]
    link_pattern = re.compile(r'-\s+\[([^\]]+)\]\(\.\.\/\.\.\/frameworks\/([^)]+)\)\s+\^\[([^\]]+)\]')

    for control_file in controls_dir.rglob('*.md'):
        with open(control_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title from control
        title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        control_title = title_match.group(1) if title_match else control_file.stem

        # Find all framework links
        for match in link_pattern.finditer(content):
            display_text = match.group(1)
            framework_path = match.group(2)  # e.g., "soc2/cc61.md"
            annotation = match.group(3)

            # Calculate relative path from framework file back to control
            # Framework file is at: docs/frameworks/soc2/cc61.md
            # Control file is at: docs/controls/iam/multi-factor-authentication.md
            # Relative path: ../../controls/iam/multi-factor-authentication.md

            control_rel_path = control_file.relative_to(repo_root / 'docs')
            relative_link = f"../../{control_rel_path}"

            backlinks[framework_path].append({
                'source_path': str(control_rel_path),
                'title': control_title,
                'relative_link': relative_link,
                'annotation': annotation
            })

    return backlinks

def main():
    repo_root = Path(__file__).parent.parent.parent
    frameworks_dir = repo_root / 'docs' / 'frameworks'

    print("Extracting backlinks from controls...")
    backlinks = extract_backlinks_from_controls()

    print(f"Found {sum(len(v) for v in backlinks.values())} backlinks to {len(backlinks)} framework files")

    modified_count = 0

    for framework_rel_path, backlinks_list in backlinks.items():
        framework_file = frameworks_dir / framework_rel_path

        if not framework_file.exists():
            print(f"Warning: {framework_file} does not exist")
            continue

        if process_framework_file(framework_file, backlinks_list):
            modified_count += 1
            print(f"Updated: {framework_rel_path}")

    print(f"\nProcessed {len(backlinks)} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
