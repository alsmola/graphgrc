#!/usr/bin/env python3
"""Remove references to the deleted access-reviews control and replace with higher-level controls."""

import re
from pathlib import Path

# Mapping of files to replacement controls
replacements = {
    "docs/standards/aws-security-standard.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access reviews of IAM roles and policies]",
         "Cloud IAM](../controls/iam/cloud-iam.md) ^[Quarterly access reviews of IAM roles and policies validate least privilege]")
    ],
    "docs/standards/saas-iam-standard.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access reviews to identify orphaned accounts, audit log monitoring for anomalous access]",
         "SaaS IAM](../controls/iam/saas-iam.md) ^[Quarterly access reviews identify orphaned accounts in SaaS applications, audit logs monitor anomalous access]")
    ],
    "docs/standards/data-classification-standard.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Annual access reviews for Confidential data, quarterly for Restricted data]",
         "Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Access to Confidential data reviewed annually, Restricted data quarterly to enforce least privilege]")
    ],
    "docs/standards/logging-monitoring-standard.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Audit logs track authentication and authorization events with user/actor, timestamp, action, resource]",
         "Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Audit logs track privileged authentication and authorization events for access review validation]")
    ],
    "docs/policies/it-administrator.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Review access quarterly, deprovision immediately upon termination]",
         "Privileged Access Management](../controls/iam/privileged-access-management.md) ^[IT administrators review privileged access quarterly, deprovision immediately upon termination]")
    ],
    "docs/policies/hr-administrator.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Review HRIS access permissions quarterly, log all access to employee records]",
         "SaaS IAM](../controls/iam/saas-iam.md) ^[HR administrators review HRIS access permissions quarterly, all access to employee records is logged]")
    ],
    "docs/policies/data-access-policy.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access reviews with manager certification, enhanced monitoring for Restricted data]",
         "Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Quarterly access reviews ensure least privilege, manager certification required, enhanced monitoring for Restricted data]")
    ],
    "docs/processes/external-audit.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access reviews provided as audit evidence]",
         "Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Quarterly access review documentation demonstrates least privilege enforcement for audit evidence]")
    ],
    "docs/processes/internal-audit.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Internal audit validates quarterly access review completion]",
         "Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Internal audit validates quarterly access review completion and least privilege enforcement]")
    ],
    "docs/charter/governance.md": [
        ("Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access review completion at 100%, least privilege principle with time-bound permissions]",
         "Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Quarterly access review completion at 100%, enforces least privilege with time-bound permissions and role-based access]")
    ],
}

# Framework replacements - just remove the lines as they'll be regenerated
framework_files = [
    "docs/frameworks/gdpr/art32.md",
    "docs/frameworks/gdpr/art5.md",
    "docs/frameworks/soc2/cc63.md",
    "docs/frameworks/soc2/cc62.md",
]

def apply_replacements():
    repo_root = Path(__file__).parent.parent.parent
    modified_count = 0

    # Apply standard/policy/process/charter replacements
    for file_path, replacements_list in replacements.items():
        full_path = repo_root / file_path
        if not full_path.exists():
            print(f"Warning: {file_path} does not exist")
            continue

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        for old_text, new_text in replacements_list:
            content = content.replace(old_text, new_text)

        if content != original_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_count += 1
            print(f"Updated: {file_path}")

    # Remove access-reviews lines from framework files (will be regenerated)
    for file_path in framework_files:
        full_path = repo_root / file_path
        if not full_path.exists():
            continue

        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = [line for line in lines if 'access-reviews.md' not in line]

        if len(new_lines) != len(lines):
            with open(full_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            modified_count += 1
            print(f"Removed access-reviews from: {file_path}")

    print(f"\nTotal files modified: {modified_count}")

if __name__ == '__main__':
    apply_replacements()
