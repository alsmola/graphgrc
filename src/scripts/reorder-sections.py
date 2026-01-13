#!/usr/bin/env python3
"""Reorder custom control sections to ensure Framework Mapping comes right before Referenced By."""

import os
import re
import glob

def reorder_custom_control(filepath):
    """Reorder sections in a custom control file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract the frontmatter
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if not frontmatter_match:
        print(f"Warning: No frontmatter found in {filepath}")
        return False

    frontmatter = frontmatter_match.group(1)
    rest = content[len(frontmatter):]

    # Skip any blank lines between frontmatter and title
    leading_newlines = ''
    while rest.startswith('\n'):
        leading_newlines += '\n'
        rest = rest[1:]

    # Extract the title (H1)
    title_match = re.match(r'^(# .*?\n)', rest)
    if not title_match:
        print(f"Warning: No title found in {filepath}")
        return False

    title = title_match.group(1)
    rest = rest[len(title):]

    # Skip any blank lines after title
    while rest.startswith('\n'):
        rest = rest[1:]

    # Split into sections
    sections = {}
    current_section = None
    current_content = []

    for line in rest.split('\n'):
        if line.startswith('## '):
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content)

            # Start new section
            current_section = line[3:].strip()
            current_content = [line]
        else:
            current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content)

    # Define the desired order
    desired_order = [
        'Objective',
        'Description',
        'Implementation Details',
        'Examples',
        'Audit Evidence',
        'Framework Mapping',
        'Referenced By'
    ]

    # Rebuild content in correct order
    new_content = frontmatter + leading_newlines + title

    for i, section_name in enumerate(desired_order):
        if section_name in sections:
            section_content = sections[section_name]

            # Add separator before Framework Mapping
            if section_name == 'Framework Mapping':
                new_content += '---\n\n'

            new_content += section_content

            # Add appropriate spacing after section
            if section_name == 'Framework Mapping':
                # Just one newline before Referenced By section
                new_content += '\n\n'
            elif i < len(desired_order) - 1:  # Not the last section
                new_content += '\n\n'

    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content.rstrip() + '\n')

    return True

def main():
    count = 0
    for filepath in glob.glob('/Users/alexsmolen/src/github.com/engseclabs/graphgrc/custom/*.md'):
        if filepath.endswith('/index.md'):
            continue

        if reorder_custom_control(filepath):
            count += 1
            print(f"Reordered: {os.path.basename(filepath)}")

    print(f"\nReordered {count} custom control files")

if __name__ == '__main__':
    main()
