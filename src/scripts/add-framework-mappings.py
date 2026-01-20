#!/usr/bin/env python3
"""
Add framework mappings to controls based on their content and relationships.
Creates thoughtful cross-references between controls, standards, policies, and processes.
"""

import re
from pathlib import Path

# Mapping of controls to relevant framework areas and other documents
CONTROL_MAPPINGS = {
    # IAM controls
    "iam/identity-authentication.md": {
        "standards": ["standard-saas-iam"],
        "processes": ["access-review"],
        "policies": ["employee", "it-administrator"],
        "description": "Core authentication control referenced by SSO and access management"
    },
    "iam/multi-factor-authentication.md": {
        "standards": ["standard-saas-iam", "standard-aws-security"],
        "processes": ["access-review"],
        "policies": ["employee", "it-administrator"],
        "description": "MFA requirements for all systems"
    },
    "iam/password-management.md": {
        "standards": ["standard-saas-iam"],
        "policies": ["employee"],
        "description": "Password policy and password manager requirements"
    },
    "iam/single-sign-on.md": {
        "standards": ["standard-saas-iam"],
        "processes": ["access-review"],
        "policies": ["it-administrator"],
        "description": "SSO integration requirements"
    },
    "iam/saas-iam.md": {
        "standards": ["standard-saas-iam"],
        "processes": ["access-review"],
        "policies": ["it-administrator"],
        "description": "SaaS application access management"
    },
    "iam/cloud-iam.md": {
        "standards": ["standard-aws-security"],
        "processes": ["access-review"],
        "policies": ["engineer", "it-administrator"],
        "description": "AWS IAM and cloud access management"
    },
    "iam/secrets-management.md": {
        "standards": ["standard-aws-security", "standard-github-security"],
        "policies": ["engineer"],
        "description": "Secrets and credentials management"
    },
    "iam/privileged-access-management.md": {
        "standards": ["standard-aws-security"],
        "processes": ["access-review"],
        "policies": ["it-administrator", "security-team"],
        "description": "Privileged and admin access controls"
    },
    "iam/access-reviews.md": {
        "processes": ["access-review"],
        "policies": ["it-administrator", "hr-administrator"],
        "description": "Periodic access review process"
    },
    "iam/least-privilege-rbac.md": {
        "standards": ["standard-saas-iam", "standard-aws-security"],
        "processes": ["access-review"],
        "policies": ["it-administrator"],
        "description": "Least privilege and role-based access"
    },

    # Cryptography controls
    "cryptography/encryption-at-rest.md": {
        "standards": ["standard-cryptography", "standard-aws-security", "standard-data-classification"],
        "policies": ["engineer"],
        "description": "Encryption requirements for stored data"
    },
    "cryptography/encryption-in-transit.md": {
        "standards": ["standard-cryptography"],
        "policies": ["engineer"],
        "description": "TLS and encryption for data in transit"
    },
    "cryptography/key-management.md": {
        "standards": ["standard-cryptography", "standard-aws-security"],
        "policies": ["engineer", "security-team"],
        "description": "Cryptographic key lifecycle management"
    },
    "cryptography/code-signing.md": {
        "standards": ["standard-github-security"],
        "policies": ["engineer"],
        "description": "Code and artifact signing requirements"
    },

    # Data Management controls
    "data-management/data-classification.md": {
        "standards": ["standard-data-classification"],
        "policies": ["employee"],
        "charter": ["risk-management"],
        "description": "Data classification framework"
    },
    "data-management/data-retention-deletion.md": {
        "standards": ["standard-data-retention"],
        "processes": ["personal-data-request"],
        "policies": ["employee"],
        "description": "Data retention and deletion policies"
    },
    "data-management/data-retention-and-deletion.md": {
        "standards": ["standard-data-retention"],
        "processes": ["personal-data-request"],
        "policies": ["employee"],
        "description": "Data retention and deletion policies"
    },
    "data-management/encryption.md": {
        "standards": ["standard-cryptography", "standard-data-classification"],
        "policies": ["engineer"],
        "description": "Data encryption requirements"
    },
    "data-management/cloud-data-inventory.md": {
        "standards": ["standard-aws-security", "standard-data-classification"],
        "policies": ["engineer", "it-administrator"],
        "description": "Cloud data inventory and classification"
    },
    "data-management/saas-data-inventory.md": {
        "standards": ["standard-saas-iam", "standard-data-classification"],
        "policies": ["it-administrator"],
        "description": "SaaS application data inventory"
    },

    # Data Privacy controls
    "data-privacy/customer-personal-data.md": {
        "standards": ["standard-data-classification", "standard-data-retention"],
        "processes": ["personal-data-request", "data-breach-response"],
        "policies": ["employee"],
        "charter": ["risk-management"],
        "description": "Customer personal data protection (GDPR/CCPA)"
    },
    "data-privacy/employee-personal-data.md": {
        "standards": ["standard-data-retention"],
        "processes": ["personal-data-request"],
        "policies": ["hr-administrator"],
        "description": "Employee personal data protection"
    },
    "data-privacy/data-privacy-gdpr-compliance.md": {
        "standards": ["standard-data-classification", "standard-data-retention"],
        "processes": ["personal-data-request", "data-breach-response"],
        "policies": ["employee"],
        "description": "GDPR compliance requirements"
    },

    # Incident Response controls
    "incident-response/security-incident-response.md": {
        "standards": ["standard-incident-response", "standard-logging-monitoring"],
        "processes": ["security-incident-response", "security-alert-triage"],
        "policies": ["employee", "security-team"],
        "description": "Security incident response procedures"
    },
    "incident-response/data-breach-response.md": {
        "standards": ["standard-incident-response"],
        "processes": ["data-breach-response", "security-incident-response"],
        "policies": ["security-team"],
        "charter": ["risk-management"],
        "description": "Data breach notification and response"
    },
    "incident-response/incident-response-exercises.md": {
        "processes": ["security-tabletop-exercises"],
        "policies": ["security-team"],
        "description": "Incident response training and exercises"
    },

    # Infrastructure Security controls
    "infrastructure-security/cloud-security-configuration-aws.md": {
        "standards": ["standard-aws-security"],
        "policies": ["engineer", "it-administrator"],
        "description": "AWS security configuration requirements"
    },
    "infrastructure-security/network-security.md": {
        "standards": ["standard-aws-security"],
        "policies": ["engineer", "it-administrator"],
        "description": "Network security controls"
    },
    "infrastructure-security/logging-monitoring.md": {
        "standards": ["standard-logging-monitoring", "standard-aws-security"],
        "processes": ["security-alert-triage"],
        "policies": ["engineer", "security-team"],
        "description": "Logging and monitoring requirements"
    },
    "infrastructure-security/backup-recovery.md": {
        "standards": ["standard-aws-security"],
        "policies": ["it-administrator"],
        "description": "Backup and disaster recovery"
    },

    # Endpoint Security controls
    "endpoint-security/device-management-macos-mdm.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator", "employee"],
        "description": "macOS device management via MDM"
    },
    "endpoint-security/endpoint-protection.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint security and EDR"
    },
    "endpoint-security/software-updates.md": {
        "standards": ["standard-endpoint-security"],
        "processes": ["vulnerability-management-process"],
        "policies": ["it-administrator", "employee"],
        "description": "Software update and patch management"
    },
    "endpoint-security/endpoint-hardening.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint hardening configuration"
    },
    "endpoint-security/endpoint-network-security.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint network security controls"
    },

    # Personnel Security controls
    "personnel-security/background-checks.md": {
        "policies": ["hr-administrator"],
        "description": "Background check requirements"
    },
    "personnel-security/security-training.md": {
        "processes": ["security-awareness-training"],
        "policies": ["hr-administrator", "security-team"],
        "description": "Security awareness training program"
    },
    "personnel-security/offboarding.md": {
        "policies": ["hr-administrator", "it-administrator"],
        "processes": ["access-review"],
        "description": "Employee offboarding procedures"
    },
    "personnel-security/personnel-lifecycle-management.md": {
        "policies": ["hr-administrator", "it-administrator"],
        "processes": ["access-review"],
        "description": "Employee lifecycle access management"
    },
    "personnel-security/insider-threat-mitigation.md": {
        "standards": ["standard-logging-monitoring"],
        "policies": ["security-team", "hr-administrator"],
        "description": "Insider threat detection and mitigation"
    },
    "personnel-security/rules-of-behavior.md": {
        "policies": ["employee"],
        "description": "Acceptable use and security policies"
    },

    # Operational Security controls
    "operational-security/change-management.md": {
        "processes": ["grc-change"],
        "policies": ["engineer"],
        "description": "Change management procedures"
    },
    "operational-security/vulnerability-management.md": {
        "standards": ["standard-vulnerability-management"],
        "processes": ["vulnerability-management-process"],
        "policies": ["engineer", "security-team"],
        "description": "Vulnerability management process"
    },
    "operational-security/incident-response.md": {
        "standards": ["standard-incident-response"],
        "processes": ["security-incident-response", "data-breach-response"],
        "policies": ["security-team"],
        "description": "Incident response procedures"
    },
    "operational-security/business-continuity.md": {
        "charter": ["risk-management"],
        "policies": ["it-administrator"],
        "description": "Business continuity planning"
    },

    # Governance controls
    "governance/security-policies.md": {
        "charter": ["governance"],
        "policies": ["security-team"],
        "description": "Security policy governance"
    },
    "governance/risk-assessment.md": {
        "charter": ["risk-management"],
        "processes": ["organizational-risk-assessment"],
        "policies": ["security-team"],
        "description": "Organizational risk assessment"
    },

    # Vendor Management controls
    "vendor-management/third-party-risk-assessment.md": {
        "processes": ["vendor-risk-review"],
        "policies": ["security-team"],
        "charter": ["risk-management"],
        "description": "Third-party vendor risk assessment"
    },
    "vendor-management/vendor-contracts-dpas.md": {
        "processes": ["vendor-risk-review"],
        "policies": ["security-team"],
        "description": "Vendor contracts and data processing agreements"
    },

    # Vulnerability Management controls
    "vulnerability-management/vulnerability-management-process.md": {
        "standards": ["standard-vulnerability-management"],
        "processes": ["vulnerability-management-process"],
        "policies": ["engineer", "security-team"],
        "description": "Vulnerability remediation process"
    },
    "vulnerability-management/cloud-vulnerability-detection.md": {
        "standards": ["standard-aws-security", "standard-vulnerability-management"],
        "processes": ["vulnerability-management-process"],
        "policies": ["engineer"],
        "description": "Cloud infrastructure vulnerability scanning"
    },
    "vulnerability-management/endpoint-vulnerability-detection.md": {
        "standards": ["standard-endpoint-security", "standard-vulnerability-management"],
        "processes": ["vulnerability-management-process"],
        "policies": ["it-administrator"],
        "description": "Endpoint vulnerability detection"
    },

    # Security Engineering controls
    "security-engineering/automated-code-analysis.md": {
        "standards": ["standard-github-security"],
        "policies": ["engineer"],
        "description": "SAST and dependency scanning"
    },
    "security-engineering/secure-code-review.md": {
        "standards": ["standard-github-security"],
        "processes": ["security-code-review"],
        "policies": ["engineer"],
        "description": "Security-focused code review"
    },
    "security-engineering/secure-coding-standards.md": {
        "standards": ["standard-github-security"],
        "policies": ["engineer"],
        "description": "Secure coding practices"
    },

    # Security Assurance controls
    "security-assurance/penetration-tests.md": {
        "processes": ["penetration-testing"],
        "policies": ["security-team"],
        "charter": ["risk-management"],
        "description": "Annual penetration testing"
    },
    "security-assurance/security-reviews.md": {
        "processes": ["security-design-review"],
        "policies": ["engineer", "security-team"],
        "description": "Security design reviews"
    },
    "security-assurance/bug-bounty-program.md": {
        "policies": ["security-team"],
        "description": "Bug bounty program management"
    },
    "security-assurance/customer-security-communications.md": {
        "policies": ["security-team"],
        "description": "Customer security communications"
    },

    # Compliance controls
    "compliance/external-audits.md": {
        "processes": ["external-audit"],
        "policies": ["security-team"],
        "charter": ["governance"],
        "description": "External audit coordination"
    },
    "compliance/internal-audits.md": {
        "processes": ["internal-audit"],
        "policies": ["security-team"],
        "charter": ["governance"],
        "description": "Internal audit procedures"
    },
    "compliance/documentation-review.md": {
        "processes": ["grc-change"],
        "policies": ["security-team"],
        "charter": ["governance"],
        "description": "Policy and documentation reviews"
    },
    "compliance/grc-function.md": {
        "charter": ["governance"],
        "policies": ["security-team"],
        "description": "GRC function responsibilities"
    },
    "compliance/contract-management.md": {
        "processes": ["vendor-risk-review"],
        "policies": ["security-team"],
        "description": "Security contract requirements"
    },

    # Monitoring controls
    "monitoring/siem.md": {
        "standards": ["standard-logging-monitoring"],
        "processes": ["security-alert-triage"],
        "policies": ["security-team"],
        "description": "SIEM and log analysis"
    },
    "monitoring/infrastructure-observability.md": {
        "standards": ["standard-logging-monitoring", "standard-aws-security"],
        "policies": ["engineer", "security-team"],
        "description": "Infrastructure monitoring"
    },
    "monitoring/endpoint-observability.md": {
        "standards": ["standard-logging-monitoring", "standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint monitoring and EDR"
    },

    # Threat Detection controls
    "threat-detection/cloud-threat-detection.md": {
        "standards": ["standard-aws-security", "standard-logging-monitoring"],
        "processes": ["security-alert-triage"],
        "policies": ["security-team"],
        "description": "AWS GuardDuty threat detection"
    },
    "threat-detection/endpoint-threat-detection.md": {
        "standards": ["standard-endpoint-security"],
        "processes": ["security-alert-triage"],
        "policies": ["security-team"],
        "description": "Endpoint threat detection (EDR)"
    },
    "threat-detection/saas-threat-detection.md": {
        "standards": ["standard-saas-iam"],
        "processes": ["security-alert-triage"],
        "policies": ["security-team"],
        "description": "CASB and SaaS threat detection"
    },

    # Configuration Management controls
    "configuration-management/cloud-hardening.md": {
        "standards": ["standard-aws-security"],
        "policies": ["engineer", "it-administrator"],
        "description": "Cloud infrastructure hardening"
    },
    "configuration-management/endpoint-hardening.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint hardening configuration"
    },
    "configuration-management/saas-hardening.md": {
        "standards": ["standard-saas-iam"],
        "policies": ["it-administrator"],
        "description": "SaaS application hardening"
    },

    # Security Training controls
    "security-training/security-awareness-training.md": {
        "processes": ["security-awareness-training"],
        "policies": ["hr-administrator", "security-team"],
        "description": "Annual security awareness training"
    },
    "security-training/secure-coding-training.md": {
        "policies": ["engineer", "security-team"],
        "description": "Secure coding training for developers"
    },
    "security-training/incident-response-training.md": {
        "processes": ["security-tabletop-exercises"],
        "policies": ["security-team"],
        "description": "Incident response team training"
    },

    # Asset Management controls
    "asset-management/cloud-inventory.md": {
        "standards": ["standard-aws-security"],
        "policies": ["it-administrator", "engineer"],
        "description": "Cloud resource inventory"
    },
    "asset-management/endpoint-inventory.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint device inventory"
    },
    "asset-management/saas-inventory.md": {
        "standards": ["standard-saas-iam"],
        "policies": ["it-administrator"],
        "description": "SaaS application inventory"
    },

    # Availability controls
    "availability/availability-monitoring.md": {
        "standards": ["standard-logging-monitoring"],
        "policies": ["engineer"],
        "description": "Uptime and availability monitoring"
    },
    "availability/capacity-planning.md": {
        "policies": ["engineer", "it-administrator"],
        "charter": ["risk-management"],
        "description": "Capacity planning and scaling"
    },
    "availability/disaster-recovery.md": {
        "charter": ["risk-management"],
        "policies": ["it-administrator"],
        "description": "Disaster recovery planning"
    },

    # Network Security controls
    "network-security/cloud-network-security.md": {
        "standards": ["standard-aws-security"],
        "policies": ["engineer", "it-administrator"],
        "description": "Cloud network segmentation and security groups"
    },
    "network-security/endpoint-network-security.md": {
        "standards": ["standard-endpoint-security"],
        "policies": ["it-administrator"],
        "description": "Endpoint firewall and VPN"
    },

    # Physical Protection controls
    "physical-protection/office-security.md": {
        "policies": ["it-administrator", "employee"],
        "description": "Office physical security"
    },

    # Risk Management controls
    "risk-management/organizational-risk-assessment.md": {
        "charter": ["risk-management"],
        "processes": ["organizational-risk-assessment"],
        "policies": ["security-team"],
        "description": "Annual risk assessment process"
    },
    "risk-management/vendor-risk-management.md": {
        "charter": ["risk-management"],
        "processes": ["vendor-risk-review"],
        "policies": ["security-team"],
        "description": "Vendor security assessments"
    },

    # Change Management controls
    "change-management/change-management.md": {
        "processes": ["grc-change"],
        "policies": ["engineer", "security-team"],
        "description": "Change management process"
    },
}

