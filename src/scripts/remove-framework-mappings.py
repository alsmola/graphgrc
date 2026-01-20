#!/usr/bin/env python3
"""Remove 'Framework Mappings' sections from framework files."""

import os
import re
from pathlib import Path

def remove_framework_mappings(file_path):
    """Remove Framework Mappings section from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match ### Framework Mappings (h3) followed by bullet points
    pattern = r'^### Framework Mappings\n(?:^-.*\n)*'

    # Remove the section
    new_content = re.sub(pattern, '', content, flags=re.MULTILINE)

    # Also handle ## Framework Mappings (h2) at end of file
    pattern2 = r'^## Framework Mappings\n(?:^-.*\n)*'
    new_content = re.sub(pattern2, '', new_content, flags=re.MULTILINE)

    # Write back if changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    repo_root = Path(__file__).parent.parent.parent
    frameworks_dir = repo_root / 'docs' / 'frameworks'

    if not frameworks_dir.exists():
        print(f"Error: {frameworks_dir} does not exist")
        return

    modified_count = 0
    total_count = 0

    for md_file in frameworks_dir.rglob('*.md'):
        if md_file.name == 'index.md':
            continue

        total_count += 1
        if remove_framework_mappings(md_file):
            modified_count += 1
            print(f"Cleaned: {md_file.relative_to(repo_root)}")

    print(f"\nProcessed {total_count} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
