#!/usr/bin/env python3
"""
Remove all references to the old ../custom/ directory from process files.
These were template files that were never updated after the custom-to-controls migration.
"""

import re
from pathlib import Path

def remove_control_mapping_section(content):
    """Remove the entire Control Mapping section that references ../custom/"""

    # Pattern to match the Control Mapping section with custom links
    pattern = r'## Control Mapping\s*\n\s*<!-- This section.*?-->\s*<!-- Add links to custom controls.*?-->\s*\n(- \[.*?\]\(\.\.\/custom\/.*?\).*?\n)+\s*---'

    # Replace with empty string
    cleaned = re.sub(pattern, '---', content, flags=re.DOTALL)

    return cleaned

def main():
    process_files = [
        'docs/processes/access-provisioning-process.md',
        'docs/processes/access-review-process.md',
        'docs/processes/backup-recovery-process.md',
        'docs/processes/change-management-process.md',
        'docs/processes/data-breach-response-process.md',
        'docs/processes/incident-response-process.md',
        'docs/processes/security-training-process.md',
        'docs/processes/vendor-risk-assessment-process.md',
        'docs/processes/vulnerability-management-process.md',
    ]

    updated_count = 0

    for file_path in process_files:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue

        content = path.read_text()

        # Check if it has custom references
        if '../custom/' not in content:
            print(f"✓ No custom references: {file_path}")
            continue

        # Remove the Control Mapping section
        cleaned_content = remove_control_mapping_section(content)

        # Write back
        path.write_text(cleaned_content)
        updated_count += 1
        print(f"✓ Cleaned: {file_path}")

    # Also update link-validation.md
    link_val_path = Path('docs/link-validation.md')
    if link_val_path.exists():
        content = link_val_path.read_text()
        if '../custom/' in content:
            # Remove lines mentioning custom directory
            lines = content.split('\n')
            filtered_lines = [line for line in lines if '../custom/' not in line]
            link_val_path.write_text('\n'.join(filtered_lines))
            updated_count += 1
            print(f"✓ Cleaned: docs/link-validation.md")

    print(f"\n{'='*60}")
    print(f"Updated {updated_count} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
