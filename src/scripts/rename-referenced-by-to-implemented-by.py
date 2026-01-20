#!/usr/bin/env python3
"""Rename 'Referenced By' to 'Implemented By' in control files."""

import re
from pathlib import Path

def rename_header(file_path):
    """Rename Referenced By header to Implemented By."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it has a Referenced By section
    if '## Referenced By' not in content:
        return False

    # Replace the header
    new_content = content.replace('## Referenced By', '## Implemented By')

    # Write back if changed
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
        if rename_header(control_file):
            modified_count += 1
            print(f"Renamed in: {control_file.relative_to(repo_root)}")

    print(f"\nProcessed {total_count} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
