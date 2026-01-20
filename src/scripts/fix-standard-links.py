#!/usr/bin/env python3
"""
Fix broken ../custom/ links in standards to point to ../controls/{family}/ instead.
Also updates control IDs from old format (ACC-01) to new format (iam-identity-authentication).
"""

import os
import re
from pathlib import Path

# Mapping of old custom control IDs to new control paths and families
CONTROL_MAPPING = {
    "ACC-01": ("iam", "identity-authentication"),
    "ACC-02": ("iam", "least-privilege-rbac"),
    "ACC-03": ("iam", "access-reviews"),
    "ACC-04": ("iam", "privileged-access-management"),
    "DAT-01": ("data-management", "data-classification"),
    "DAT-02": ("data-management", "encryption"),
    "DAT-03": ("data-management", "data-retention-deletion"),
    "DAT-04": ("data-management", "data-privacy-gdpr-compliance"),
    "END-01": ("endpoint-security", "device-management-macos-mdm"),
    "END-02": ("endpoint-security", "endpoint-protection"),
    "END-03": ("endpoint-security", "software-updates"),
    "GOV-01": ("governance", "security-policies"),
    "GOV-02": ("governance", "risk-assessment"),
    "INF-01": ("infrastructure-security", "cloud-security-configuration-aws"),
    "INF-02": ("infrastructure-security", "network-security"),
    "INF-03": ("infrastructure-security", "logging-monitoring"),
    "INF-04": ("infrastructure-security", "backup-recovery"),
    "OPS-01": ("operational-security", "change-management"),
    "OPS-02": ("operational-security", "vulnerability-management"),
    "OPS-03": ("operational-security", "incident-response"),
    "OPS-04": ("operational-security", "business-continuity"),
    "PEO-01": ("personnel-security", "background-checks"),
    "PEO-02": ("personnel-security", "security-training"),
    "PEO-03": ("personnel-security", "offboarding"),
    "VEN-01": ("vendor-management", "third-party-risk-assessment"),
    "VEN-02": ("vendor-management", "vendor-contracts-dpas"),
}

def fix_links_in_file(file_path):
    """Fix all ../custom/ links in a file to point to ../controls/{family}/"""
    content = file_path.read_text()
    original_content = content
    changes = []

    # Pattern: [Control Name](../custom/control-id.md)
    # Also captures the annotation if present: ^[annotation text]
    pattern = r'\[([^\]]+)\]\(\.\./custom/([a-z]{3}-\d{2})\.md\)(\s*\^[^\n]+)?'

    def replace_link(match):
        control_name = match.group(1)
        old_id = match.group(2).upper()
        annotation = match.group(3) or ''

        if old_id in CONTROL_MAPPING:
            family, slug = CONTROL_MAPPING[old_id]
            new_path = f"../controls/{family}/{slug}.md"
            changes.append(f"  {old_id} → {family}/{slug}")
            return f"[{control_name}]({new_path}){annotation}"
        else:
            print(f"  ⚠️  Unknown control ID: {old_id}")
            return match.group(0)  # Leave unchanged

    content = re.sub(pattern, replace_link, content)

    # Also update the comment line
    content = content.replace(
        "<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->",
        "<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->"
    )

    if content != original_content:
        file_path.write_text(content)
        return changes
    return None

def main():
    standards_dir = Path("docs/standards")

    if not standards_dir.exists():
        print(f"Error: {standards_dir} does not exist")
        return

    print("Fixing broken ../custom/ links in standards...\n")

    fixed_files = []
    total_changes = 0

    for standard_file in sorted(standards_dir.glob("*.md")):
        changes = fix_links_in_file(standard_file)
        if changes:
            print(f"✓ {standard_file.name}")
            for change in changes:
                print(change)
            print()
            fixed_files.append(standard_file.name)
            total_changes += len(changes)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Fixed {len(fixed_files)} files")
    print(f"Total link updates: {total_changes}")

    if fixed_files:
        print(f"\nFixed files:")
        for filename in fixed_files:
            print(f"  - {filename}")

if __name__ == '__main__':
    main()
