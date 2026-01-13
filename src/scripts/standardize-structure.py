#!/usr/bin/env python3
"""Standardize all document structures and fill in control mappings."""

import os
import glob
import re

def standardize_custom_controls():
    """Ensure all custom controls have consistent structure with Framework Mapping."""
    for filepath in glob.glob("custom/*.md"):
        if filepath.endswith("/index.md"):
            continue

        with open(filepath, 'r') as f:
            content = f.read()

        # Replace "## Satisfies Framework Controls" with "## Framework Mapping"
        content = content.replace("## Satisfies Framework Controls", "## Framework Mapping")

        # Ensure Framework Mapping section exists and has proper comment
        if "## Framework Mapping" not in content:
            # Add it before Referenced By
            ref_by_pos = content.find("## Referenced By")
            if ref_by_pos > 0:
                insert_pos = content.rfind("---", 0, ref_by_pos)
                if insert_pos > 0:
                    new_section = "\n## Framework Mapping\n\n<!-- This section is used to generate backlinks from framework controls to this custom control. Do not remove. -->\n\n---\n\n"
                    content = content[:insert_pos] + new_section + content[insert_pos+4:]

        # Fix **SOC 2:** to ### SOC 2
        content = re.sub(r'\n\*\*SOC 2:\*\*\n', r'\n### SOC 2\n', content)
        content = re.sub(r'\n\*\*GDPR:\*\*\n', r'\n### GDPR\n', content)
        content = re.sub(r'\n\*\*ISO 27001:\*\*\n', r'\n### ISO 27001\n', content)
        content = re.sub(r'\n\*\*NIST 800-53:\*\*\n', r'\n### NIST 800-53\n', content)

        with open(filepath, 'w') as f:
            f.write(content)

    print(f"Standardized {len(glob.glob('custom/*.md'))-1} custom controls")

def standardize_grc_docs():
    """Ensure all standards/processes/policies/charter have Control Mapping section."""
    patterns = ['standards/*.md', 'processes/*.md', 'policies/*.md', 'charter/*.md']

    count = 0
    for pattern in patterns:
        for filepath in glob.glob(pattern):
            if filepath.endswith("/index.md"):
                continue

            with open(filepath, 'r') as f:
                content = f.read()

            # Replace "## Satisfies Controls" with "## Control Mapping"
            content = content.replace("## Satisfies Controls", "## Control Mapping")

            # Ensure Control Mapping section exists
            if "## Control Mapping" not in content:
                # Add it before Referenced By
                ref_by_pos = content.find("## Referenced By")
                if ref_by_pos > 0:
                    insert_pos = content.rfind("---", 0, ref_by_pos)
                    if insert_pos > 0:
                        new_section = "\n## Control Mapping\n\n<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->\n<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->\n\n---\n\n"
                        content = content[:insert_pos] + new_section + content[insert_pos+4:]

            with open(filepath, 'w') as f:
                f.write(content)
            count += 1

    print(f"Standardized {count} GRC documents")

if __name__ == '__main__':
    print("Standardizing document structures...")
    standardize_custom_controls()
    standardize_grc_docs()
    print("Done!")
