#!/usr/bin/env python3
"""Final cleanup of custom control structure."""

import os
import re
import glob

def final_cleanup(filepath):
    """Fix the structure to have Framework Mapping right before Referenced By."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove the stray "<!-- Backlinks auto-generated below -->" comment if it appears before Framework Mapping
    content = re.sub(r'---\s*\n\s*<!-- Backlinks auto-generated below -->\s*\n\s*---\s*\n\s*## Framework Mapping',
                     '---\n\n## Framework Mapping', content)

    # Ensure the comment appears right before Referenced By
    # First, remove any existing "<!-- Backlinks auto-generated below -->" comments
    content = re.sub(r'<!-- Backlinks auto-generated below -->\s*\n\s*', '', content)

    # Add it back right before "## Referenced By"
    content = re.sub(r'(###? .*?\n.*?\n)\s*## Referenced By',
                     r'\1\n---\n\n<!-- Backlinks auto-generated below -->\n## Referenced By', content)

    with open(filepath, 'w') as f:
        f.write(content)

def main():
    for filepath in glob.glob('/Users/alexsmolen/src/github.com/engseclabs/graphgrc/custom/*.md'):
        if filepath.endswith('/index.md'):
            continue

        final_cleanup(filepath)
        print(f"Cleaned: {os.path.basename(filepath)}")

if __name__ == '__main__':
    main()
