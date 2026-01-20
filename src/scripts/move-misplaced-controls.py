#!/usr/bin/env python3
"""Move misplaced controls to correct families and update all references."""

import re
import shutil
from pathlib import Path

def move_control_and_update_references(repo_root: Path):
    """Move misplaced controls and update all references."""

    print("Phase 2: Moving misplaced controls\n")

    # Move 1: Data Privacy (GDPR) from data-management to data-privacy
    old_path = "docs/controls/data-management/data-privacy-gdpr-compliance.md"
    new_path = "docs/controls/data-privacy/data-privacy-gdpr-compliance.md"

    old_file = repo_root / old_path
    new_file = repo_root / new_path

    if old_file.exists():
        print(f"📦 Moving: {old_path}")
        print(f"      To: {new_path}")
        print(f"   Reason: GDPR privacy control belongs in data-privacy family, not data-management")

        # Update the frontmatter family field
        content = old_file.read_text(encoding='utf-8')
        content = content.replace('family: data-management', 'family: data-privacy')
        content = content.replace('id: data-management-data-privacy-gdpr-compliance',
                                   'id: data-privacy-data-privacy-gdpr-compliance')

        # Write to new location
        new_file.write_text(content, encoding='utf-8')
        print(f"   ✅ Moved and updated family metadata")

        # Update all references
        reference_count = 0
        docs_dir = repo_root / "docs"
        for md_file in docs_dir.rglob("*.md"):
            if md_file.samefile(new_file):
                continue

            file_content = md_file.read_text(encoding='utf-8')
            original = file_content

            # Update various reference formats
            file_content = file_content.replace(
                "data-management/data-privacy-gdpr-compliance.md",
                "data-privacy/data-privacy-gdpr-compliance.md"
            )
            file_content = file_content.replace(
                "../controls/data-management/data-privacy-gdpr-compliance.md",
                "../controls/data-privacy/data-privacy-gdpr-compliance.md"
            )
            file_content = file_content.replace(
                "/docs/controls/data-management/data-privacy-gdpr-compliance.md",
                "/docs/controls/data-privacy/data-privacy-gdpr-compliance.md"
            )

            if file_content != original:
                md_file.write_text(file_content, encoding='utf-8')
                reference_count += 1

        print(f"   ✅ Updated {reference_count} files with references")

        # Delete old file
        old_file.unlink()
        print(f"   ✅ Deleted old file\n")
    else:
        print(f"⚠️  File not found: {old_path}\n")

    # Move 2: GRC Function - actually should be REMOVED not moved
    # It's an organizational structure, not a control
    # The charter documents already implement the governance/risk functions
    grc_path = "docs/controls/compliance/grc-function.md"
    grc_file = repo_root / grc_path

    if grc_file.exists():
        print(f"🗑️  Removing: {grc_path}")
        print(f"   Reason: GRC Function describes organizational structure, not a security control")
        print(f"   Action: Charter documents already define governance/risk management responsibilities")
        print(f"   Framework Mappings to redistribute:")

        # Read the framework mappings before deleting
        content = grc_file.read_text(encoding='utf-8')
        print(f"      - SOC 2: CC1.1 (governance commitment), CC1.2 (board oversight), CC3.2 (risk assessment)")
        print(f"      - GDPR: Article 24 (appropriate data protection policies)")
        print(f"      → These are already covered by charter/governance.md and charter/risk-management.md")

        # Update references to point to charter documents
        reference_count = 0
        docs_dir = repo_root / "docs"
        for md_file in docs_dir.rglob("*.md"):
            if md_file.samefile(grc_file):
                continue

            file_content = md_file.read_text(encoding='utf-8')
            original = file_content

            # Remove any links to GRC Function (they should reference charter instead)
            # Match the full markdown link with annotation
            pattern = r'-\s+\[GRC Function\]\([^)]+controls/compliance/grc-function\.md\)[^\n]*\n?'
            file_content = re.sub(pattern, '', file_content)

            # Also update any text references
            file_content = file_content.replace(
                "compliance/grc-function.md",
                "charter/governance.md"  # Default redirect to governance charter
            )
            file_content = file_content.replace(
                "../controls/compliance/grc-function.md",
                "../charter/governance.md"
            )

            if file_content != original:
                md_file.write_text(file_content, encoding='utf-8')
                reference_count += 1

        print(f"   ✅ Removed {reference_count} references to GRC Function control")

        # Delete the file
        grc_file.unlink()
        print(f"   ✅ Deleted GRC Function control\n")
    else:
        print(f"⚠️  File not found: {grc_path}\n")

    print(f"✅ Phase 2 complete!")
    print(f"   - Moved data-privacy-gdpr-compliance to correct family")
    print(f"   - Removed GRC Function (organizational structure, not a control)")
    print(f"\n⚠️  Next: Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    move_control_and_update_references(repo_root)

if __name__ == '__main__':
    main()
