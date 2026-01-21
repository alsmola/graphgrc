#!/usr/bin/env python3
"""Remove least-privilege-rbac control and redistribute framework mappings."""

import re
from pathlib import Path

def remove_least_privilege_rbac(repo_root: Path):
    """Remove least-privilege-rbac control and update references."""

    print("Removing least-privilege-rbac control\n")

    control_path = "docs/controls/iam/least-privilege-rbac.md"
    control_file = repo_root / control_path

    if not control_file.exists():
        print(f"⚠️  File not found: {control_path}")
        return

    print(f"📋 Analyzing least-privilege-rbac control:")
    print(f"   Framework Mappings:")
    print(f"      - SOC 2 CC6.3: Access authorization based on roles")
    print(f"      - GDPR Article 32: Minimizes unauthorized access risk")
    print(f"      - GDPR Article 25: Data protection by design")
    print()
    print(f"   Redistribution Strategy:")
    print(f"      → Cloud IAM: AWS-specific RBAC implementation")
    print(f"      → SaaS IAM: SaaS-specific RBAC implementation")
    print(f"      → Privileged Access Management: Elevated access approval/time-limiting")
    print()

    # Remove all references to this control
    # Most references are in "Implemented By" sections which will be auto-regenerated
    # We need to update "Control Mapping" sections in implementation docs
    reference_count = 0
    docs_dir = repo_root / "docs"

    for md_file in docs_dir.rglob("*.md"):
        if md_file.samefile(control_file):
            continue

        file_content = md_file.read_text(encoding='utf-8')
        original = file_content

        # Remove links to least-privilege-rbac
        # Pattern: - [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[annotation]
        pattern = r'-\s+\[Least Privilege & RBAC\]\([^)]*least-privilege-rbac\.md\)[^\n]*\n?'
        file_content = re.sub(pattern, '', file_content)

        # Also handle variations
        file_content = file_content.replace(
            "iam/least-privilege-rbac.md",
            "iam/cloud-iam.md"  # Default redirect to cloud-iam
        )
        file_content = file_content.replace(
            "../controls/iam/least-privilege-rbac.md",
            "../controls/iam/cloud-iam.md"
        )

        if file_content != original:
            md_file.write_text(file_content, encoding='utf-8')
            reference_count += 1

    print(f"   ✅ Removed {reference_count} references to least-privilege-rbac")

    # Delete the control file
    control_file.unlink()
    print(f"   ✅ Deleted {control_path}\n")

    print(f"⚠️  Manual Steps Required:")
    print(f"   1. Add framework mappings to appropriate controls:")
    print(f"      - Add CC6.3, Article 25, Article 32 to cloud-iam.md")
    print(f"      - Add CC6.3, Article 25, Article 32 to saas-iam.md")
    print(f"      - Add CC6.3, Article 32 to privileged-access-management.md")
    print()
    print(f"   2. Run 'make generate-backlinks' to update all backlink sections")
    print()
    print(f"   Note: Many implementation docs (standards/policies/processes) referenced")
    print(f"         least-privilege-rbac. Their Control Mapping sections should now point")
    print(f"         to Cloud IAM, SaaS IAM, or Privileged Access Management instead.")

def main():
    repo_root = Path(__file__).parent.parent.parent
    remove_least_privilege_rbac(repo_root)

if __name__ == '__main__':
    main()
