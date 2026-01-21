#!/usr/bin/env python3
"""Remove additional controls: least-privilege-rbac and data-privacy-gdpr-compliance."""

import re
from pathlib import Path

def remove_controls(repo_root: Path):
    """Remove specified controls and update references."""

    print("Removing additional controls\n")

    controls_to_remove = [
        {
            "path": "docs/controls/iam/least-privilege-rbac.md",
            "name": "Least Privilege & RBAC",
            "reason": "Vague umbrella term - covered by Cloud IAM, SaaS IAM, Privileged Access Management",
            "framework_mappings": [
                "SOC 2 CC6.3 (access authorization based on roles)",
                "GDPR Article 32 (minimize unauthorized access)",
                "GDPR Article 25 (data protection by design)"
            ],
            "redistribute_to": [
                ("Cloud IAM", "cloud-iam.md"),
                ("SaaS IAM", "saas-iam.md"),
                ("Privileged Access Management", "privileged-access-management.md")
            ]
        },
        {
            "path": "docs/controls/data-privacy/data-privacy-gdpr-compliance.md",
            "name": "Data Privacy (GDPR Compliance)",
            "reason": "GDPR-specific privacy - covered by Customer Personal Data and Employee Personal Data",
            "framework_mappings": [
                "SOC 2 P11 (privacy notice to data subjects)",
                "SOC 2 P21 (choice and consent mechanisms)",
                "GDPR Article 5 (lawful, fair, transparent processing)",
                "GDPR Article 6 (lawful basis for processing)",
                "GDPR Article 13 (information to data subjects)",
                "GDPR Article 24 (appropriate measures for compliance)"
            ],
            "redistribute_to": [
                ("Customer Personal Data", "customer-personal-data.md"),
                ("Employee Personal Data", "employee-personal-data.md")
            ]
        }
    ]

    total_removed_references = 0

    for control_info in controls_to_remove:
        control_path = control_info["path"]
        control_file = repo_root / control_path

        if not control_file.exists():
            print(f"⚠️  File not found: {control_path}\n")
            continue

        print(f"🗑️  Removing: {control_path}")
        print(f"   Name: {control_info['name']}")
        print(f"   Reason: {control_info['reason']}")
        print(f"   Framework Mappings:")
        for mapping in control_info["framework_mappings"]:
            print(f"      - {mapping}")
        print(f"   Redistribute to:")
        for name, path in control_info["redistribute_to"]:
            print(f"      - {name} ({path})")
        print()

        # Remove all references to this control
        reference_count = 0
        docs_dir = repo_root / "docs"

        # Extract short filename for pattern matching
        control_filename = Path(control_path).name

        for md_file in docs_dir.rglob("*.md"):
            if md_file.samefile(control_file):
                continue

            file_content = md_file.read_text(encoding='utf-8')
            original = file_content

            # Remove links with patterns
            # Pattern 1: Full markdown link with annotation
            pattern1 = rf'-\s+\[{re.escape(control_info["name"])}\]\([^)]*{re.escape(control_filename)}\)[^\n]*\n?'
            file_content = re.sub(pattern1, '', file_content)

            # Pattern 2: Simple path replacements
            file_content = file_content.replace(control_filename, "")

            # Pattern 3: Relative paths
            if "iam/least-privilege-rbac.md" in control_path:
                file_content = file_content.replace("iam/least-privilege-rbac.md", "iam/cloud-iam.md")
                file_content = file_content.replace("../controls/iam/least-privilege-rbac.md", "../controls/iam/cloud-iam.md")
            elif "data-privacy/data-privacy-gdpr-compliance.md" in control_path:
                file_content = file_content.replace("data-privacy/data-privacy-gdpr-compliance.md", "data-privacy/customer-personal-data.md")
                file_content = file_content.replace("../controls/data-privacy/data-privacy-gdpr-compliance.md", "../controls/data-privacy/customer-personal-data.md")

            if file_content != original:
                md_file.write_text(file_content, encoding='utf-8')
                reference_count += 1

        print(f"   ✅ Removed {reference_count} references")
        total_removed_references += reference_count

        # Delete the control file
        control_file.unlink()
        print(f"   ✅ Deleted {control_path}\n")

    print(f"📊 Summary:")
    print(f"   Deleted: {len(controls_to_remove)} controls")
    print(f"   Updated: {total_removed_references} files with references")
    print()
    print(f"⚠️  Next Steps:")
    print(f"   1. Add framework mappings to appropriate controls:")
    print(f"      - Cloud IAM: Add CC6.3, Article 25, Article 32")
    print(f"      - SaaS IAM: Add CC6.3, Article 25, Article 32")
    print(f"      - Privileged Access Management: Add CC6.3, Article 32")
    print(f"      - Customer Personal Data: Add P11, P21, Articles 5/6/13/24")
    print(f"      - Employee Personal Data: Add Articles 5/6/13/24")
    print()
    print(f"   2. Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    remove_controls(repo_root)

if __name__ == '__main__':
    main()