def add_framework_mappings(control_path, mappings):
    """Add framework mappings to a control file."""
    file_path = Path("docs/controls") / control_path

    if not file_path.exists():
        return False

    content = file_path.read_text()

    # Find the Framework Mapping section
    pattern = r'(## Framework Mapping\n\n)(<!-- .*? -->)'

    def replace_mapping(match):
        header = match.group(1)

        mapping_lines = []

        # Add standards
        if "standards" in mappings:
            mapping_lines.append("### Standards")
            mapping_lines.append("")
            for standard_id in mappings["standards"]:
                # Convert ID to title
                title = standard_id.replace("standard-", "").replace("-", " ").title()
                standard_file = f"{standard_id.replace('standard-', '')}-standard.md"
                mapping_lines.append(f"- [{title}](../standards/{standard_file})")
            mapping_lines.append("")

        # Add processes
        if "processes" in mappings:
            mapping_lines.append("### Processes")
            mapping_lines.append("")
            for process in mappings["processes"]:
                title = process.replace("-", " ").title()
                mapping_lines.append(f"- [{title}](../processes/{process}.md)")
            mapping_lines.append("")

        # Add policies
        if "policies" in mappings:
            mapping_lines.append("### Policies")
            mapping_lines.append("")
            for policy in mappings["policies"]:
                title = policy.replace("-", " ").title()
                mapping_lines.append(f"- [{title}](../policies/{policy}.md)")
            mapping_lines.append("")

        # Add charter
        if "charter" in mappings:
            mapping_lines.append("### Charter")
            mapping_lines.append("")
            for charter_doc in mappings["charter"]:
                title = charter_doc.replace("-", " ").title()
                mapping_lines.append(f"- [{title}](../charter/{charter_doc}.md)")
            mapping_lines.append("")

        return header + "\n".join(mapping_lines)

    new_content = re.sub(pattern, replace_mapping, content, flags=re.DOTALL)

    if new_content != content:
        file_path.write_text(new_content)
        return True

    return False

def main():
    print("Adding framework mappings to controls...\n")

    updated = []
    skipped = []

    for control_path, mappings in CONTROL_MAPPINGS.items():
        if add_framework_mappings(control_path, mappings):
            print(f"✓ {control_path}")
            updated.append(control_path)
        else:
            print(f"⏭️  {control_path} (not found or no change)")
            skipped.append(control_path)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Updated: {len(updated)} controls")
    print(f"Skipped: {len(skipped)} controls")

if __name__ == '__main__':
    main()
