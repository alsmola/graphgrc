#!/usr/bin/env python3
"""Consolidate overlapping logging/monitoring controls."""

import re
from pathlib import Path

def consolidate_logging_monitoring(repo_root: Path):
    """Consolidate infrastructure-security/logging-monitoring and monitoring/infrastructure-observability."""

    print("Phase 3: Consolidating logging/monitoring overlap\n")

    # Files involved
    keep_file = "docs/controls/infrastructure-security/logging-monitoring.md"
    remove_file = "docs/controls/monitoring/infrastructure-observability.md"

    keep_path = repo_root / keep_file
    remove_path = repo_root / remove_file

    if not remove_path.exists():
        print(f"⚠️  File not found: {remove_file}")
        return

    # Read the file we're removing to extract unique content
    remove_content = remove_path.read_text(encoding='utf-8')

    # Check for unique framework mappings
    # infrastructure-observability has A11 (availability) that logging-monitoring doesn't have
    print(f"📋 Analyzing controls to merge:")
    print(f"   KEEP: {keep_file} (more detailed, security-focused)")
    print(f"   REMOVE: {remove_file} (thin, infrastructure-focused)")
    print()
    print(f"   Unique framework mapping in removed control:")
    print(f"      - SOC 2 A11: Infrastructure monitoring measures capacity and system component usage")
    print(f"   → Will add this to the kept control\n")

    # Update the kept file with the unique framework mapping
    keep_content = keep_path.read_text(encoding='utf-8')

    # Find the SOC 2 section and add A11
    soc2_section = keep_content.find("### SOC 2")
    if soc2_section != -1:
        # Find the end of SOC 2 section (next ### or ---)
        next_section = keep_content.find("\n###", soc2_section + 1)
        if next_section == -1:
            next_section = keep_content.find("\n---", soc2_section + 1)

        # Insert A11 before the next section
        insertion_point = next_section
        new_line = "- [A11](../../frameworks/soc2/a11.md) ^[Infrastructure monitoring measures capacity and system component usage]\n"
        keep_content = keep_content[:insertion_point] + new_line + keep_content[insertion_point:]

        # Write back
        keep_path.write_text(keep_content, encoding='utf-8')
        print(f"   ✅ Added SOC 2 A11 mapping to {keep_file}")

    # Update all references to point to the kept file
    reference_count = 0
    docs_dir = repo_root / "docs"

    for md_file in docs_dir.rglob("*.md"):
        if md_file.samefile(remove_path) or md_file.samefile(keep_path):
            continue

        file_content = md_file.read_text(encoding='utf-8')
        original = file_content

        # Update various reference formats
        file_content = file_content.replace(
            "monitoring/infrastructure-observability.md",
            "infrastructure-security/logging-monitoring.md"
        )
        file_content = file_content.replace(
            "../controls/monitoring/infrastructure-observability.md",
            "../controls/infrastructure-security/logging-monitoring.md"
        )
        file_content = file_content.replace(
            "/docs/controls/monitoring/infrastructure-observability.md",
            "/docs/controls/infrastructure-security/logging-monitoring.md"
        )
        # Also update the title if it appears in links
        file_content = re.sub(
            r'\[Infrastructure Observability\]\([^)]*monitoring/infrastructure-observability\.md\)',
            '[Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md)',
            file_content
        )

        if file_content != original:
            md_file.write_text(file_content, encoding='utf-8')
            reference_count += 1

    print(f"   ✅ Updated {reference_count} files with references")

    # Delete the removed file
    remove_path.unlink()
    print(f"   ✅ Deleted {remove_file}\n")

    print(f"✅ Phase 3 complete!")
    print(f"   - Consolidated logging/monitoring controls")
    print(f"   - Merged unique framework mappings")
    print(f"\n⚠️  Next: Run 'make generate-backlinks' to update all backlink sections")

def main():
    repo_root = Path(__file__).parent.parent.parent
    consolidate_logging_monitoring(repo_root)

if __name__ == '__main__':
    main()
