#!/usr/bin/env python3
"""Consolidate duplicate controls by removing thin/duplicate versions and updating all references."""

import re
from pathlib import Path

# Map of files to delete → replacement control paths
DUPLICATE_REPLACEMENTS = {
    "docs/controls/data-management/encryption.md": {
        "replacement": "docs/controls/cryptography/",
        "note": "Duplicate of cryptography family controls",
        "redirect_to": [
            ("Encryption at Rest", "docs/controls/cryptography/encryption-at-rest.md"),
            ("Encryption in Transit", "docs/controls/cryptography/encryption-in-transit.md"),
            ("Key Management", "docs/controls/cryptography/key-management.md"),
        ]
    },
    "docs/controls/data-management/data-retention-deletion.md": {
        "replacement": "docs/controls/data-management/data-retention-and-deletion.md",
        "note": "Thin duplicate - keep detailed version with quarterly cadence",
        "redirect_to": [
            ("Data Retention & Deletion", "docs/controls/data-management/data-retention-and-deletion.md"),
        ]
    },
    "docs/controls/operational-security/incident-response.md": {
        "replacement": "docs/controls/incident-response/security-incident-response.md",
        "note": "Exact duplicate - keep incident-response family version",
        "redirect_to": [
            ("Security Incident Response", "docs/controls/incident-response/security-incident-response.md"),
        ]
    },
    "docs/controls/change-management/change-management.md": {
        "replacement": "docs/controls/operational-security/change-management.md",
        "note": "Skeleton version - keep detailed operational-security version",
        "redirect_to": [
            ("Change Management", "docs/controls/operational-security/change-management.md"),
        ]
    },
}

def update_references_in_file(file_path: Path, old_path: str, new_path: str) -> bool:
    """Update references from old_path to new_path in a file. Returns True if modified."""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # Convert paths to relative link format
        # e.g., "data-management/encryption.md" or "../controls/data-management/encryption.md"

        # Pattern 1: Direct markdown links
        old_link_pattern = re.escape(old_path)
        new_link = new_path
        content = re.sub(old_link_pattern, new_link, content)

        # Pattern 2: Framework backlinks (absolute paths like /docs/controls/...)
        old_absolute = f"/docs/{old_path}"
        new_absolute = f"/docs/{new_path}"
        content = re.sub(re.escape(old_absolute), new_absolute, content)

        # Pattern 3: Relative paths from different directories
        # ../controls/data-management/encryption.md → ../controls/cryptography/encryption-at-rest.md
        old_relative_controls = old_path.replace("docs/controls/", "../controls/")
        new_relative_controls = new_path.replace("docs/controls/", "../controls/")
        content = re.sub(re.escape(old_relative_controls), new_relative_controls, content)

        # Pattern 4: From within controls directory
        old_within_controls = old_path.replace("docs/controls/", "")
        new_within_controls = new_path.replace("docs/controls/", "")
        content = re.sub(re.escape(old_within_controls), new_within_controls, content)

        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def delete_control_and_update_references(repo_root: Path):
    """Delete duplicate controls and update all references."""
    modified_files = []

    print("Phase 1: Deleting duplicate controls and updating references\n")

    for old_path, info in DUPLICATE_REPLACEMENTS.items():
        file_to_delete = repo_root / old_path

        if not file_to_delete.exists():
            print(f"⚠️  File not found (may already be deleted): {old_path}")
            continue

        print(f"🗑️  Deleting: {old_path}")
        print(f"   Reason: {info['note']}")
        print(f"   Replacement: {info['replacement']}")

        # For encryption.md, we need special handling since it maps to multiple controls
        if "encryption.md" in old_path:
            print("   ⚠️  SPECIAL CASE: This control duplicates the entire cryptography family")
            print("   Manual review required for framework mappings - they should be distributed across:")
            for name, path in info['redirect_to']:
                print(f"      - {name}: {path}")
            print()

        # Find all files that reference this control
        print(f"   Searching for references to update...")
        docs_dir = repo_root / "docs"
        reference_count = 0

        # Search in all markdown files
        for md_file in docs_dir.rglob("*.md"):
            # Skip the file we're about to delete
            if md_file.samefile(file_to_delete):
                continue

            # For single replacements, do direct substitution
            if len(info['redirect_to']) == 1:
                new_name, new_path = info['redirect_to'][0]
                if update_references_in_file(md_file, old_path, new_path):
                    reference_count += 1
                    modified_files.append(str(md_file.relative_to(repo_root)))

        print(f"   ✅ Updated {reference_count} files with references")

        # Delete the duplicate file
        file_to_delete.unlink()
        print(f"   ✅ Deleted {old_path}\n")

    print(f"\n📊 Summary:")
    print(f"   Deleted: {len(DUPLICATE_REPLACEMENTS)} duplicate controls")
    print(f"   Updated: {len(set(modified_files))} files with references")

    if modified_files:
        print(f"\n📝 Modified files:")
        for f in sorted(set(modified_files)):
            print(f"   - {f}")

    print(f"\n⚠️  MANUAL REVIEW NEEDED:")
    print(f"   - data-management/encryption.md had framework mappings that should be")
    print(f"     distributed across the cryptography family controls")
    print(f"   - Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    delete_control_and_update_references(repo_root)

if __name__ == '__main__':
    main()
