#!/usr/bin/env python3
"""Definitively fix the structure of all custom controls."""

import os
import re
import glob

def definitive_fix(filepath):
    """Fix structure to match the spec exactly."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Split content by the main markers
    # Find "## Audit Evidence" section end
    audit_evidence_end = re.search(r'(## Audit Evidence.*?)(?=\n---)', content, re.DOTALL)
    if not audit_evidence_end:
        print(f"Warning: Cannot find Audit Evidence in {filepath}")
        return False

    # Find Framework Mapping section
    framework_mapping = re.search(r'(## Framework Mapping\n\n<!-- This section.*?)((?=\n---)|(?=\n## Referenced By))', content, re.DOTALL)
    if not framework_mapping:
        print(f"Warning: Cannot find Framework Mapping in {filepath}")
        return False

    # Find Referenced By section
    referenced_by = re.search(r'(## Referenced By\n\n\*This section.*)', content, re.DOTALL)
    if not referenced_by:
        print(f"Warning: Cannot find Referenced By in {filepath}")
        return False

    # Get everything before Audit Evidence ends
    before_audit = content[:audit_evidence_end.end()]

    # Construct the correct structure
    correct_structure = before_audit + '\n\n---\n\n'
    correct_structure += framework_mapping.group(1).strip() + '\n\n---\n\n<!-- Backlinks auto-generated below -->\n'
    correct_structure += referenced_by.group(1).strip() + '\n'

    with open(filepath, 'w') as f:
        f.write(correct_structure)

    return True

def main():
    count = 0
    for filepath in glob.glob('/Users/alexsmolen/src/github.com/alsmola/graphgrc/custom/*.md'):
        if filepath.endswith('/index.md'):
            continue

        if definitive_fix(filepath):
            count += 1
            print(f"Fixed: {os.path.basename(filepath)}")

    print(f"\nFixed {count} custom control files")

if __name__ == '__main__':
    main()
