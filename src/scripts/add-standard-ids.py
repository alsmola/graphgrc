#!/usr/bin/env python3
"""
Add 'id' field to frontmatter of all standards.
ID is derived from filename (e.g., cryptography-standard.md → standard-cryptography).
"""

import re
from pathlib import Path

def add_id_to_frontmatter(file_path):
    """Add id field to frontmatter if missing."""
    content = file_path.read_text()

    # Check if frontmatter exists
    if not content.startswith('---\n'):
        print(f"  ⚠️  No frontmatter found")
        return False

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        print(f"  ⚠️  Could not parse frontmatter")
        return False

    frontmatter = match.group(1)
    body = match.group(2)

    # Check if id already exists
    if re.search(r'^id:', frontmatter, re.MULTILINE):
        print(f"  ⏭️  Already has ID")
        return False

    # Generate ID from filename
    filename = file_path.stem  # e.g., "cryptography-standard"
    # Remove "-standard" suffix if present
    if filename.endswith('-standard'):
        standard_id = f"standard-{filename[:-9]}"  # e.g., "standard-cryptography"
    else:
        standard_id = f"standard-{filename}"

    # Add id as second line (after type)
    lines = frontmatter.split('\n')
    new_lines = []
    id_added = False

    for line in lines:
        new_lines.append(line)
        if line.startswith('type:') and not id_added:
            new_lines.append(f'id: {standard_id}')
            id_added = True

    # Reconstruct content
    new_frontmatter = '\n'.join(new_lines)
    new_content = f'---\n{new_frontmatter}\n---\n{body}'

    file_path.write_text(new_content)
    print(f"  ✓ Added ID: {standard_id}")
    return True

def main():
    standards_dir = Path("docs/standards")

    if not standards_dir.exists():
        print(f"Error: {standards_dir} does not exist")
        return

    print("Adding IDs to standards...\n")

    updated = []

    for standard_file in sorted(standards_dir.glob("*.md")):
        print(f"{standard_file.name}")
        if add_id_to_frontmatter(standard_file):
            updated.append(standard_file.name)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Updated {len(updated)} files")

    if updated:
        print(f"\nUpdated files:")
        for filename in updated:
            print(f"  - {filename}")

if __name__ == '__main__':
    main()
