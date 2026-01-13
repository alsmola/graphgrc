#!/usr/bin/env python3
"""Move Framework Mapping section to right before Referenced By in custom controls."""

import os
import re
import glob

def fix_control_file(filepath):
    """Move Framework Mapping section to be right before Referenced By."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the Framework Mapping section
    fm_pattern = r'(---\n\n## Framework Mapping\n\n.*?)(?=\n---\n\n<!-- Backlinks auto-generated below -->)'
    fm_match = re.search(fm_pattern, content, re.DOTALL)

    if not fm_match:
        print(f"Warning: Could not find Framework Mapping in {filepath}")
        return False

    framework_mapping = fm_match.group(1)

    # Remove the Framework Mapping section from its current location
    content = re.sub(fm_pattern, '', content, flags=re.DOTALL)

    # Find where to insert it (right before the "---\n\n<!-- Backlinks auto-generated below -->" marker)
    insertion_marker = '---\n\n<!-- Backlinks auto-generated below -->'

    if insertion_marker not in content:
        print(f"Warning: Could not find backlinks marker in {filepath}")
        return False

    # Insert Framework Mapping right before the marker
    content = content.replace(insertion_marker, framework_mapping + '\n' + insertion_marker)

    # Write back
    with open(filepath, 'w') as f:
        f.write(content)

    return True

def main():
    count = 0
    for filepath in glob.glob('/Users/alexsmolen/src/github.com/alsmola/graphgrc/custom/*.md'):
        if filepath.endswith('/index.md'):
            continue

        if fix_control_file(filepath):
            count += 1
            print(f"Fixed: {os.path.basename(filepath)}")

    print(f"\nFixed {count} custom control files")

if __name__ == '__main__':
    main()
