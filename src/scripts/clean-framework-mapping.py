#!/usr/bin/env python3
"""Remove Standards/Processes/Policies from Framework Mapping sections in controls."""

import re
from pathlib import Path

def clean_framework_mapping(file_path):
    """Remove non-framework subsections from Framework Mapping."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Framework Mapping section
    pattern = r'(## Framework Mapping\n\n)(.*?)(---)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return False

    existing_content = match.group(2)

    # Extract ONLY framework subsections (SOC 2, GDPR, ISO, NIST)
    new_lines = []
    in_framework_section = False

    for line in existing_content.split('\n'):
        if line.startswith('### SOC 2') or line.startswith('### GDPR') or line.startswith('### ISO') or line.startswith('### NIST'):
            in_framework_section = True
            new_lines.append(line)
        elif line.startswith('###'):
            # Non-framework subsection, skip it
            in_framework_section = False
        elif in_framework_section:
            new_lines.append(line)

    # Rebuild the section
    new_section = match.group(1) + '\n'.join(new_lines).strip() + '\n\n' + match.group(3)
    new_content = content[:match.start()] + new_section + content[match.end():]

    # Only write if changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    repo_root = Path(__file__).parent.parent.parent
    controls_dir = repo_root / 'docs' / 'controls'

    modified_count = 0
    total_count = 0

    for control_file in controls_dir.rglob('*.md'):
        total_count += 1
        if clean_framework_mapping(control_file):
            modified_count += 1
            print(f"Cleaned: {control_file.relative_to(repo_root)}")

    print(f"\nProcessed {total_count} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
