#!/usr/bin/env python3
"""Clean up multiple --- separators in custom control files."""

import os
import re
import glob

def clean_file(filepath):
    """Remove duplicate --- separators."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace multiple consecutive --- separators with just one
    # Pattern: --- followed by optional whitespace, then another ---
    while re.search(r'---\s*\n\s*---', content):
        content = re.sub(r'---\s*\n\s*---', '---', content)

    # Ensure proper spacing: exactly one blank line after --- before ## Framework Mapping
    content = re.sub(r'---\s*\n+## Framework Mapping', '---\n\n## Framework Mapping', content)

    # Ensure proper spacing between Framework Mapping and Referenced By (two blank lines)
    content = re.sub(r'(### GDPR\n.*?\n)\s*\n+## Referenced By', r'\1\n\n## Referenced By', content)

    with open(filepath, 'w') as f:
        f.write(content)

def main():
    for filepath in glob.glob('/Users/alexsmolen/src/github.com/engseclabs/graphgrc/custom/*.md'):
        if filepath.endswith('/index.md'):
            continue

        clean_file(filepath)
        print(f"Cleaned: {os.path.basename(filepath)}")

if __name__ == '__main__':
    main()
