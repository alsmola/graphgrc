#!/usr/bin/env python3
"""Remove data-access-policy - its control mappings should be in baseline-security-policy."""

import re
from pathlib import Path

def remove_data_access_policy(repo_root: Path):
    """Remove data-access-policy and update references."""

    print("Removing data-access-policy\n")

    policy_path = "docs/policies/data-access-policy.md"
    policy_file = repo_root / policy_path

    if not policy_file.exists():
        print(f"⚠️  File not found: {policy_path}")
        return

    print(f"📋 Analyzing data-access-policy:")
    print(f"   Type: Policy document (not a control)")
    print(f"   Content: Data access requirements, classification review, access principles")
    print(f"   Control Mappings:")
    print(f"      - Data Classification")
    print(f"      - Customer/Employee Personal Data")
    print(f"      - Encryption at Rest/In Transit")
    print(f"      - Data Retention")
    print(f"      - Data Breach Response")
    print(f"      - Logging & Monitoring")
    print()
    print(f"   Redistribution Strategy:")
    print(f"      → Baseline Security Policy: Core data access requirements")
    print(f"      → Individual control mappings will be removed (policies link to controls, not vice versa)")
    print()

    # Remove all references to this policy
    reference_count = 0
    docs_dir = repo_root / "docs"

    for md_file in docs_dir.rglob("*.md"):
        if md_file.samefile(policy_file):
            continue

        file_content = md_file.read_text(encoding='utf-8')
        original = file_content

        # Remove links to data-access-policy
        # Pattern: - [Data Access Policy](../policies/data-access-policy.md) ^[annotation]
        pattern = r'-\s+\[.*Data Access Policy.*\]\([^)]*data-access-policy\.md\)[^\n]*\n?'
        file_content = re.sub(pattern, '', file_content, flags=re.IGNORECASE)

        # Also handle direct path references
        file_content = file_content.replace("data-access-policy.md", "baseline-security-policy.md")
        file_content = file_content.replace("../policies/data-access-policy.md", "../policies/baseline-security-policy.md")
        file_content = file_content.replace("/policies/data-access-policy.md", "/policies/baseline-security-policy.md")

        if file_content != original:
            md_file.write_text(file_content, encoding='utf-8')
            reference_count += 1

    print(f"   ✅ Removed {reference_count} references to data-access-policy")

    # Delete the policy file
    policy_file.unlink()
    print(f"   ✅ Deleted {policy_path}\n")

    print(f"✅ Complete!")
    print(f"   Note: This was a policy document, not a control.")
    print(f"   Its control mappings were forward links (policy → controls).")
    print(f"   When we regenerate backlinks, controls will no longer show")
    print(f"   data-access-policy in their 'Implemented By' sections.")
    print()
    print(f"⚠️  Next: Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    remove_data_access_policy(repo_root)

if __name__ == '__main__':
    main()
