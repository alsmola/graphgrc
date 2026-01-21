#!/usr/bin/env python3
"""Remove policy documents: data-access-policy, engineering-security-policy, baseline-security-policy."""

import re
from pathlib import Path

def remove_policies(repo_root: Path):
    """Remove specified policy documents and update references."""

    print("Removing policy documents\n")

    policies_to_remove = [
        {
            "path": "docs/policies/data-access-policy.md",
            "name": "Data Access Policy",
            "reason": "Redundant policy - access requirements covered by individual control implementations"
        },
        {
            "path": "docs/policies/engineering-security-policy.md",
            "name": "Engineering Security Policy",
            "reason": "Redundant with engineer.md - same target audience"
        },
        {
            "path": "docs/policies/baseline-security-policy.md",
            "name": "Baseline Security Policy",
            "reason": "Generic policy - specific requirements better captured in controls and role-specific policies"
        }
    ]

    total_removed_references = 0

    for policy_info in policies_to_remove:
        policy_path = policy_info["path"]
        policy_file = repo_root / policy_path

        if not policy_file.exists():
            print(f"⚠️  File not found: {policy_path}\n")
            continue

        print(f"🗑️  Removing: {policy_path}")
        print(f"   Name: {policy_info['name']}")
        print(f"   Reason: {policy_info['reason']}")
        print()

        # Remove all references to this policy
        reference_count = 0
        docs_dir = repo_root / "docs"

        # Extract filename for pattern matching
        policy_filename = Path(policy_path).name

        for md_file in docs_dir.rglob("*.md"):
            if md_file.samefile(policy_file):
                continue

            file_content = md_file.read_text(encoding='utf-8')
            original = file_content

            # Remove links with patterns
            # Pattern 1: Full markdown link with annotation
            pattern1 = rf'-\s+\[.*{re.escape(policy_info["name"])}.*\]\([^)]*{re.escape(policy_filename)}\)[^\n]*\n?'
            file_content = re.sub(pattern1, '', file_content, flags=re.IGNORECASE)

            # Pattern 2: Simple filename replacements
            file_content = file_content.replace(policy_filename, "")

            # Pattern 3: Relative paths
            file_content = file_content.replace(f"../policies/{policy_filename}", "")
            file_content = file_content.replace(f"/policies/{policy_filename}", "")
            file_content = file_content.replace(f"policies/{policy_filename}", "")

            if file_content != original:
                md_file.write_text(file_content, encoding='utf-8')
                reference_count += 1

        print(f"   ✅ Removed {reference_count} references")
        total_removed_references += reference_count

        # Delete the policy file
        policy_file.unlink()
        print(f"   ✅ Deleted {policy_path}\n")

    print(f"📊 Summary:")
    print(f"   Deleted: {len(policies_to_remove)} policy documents")
    print(f"   Updated: {total_removed_references} files with references")
    print()
    print(f"✅ Complete!")
    print(f"   Note: These were policy documents (implementation docs), not controls.")
    print(f"   Their Control Mapping sections contained forward links (policy → controls).")
    print(f"   When we regenerate backlinks, controls will no longer show these")
    print(f"   policies in their 'Implemented By' sections.")
    print()
    print(f"⚠️  Next: Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    remove_policies(repo_root)

if __name__ == '__main__':
    main()
