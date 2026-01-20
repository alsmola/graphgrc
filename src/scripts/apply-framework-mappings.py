#!/usr/bin/env python3
"""Apply framework mappings to control files."""

import json
import re
from pathlib import Path

def apply_mappings_to_control(control_path, mappings):
    """Add framework mappings to a control file."""
    with open(control_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Framework Mapping section
    framework_mapping_pattern = r'(## Framework Mapping\n\n)(.*?)(---)'
    match = re.search(framework_mapping_pattern, content, re.DOTALL)

    if not match:
        print(f"Warning: No Framework Mapping section found in {control_path}")
        return False

    # Build the new framework mapping section
    new_mapping_lines = []

    # Keep existing Standards/Processes/Policies/Charter subsections, but NOT SOC 2 or GDPR
    existing_content = match.group(2)

    # Extract only non-framework subsections
    lines_to_keep = []
    in_framework_section = False
    for line in existing_content.split('\n'):
        if line.startswith('### SOC 2') or line.startswith('### GDPR') or line.startswith('### ISO'):
            in_framework_section = True
            continue
        elif line.startswith('###'):
            in_framework_section = False
            lines_to_keep.append(line)
        elif not in_framework_section and line.strip():
            lines_to_keep.append(line)

    if lines_to_keep:
        new_mapping_lines.extend(lines_to_keep)
        new_mapping_lines.append('')

    # Add SOC 2 mappings
    if 'soc2' in mappings and mappings['soc2']:
        new_mapping_lines.append('### SOC 2')
        for mapping in mappings['soc2']:
            control_id = mapping['id'].upper()
            # Format: cc61 -> CC6.1, cc123 -> CC1.23
            if control_id.startswith('CC'):
                if len(control_id) == 4:  # cc61 -> CC6.1
                    formatted_id = f"{control_id[:3]}.{control_id[3]}"
                else:  # cc123 -> CC1.23
                    formatted_id = f"{control_id[:3]}.{control_id[3:]}"
            else:
                formatted_id = control_id.upper()

            annotation = mapping['annotation']
            new_mapping_lines.append(f'- [{formatted_id}](../../frameworks/soc2/{mapping["id"]}.md) ^[{annotation}]')
        new_mapping_lines.append('')

    # Add GDPR mappings
    if 'gdpr' in mappings and mappings['gdpr']:
        new_mapping_lines.append('### GDPR')
        for mapping in mappings['gdpr']:
            # Format: art32 -> Article 32
            article_num = mapping['id'].replace('art', '')
            formatted_id = f"Article {article_num}"
            annotation = mapping['annotation']
            new_mapping_lines.append(f'- [{formatted_id}](../../frameworks/gdpr/{mapping["id"]}.md) ^[{annotation}]')
        new_mapping_lines.append('')

    # Construct the new Framework Mapping section
    new_section = match.group(1) + '\n'.join(new_mapping_lines) + '\n' + match.group(3)

    # Replace the section in content
    new_content = content[:match.start()] + new_section + content[match.end():]

    # Write back
    with open(control_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    repo_root = Path(__file__).parent.parent.parent
    mappings_file = repo_root / 'control-framework-mappings.json'

    if not mappings_file.exists():
        print(f"Error: {mappings_file} does not exist")
        return

    # Load mappings
    with open(mappings_file, 'r', encoding='utf-8') as f:
        all_mappings = json.load(f)

    modified_count = 0
    total_count = len(all_mappings)

    for control_rel_path, mappings in all_mappings.items():
        control_path = repo_root / 'docs' / control_rel_path

        if not control_path.exists():
            print(f"Warning: {control_path} does not exist")
            continue

        if apply_mappings_to_control(control_path, mappings):
            modified_count += 1
            print(f"Updated: {control_rel_path}")

    print(f"\nProcessed {total_count} controls, modified {modified_count} files")

if __name__ == '__main__':
    main()
