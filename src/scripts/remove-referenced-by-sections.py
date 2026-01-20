#!/usr/bin/env python3
"""Remove Referenced By sections from standards/policies/processes/charter files."""

import re
from pathlib import Path

def remove_referenced_by(file_path):
    """Remove Referenced By section from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it has a Referenced By section
    if '## Referenced By' not in content:
        return False

    # Remove the entire Referenced By section (from header to end of file or next ## section)
    pattern = r'^---\s*\n\n## Referenced By\n\n.*$'
    new_content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)

    # If that didn't work, try without the leading ---
    if new_content == content:
        pattern = r'^## Referenced By\n\n.*$'
        new_content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)

    # Write back if changed
    if new_content != content:
        # Clean up trailing whitespace
        new_content = new_content.rstrip() + '\n'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    repo_root = Path(__file__).parent.parent.parent
    docs_dir = repo_root / 'docs'

    directories = ['standards', 'policies', 'processes', 'charter']

    modified_count = 0
    total_count = 0

    for dir_name in directories:
        dir_path = docs_dir / dir_name
        if not dir_path.exists():
            continue

        for md_file in dir_path.rglob('*.md'):
            total_count += 1
            if remove_referenced_by(md_file):
                modified_count += 1
                print(f"Removed from: {md_file.relative_to(repo_root)}")

    print(f"\nProcessed {total_count} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
