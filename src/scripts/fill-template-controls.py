#!/usr/bin/env python3
"""
Fill out template controls with realistic content based on control family and title.
Uses patterns from filled-out controls and industry best practices.
"""

import re
from pathlib import Path

# Control content templates organized by family
CONTROL_CONTENT = {
    "asset-management": {
        "cloud-inventory": {
            "objective": "Maintain accurate, real-time inventory of all cloud resources to enable security monitoring, cost optimization, and compliance tracking.",
            "implementation": "**AWS Resource Tagging**: All resources tagged with: Owner, Environment (prod/staging/dev), DataClassification, CostCenter. **Automated Discovery**: AWS Config continuously discovers and records all resources. **Inventory Dashboard**: Cloud asset management tool (e.g., AWS Systems Manager Inventory, CloudQuery) aggregates resources across accounts. **Drift Detection**: Daily scans identify untagged or non-compliant resources. **Quarterly Reviews**: Asset owners verify inventory accuracy.",
            "evidence": "- AWS Config resource inventory reports\n- Cloud asset management dashboard exports\n- Resource tagging compliance reports\n- Quarterly inventory review sign-offs\n- Untagged resource remediation tickets"
        },
        "endpoint-inventory": {
            "objective": "Maintain complete inventory of all endpoint devices (laptops, desktops, mobile devices) to ensure security controls are applied and track device lifecycle.",
            "implementation": "**MDM Enrollment**: All company devices enrolled in MDM (Jamf for macOS, Intune for Windows). **Automated Discovery**: MDM automatically discovers enrolled devices. **Inventory Tracking**: Device attributes recorded: Serial number, OS version, last check-in, assigned user, enrollment date. **BYOD Policy**: Personal devices accessing company resources must enroll or use virtual desktop. **Decommissioning**: Devices removed from inventory upon employee offboarding or hardware refresh.",
            "evidence": "- MDM device inventory reports\n- Device enrollment logs\n- Hardware asset register\n- Device assignment records\n- Decommissioning documentation"
        },
        "saas-inventory": {
            "objective": "Maintain comprehensive inventory of all SaaS applications to manage access, monitor security posture, and prevent shadow IT.",
            "implementation": "**Procurement Approval**: All SaaS purchases require IT and Security approval. **SSO Integration**: Production SaaS tools integrated with SSO for visibility. **CASB Monitoring**: Cloud Access Security Broker (e.g., Netskope) discovers SaaS usage via network traffic analysis. **Quarterly Reviews**: IT reviews SaaS inventory, identifies shadow IT, and assesses security posture. **Vendor Risk**: Critical SaaS apps undergo vendor risk assessment.",
            "evidence": "- SaaS application inventory (IT procurement system)\n- SSO integration list\n- CASB shadow IT reports\n- Quarterly SaaS review documentation\n- Vendor risk assessment records"
        }
    },
    "availability": {
        "availability-monitoring": {
            "objective": "Continuously monitor system availability and performance to detect and respond to outages or degradations before customer impact.",
            "implementation": "**Uptime Monitoring**: External monitoring service (e.g., Pingdom, StatusCake) checks production endpoints every 1 minute from multiple geographic locations. **Application Monitoring**: APM tool (e.g., New Relic, Datadog) tracks application performance, error rates, and latency. **Infrastructure Monitoring**: CloudWatch monitors EC2, RDS, ELB health metrics with alerting on anomalies. **On-Call Rotation**: 24/7 on-call engineer receives alerts via PagerDuty. **Status Page**: Public status page (e.g., status.io) communicates availability to customers.",
            "evidence": "- Uptime monitoring reports (99.9% target)\n- Application performance dashboards\n- CloudWatch alarm history\n- PagerDuty incident logs\n- Status page incident timeline"
        },
        "capacity-planning": {
            "objective": "Proactively plan and provision capacity to maintain performance and availability as usage grows, preventing resource exhaustion.",
            "implementation": "**Usage Metrics**: Track CPU, memory, storage, network utilization across all production systems. **Growth Trends**: Quarterly analysis of growth rates (users, transactions, data volume). **Capacity Thresholds**: Alert when utilization exceeds 80% to trigger provisioning. **Auto-Scaling**: AWS Auto Scaling groups automatically add capacity during traffic spikes. **Annual Planning**: Engineering reviews capacity needs for next 12 months, budgets for infrastructure expansion.",
            "evidence": "- CloudWatch capacity utilization reports\n- Quarterly capacity trend analysis\n- Auto-scaling event logs\n- Annual capacity planning documents\n- Infrastructure budget approvals"
        },
        "disaster-recovery": {
            "objective": "Ensure business continuity by maintaining tested disaster recovery capabilities with defined Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO).",
            "implementation": "**RTO/RPO Targets**: Production systems: RTO 4 hours, RPO 1 hour. **Multi-Region Architecture**: Primary region us-east-1, DR region us-west-2. **Data Replication**: RDS cross-region replicas, S3 cross-region replication enabled for critical buckets. **DR Runbooks**: Documented procedures for failover to DR region. **Annual DR Test**: Full failover test conducted annually, results documented, gaps remediated. **Backup Validation**: Monthly restore tests verify backup integrity.",
            "evidence": "- DR plan document with RTO/RPO targets\n- Cross-region replication configuration\n- DR runbooks\n- Annual DR test reports\n- Monthly backup restore test logs"
        }
    },
    "compliance": {
        "contract-management": {
            "objective": "Ensure all vendor contracts include appropriate security, privacy, and compliance requirements to protect organizational and customer data.",
            "implementation": "**Contract Templates**: Legal maintains standard templates with required security clauses (confidentiality, data protection, audit rights, incident notification). **Security Review**: Security team reviews contracts for SaaS vendors handling Confidential or Restricted data. **DPAs Required**: Data Processing Agreements mandatory for vendors processing customer personal data. **SOC 2 Attestation**: Vendors processing Confidential data must provide SOC 2 Type II report. **Contract Repository**: All signed contracts stored in CLM system with renewal date tracking.",
            "evidence": "- Contract templates with security clauses\n- Security contract review records\n- Signed DPAs with vendors\n- Vendor SOC 2 reports\n- Contract management system records"
        },
        "documentation-review": {
            "objective": "Maintain current, accurate security documentation through regular review cycles to ensure policies and procedures reflect actual practices.",
            "implementation": "**Review Cadence**: Policies (annual), Standards (annual), Processes (annual), Controls (quarterly). **Owner Assignment**: Each document has designated owner responsible for reviews. **Review Process**: Owner reviews content, updates as needed, signs off on completion. **Change Tracking**: Git tracks all documentation changes with commit messages explaining rationale. **Approval Workflow**: Material policy changes require executive sponsor approval.",
            "evidence": "- Document review schedule\n- last_reviewed dates in frontmatter\n- Git commit history for documentation updates\n- Review sign-off records\n- Policy change approval emails"
        },
        "external-audits": {
            "objective": "Demonstrate security program effectiveness through independent third-party audits, providing assurance to customers and stakeholders.",
            "implementation": "**Annual SOC 2 Type II**: CPA firm audits Trust Service Criteria (Security, Availability, Confidentiality) over 12-month period. **Audit Planning**: Scope defined Q4, fieldwork conducted Q1, report delivered by March 31. **Evidence Collection**: Security team maintains evidence repository (access logs, change tickets, training records, vulnerability scans). **Finding Remediation**: All audit exceptions remediated with documented management responses. **Report Distribution**: SOC 2 report available to customers via NDA through security portal.",
            "evidence": "- SOC 2 Type II audit report\n- Audit planning documents\n- Evidence repository\n- Management response letters\n- Customer report distribution log"
        },
        "grc-function": {
            "objective": "Establish dedicated GRC function to manage compliance programs, coordinate audits, and maintain risk register.",
            "implementation": "**GRC Team**: Security team includes GRC function (may be fractional role in small orgs). **Responsibilities**: Coordinate external audits, maintain risk register, track control effectiveness, manage compliance documentation, conduct internal audits. **GRC Tool**: Compliance tracking system (e.g., Vanta, Drata, Sprinto) automates evidence collection and control monitoring. **Quarterly Reporting**: GRC function reports compliance status to Security Committee. **Framework Alignment**: Maps controls to SOC 2, ISO 27001, GDPR requirements.",
            "evidence": "- GRC team org chart and responsibilities\n- GRC tool configuration and reports\n- Quarterly compliance reports to Security Committee\n- Control mapping documentation\n- Risk register"
        },
        "internal-audits": {
            "objective": "Validate security control effectiveness through regular internal testing, identifying gaps before external audits.",
            "implementation": "**Quarterly Testing**: Internal audit of key controls: access reviews, change management, vulnerability patching, training completion, log monitoring. **Test Procedures**: Sample-based testing following external audit methodology. **Documentation**: Test results documented in audit workpapers with screenshots, log exports, signed attestations. **Gap Remediation**: Identified gaps assigned to control owners with due dates. **Pre-Audit Readiness**: Internal audit conducted 1-2 months before external audit to identify and fix issues.",
            "evidence": "- Quarterly internal audit workpapers\n- Control testing results\n- Gap remediation tracking\n- Internal audit reports\n- Pre-audit readiness assessments"
        }
    },
    "configuration-management": {
        "cloud-hardening": {
            "objective": "Apply security hardening standards to all cloud infrastructure to reduce attack surface and prevent misconfigurations.",
            "implementation": "**CIS Benchmarks**: Apply CIS AWS Foundations Benchmark configurations. **Security Baselines**: AWS Security Hub checks for security best practices (S3 public access blocked, EBS encryption enabled, unused credentials removed). **Infrastructure-as-Code**: Terraform templates include security configurations by default (encrypted storage, private subnets, security group restrictions). **Continuous Compliance**: AWS Config rules monitor for configuration drift, auto-remediate or alert. **Quarterly Reviews**: Review and update hardening standards based on new threats and AWS features.",
            "evidence": "- CIS Benchmark compliance reports\n- AWS Security Hub findings\n- Terraform security configurations\n- AWS Config compliance dashboard\n- Hardening standard review records"
        },
        "endpoint-hardening": {
            "objective": "Apply security hardening configurations to all endpoint devices to prevent compromise and limit lateral movement.",
            "implementation": "**OS Hardening**: CIS Benchmarks applied via MDM configuration profiles. **Disk Encryption**: FileVault (macOS) or BitLocker (Windows) enforced, keys escrowed to MDM. **Firewall**: Host firewall enabled, only required ports open. **Screen Lock**: Auto-lock after 5 minutes, password required to unlock. **Removable Media**: USB storage disabled except for approved devices. **Local Admin**: Removed for standard users, emergency admin access via MDM. **Compliance Monitoring**: MDM reports non-compliant devices daily.",
            "evidence": "- MDM configuration profiles\n- CIS Benchmark compliance reports\n- Encryption key escrow records\n- Firewall configuration policies\n- Device compliance dashboards"
        },
        "saas-hardening": {
            "objective": "Apply security configurations to SaaS applications to protect against unauthorized access and data leakage.",
            "implementation": "**SSO Enforcement**: All production SaaS apps require SSO login (no local passwords). **MFA Mandatory**: MFA enforced at IdP level for all users. **Session Timeouts**: Sessions expire after 8 hours of inactivity. **IP Restrictions**: Admin access to critical SaaS apps restricted to corporate IPs or VPN. **Data Loss Prevention**: CASB enforces DLP policies (block Confidential data uploads to unapproved apps). **Audit Logging**: Enable maximum audit logging retention in all SaaS apps. **Quarterly Reviews**: Review SaaS security settings, apply new hardening recommendations.",
            "evidence": "- SaaS SSO configuration screenshots\n- IdP MFA enforcement policies\n- Session timeout settings\n- IP allowlist configurations\n- CASB DLP policy settings\n- SaaS audit log retention settings"
        }
    },
    "cryptography": {
        "code-signing": {
            "objective": "Sign all software releases to ensure integrity and authenticity, preventing tampering or malware injection.",
            "implementation": "**Signing Keys**: Code signing certificates stored in secure key management service (AWS KMS, HashiCorp Vault). **Build Pipeline**: CI/CD pipeline automatically signs artifacts during build process. **Certificate Management**: Code signing certificates renewed before expiration, rotated every 2 years. **Verification**: Release process verifies signatures before deployment. **Key Access**: Only automated build systems have signing key access (no developer access).",
            "evidence": "- Code signing certificates\n- CI/CD signing configuration\n- Signed artifact verification logs\n- Certificate renewal records\n- Key access audit logs"
        },
        "encryption-at-rest": {
            "objective": "Encrypt all Confidential and Restricted data at rest to protect against unauthorized access from storage compromise.",
            "implementation": "**Database Encryption**: RDS encryption enabled using AWS KMS customer-managed keys. **S3 Encryption**: SSE-KMS encryption required for all buckets containing Confidential data. **EBS Encryption**: All EBS volumes encrypted by default. **Encryption Standards**: AES-256-GCM encryption algorithm. **Key Rotation**: KMS automatic key rotation enabled (annual). **Backup Encryption**: All backups encrypted using same keys as source data.",
            "evidence": "- RDS encryption settings\n- S3 bucket encryption policies\n- EBS default encryption configuration\n- KMS key rotation logs\n- Encrypted backup verification"
        },
        "encryption-in-transit": {
            "objective": "Encrypt all data in transit using TLS to prevent interception, eavesdropping, and man-in-the-middle attacks.",
            "implementation": "**TLS Requirements**: Minimum TLS 1.2, TLS 1.3 preferred. **Certificate Management**: AWS ACM manages certificates with automatic renewal. **HTTPS Only**: All public endpoints require HTTPS, HTTP redirects to HTTPS. **HSTS**: HTTP Strict Transport Security header enabled (max-age 1 year). **Internal Services**: Service-to-service communication uses TLS with mutual authentication where feasible. **API Security**: APIs enforce HTTPS, reject plain HTTP requests.",
            "evidence": "- ALB/CloudFront TLS configuration (TLS 1.2+ enforced)\n- ACM certificate list and renewal status\n- HSTS header configuration\n- TLS connection logs\n- API gateway HTTPS enforcement settings"
        },
        "key-management": {
            "objective": "Securely generate, store, rotate, and retire cryptographic keys following industry best practices.",
            "implementation": "**Key Storage**: AWS KMS for encryption keys, AWS Secrets Manager for API keys and credentials. **No Hardcoded Keys**: Automated scans (TruffleHog) detect hardcoded secrets in code. **Key Rotation**: KMS automatic rotation enabled annually. API keys rotated every 90 days. **Access Control**: Least privilege access to keys via IAM policies. **Audit Logging**: CloudTrail logs all key usage. **Key Lifecycle**: Retired keys maintained for decrypt-only access to historical data.",
            "evidence": "- AWS KMS key configuration\n- Secrets Manager inventory\n- Secret scanning tool reports\n- Key rotation logs\n- CloudTrail key usage logs"
        }
    },
    "data-management": {
        "cloud-data-inventory": {
            "objective": "Maintain comprehensive inventory of data stored in cloud services, classified by sensitivity, to enable proper protection and compliance.",
            "implementation": "**Data Discovery**: Automated tools (AWS Macie, data classification scanners) identify and classify data in S3, RDS, and other cloud storage. **Data Tagging**: S3 buckets and RDS databases tagged with DataClassification (Public, Internal, Confidential, Restricted). **Data Catalog**: AWS Glue Data Catalog or similar maintains metadata about datasets (location, classification, owner, retention). **Quarterly Reviews**: Data owners review inventory for accuracy, identify orphaned data. **Compliance Mapping**: Inventory indicates which data is subject to GDPR, PCI, HIPAA requirements.",
            "evidence": "- Cloud data inventory reports\n- Data classification scan results\n- S3 bucket and RDS tagging reports\n- Data catalog exports\n- Quarterly data inventory reviews"
        },
        "data-retention-and-deletion": {
            "objective": "Retain data only as long as needed for business and legal requirements, then securely delete to minimize risk and storage costs.",
            "implementation": "**Retention Policies**: Customer data 7 years, employee records 7 years, audit logs 2 years, application logs 1 year, system logs 90 days. **Automated Deletion**: S3 lifecycle policies, RDS automated backups, log retention rules automatically delete data past retention period. **Secure Deletion**: S3 bucket versioning disabled or versioned objects purged, RDS snapshots encrypted then deleted. **Legal Hold**: Litigation or investigation triggers legal hold preventing deletion. **Customer Deletion Requests**: GDPR Right to Erasure implemented within 30 days.",
            "evidence": "- Data retention policy document\n- S3 lifecycle policy configurations\n- RDS backup retention settings\n- Log retention configurations\n- Customer deletion request logs"
        },
        "saas-data-inventory": {
            "objective": "Maintain inventory of data stored in SaaS applications to understand data location, classification, and compliance obligations.",
            "implementation": "**SaaS Data Mapping**: Document what data is stored in each SaaS app (Slack, Google Workspace, Salesforce, etc.). **Data Classification**: Classify SaaS data per data classification standard. **Vendor Assessments**: Verify SaaS vendors implement appropriate security controls for data sensitivity. **Data Export**: Quarterly data exports for critical SaaS apps to prevent vendor lock-in. **Compliance Review**: Identify SaaS apps storing data subject to GDPR, CCPA, or other regulations.",
            "evidence": "- SaaS data inventory spreadsheet\n- Data classification per SaaS app\n- Vendor security assessments\n- SaaS data export logs\n- Compliance data mapping"
        }
    },
    "data-privacy": {
        "customer-personal-data": {
            "objective": "Protect customer personal data in compliance with privacy regulations (GDPR, CCPA) through proper handling, consent, and data subject rights.",
            "implementation": "**Data Minimization**: Collect only necessary personal data. **Consent Management**: Capture and document customer consent for data processing. **Data Subject Rights**: Process requests for access, rectification, erasure, portability within regulatory timeframes (30 days GDPR). **DPAs with Vendors**: Data Processing Agreements with all vendors processing customer personal data. **Privacy Notice**: Clear privacy policy on website explaining data collection and use. **Breach Notification**: Report personal data breaches to authorities within 72 hours per GDPR.",
            "evidence": "- Privacy policy\n- Consent management records\n- Data subject request logs and responses\n- DPAs with vendors\n- Privacy impact assessments\n- Breach notification procedures"
        },
        "employee-personal-data": {
            "objective": "Protect employee personal data in compliance with privacy laws and maintain employee trust.",
            "implementation": "**HR System Security**: HRIS (BambooHR, Workday) with role-based access, MFA, audit logging. **Data Minimization**: Collect only employment-related personal data. **Access Restrictions**: HR team and employee's manager only. **Retention**: Terminated employee records retained 7 years per legal requirements, then deleted. **Employee Rights**: Employees can request access to their personal data. **Background Checks**: Consent obtained before background checks, results handled confidentially.",
            "evidence": "- HRIS access control configuration\n- Employee data retention policies\n- Employee data request logs\n- Background check consent forms\n- HR data access audit logs"
        }
    },
    "iam": {
        "cloud-iam": {
            "objective": "Manage cloud infrastructure access using identity-based policies, roles, and least privilege principles.",
            "implementation": "**AWS IAM**: Users access via SSO (AWS IAM Identity Center), no long-lived credentials. **Role-Based Access**: Engineers get read-only by default, elevated access requires approval and time-bound sessions. **Service Accounts**: EC2 instances use IAM roles, Lambda functions use execution roles (no embedded credentials). **MFA Required**: MFA enforced for console access. **Permission Boundaries**: Limit maximum permissions for delegated admin. **Quarterly Reviews**: Review IAM users, roles, policies for least privilege.",
            "evidence": "- AWS IAM SSO configuration\n- IAM role definitions and policies\n- IAM credential report (no unused credentials)\n- MFA enforcement settings\n- Quarterly IAM access reviews"
        },
        "multi-factor-authentication": {
            "objective": "Require multiple authentication factors to protect against credential theft and phishing attacks.",
            "implementation": "**MFA Mandatory**: Enforced for all users accessing production systems via SSO (Okta, Google Workspace). **WebAuthn Preferred**: Hardware security keys (YubiKey) or platform authenticators (Touch ID) preferred over TOTP. **Phishing-Resistant**: WebAuthn/FIDO2 prevents phishing, SMS-based MFA prohibited. **Recovery**: Backup authentication methods registered (multiple security keys). **Compliance**: MFA status monitored, users without MFA blocked after 7 days. **Admin Access**: Admin/privileged accounts require phishing-resistant MFA.",
            "evidence": "- IdP MFA enforcement policies\n- User MFA enrollment reports (100% target)\n- WebAuthn/hardware key inventory\n- MFA authentication logs\n- Admin account MFA requirements"
        },
        "password-management": {
            "objective": "Ensure strong, unique passwords for all accounts through password manager adoption and password policy enforcement.",
            "implementation": "**Password Manager Required**: All employees issued 1Password for business, usage monitored. **SSO Preferred**: Reduce passwords by SSO integration for SaaS apps. **Password Policy**: Minimum 12 characters for accounts not using SSO, complexity requirements enforced. **No Reuse**: Password manager prevents reuse across services. **Credential Scanning**: Monitor for compromised passwords in breaches (1Password Watchtower, Have I Been Pwned). **Rotation**: Passwords changed immediately if compromised, otherwise no forced rotation (per NIST guidance).",
            "evidence": "- 1Password for Business deployment\n- Password policy configuration\n- SSO integration list\n- Compromised credential alerts\n- Password manager adoption reports"
        },
        "saas-iam": {
            "objective": "Centralize SaaS application access through SSO with automated provisioning and deprovisioning.",
            "implementation": "**SSO Integration**: All production SaaS apps integrated with SSO (Okta, Google Workspace). **SCIM Provisioning**: Automated user provisioning and deprovisioning via SCIM protocol. **MFA at IdP**: MFA enforced centrally at IdP, not per-app. **Role Mapping**: IdP groups map to SaaS app roles (e.g., Okta Engineering group → GitHub Engineers team). **Access Requests**: ServiceNow or similar for SaaS access requests, manager approval required. **Quarterly Reviews**: Review SaaS access, remove unused accounts.",
            "evidence": "- SSO integration configuration per SaaS app\n- SCIM provisioning logs\n- IdP group to SaaS role mappings\n- Access request records\n- Quarterly SaaS access reviews"
        },
        "secrets-management": {
            "objective": "Securely store and manage application secrets (API keys, database passwords) to prevent exposure and unauthorized access.",
            "implementation": "**Secrets Manager**: AWS Secrets Manager or HashiCorp Vault stores all application secrets. **No Hardcoded Secrets**: Automated scanning (TruffleHog, GitGuardian) detects hardcoded secrets in code, blocks commits. **Dynamic Secrets**: Database credentials rotated automatically by Secrets Manager. **Least Privilege**: Applications granted access only to required secrets via IAM policies. **Audit Logging**: All secret access logged via CloudTrail. **Rotation**: API keys rotated every 90 days, database passwords rotated every 30 days automatically.",
            "evidence": "- Secrets Manager inventory\n- Secret scanning tool configuration and alerts\n- Secret rotation logs\n- IAM policies for secret access\n- CloudTrail secret access logs"
        },
        "single-sign-on": {
            "objective": "Centralize authentication through SSO to reduce password sprawl, improve security, and enable centralized access control.",
            "implementation": "**SSO Provider**: Okta or Google Workspace as IdP. **SAML/OIDC**: SaaS apps integrated via SAML 2.0 or OpenID Connect. **Directory Sync**: IdP synced with HR system (BambooHR) for automated user lifecycle. **MFA Enforced**: MFA required at IdP level for all users. **Session Management**: Idle timeout 8 hours, users re-authenticate daily. **Cloud Access**: AWS, GCP access via SSO (no local cloud accounts). **Quarterly Reviews**: Review SSO integrations, add new SaaS apps to SSO.",
            "evidence": "- SSO provider configuration\n- SAML/OIDC integration list\n- HR system directory sync logs\n- MFA enforcement policies\n- SSO authentication logs"
        }
    },
    "incident-response": {
        "data-breach-response": {
            "objective": "Respond to data breaches affecting personal data in compliance with breach notification laws (GDPR, state laws).",
            "implementation": "**Breach Definition**: Unauthorized access, disclosure, or loss of personal data. **Incident Classification**: Security incidents assessed for personal data impact. **Notification Timing**: GDPR requires notification to supervisory authority within 72 hours if high risk to individuals. **Affected Individuals**: Notify individuals without undue delay if high risk. **Documentation**: Breach register documents: date, scope, cause, impact, remediation, notifications sent. **Legal Review**: Legal counsel reviews breach notification requirements. **Annual Tabletop**: Conduct data breach response tabletop exercise annually.",
            "evidence": "- Data breach response plan\n- Breach notification templates\n- Breach register\n- Regulatory breach notifications sent\n- Tabletop exercise documentation"
        },
        "incident-response-exercises": {
            "objective": "Test and improve incident response capabilities through regular tabletop exercises and simulations.",
            "implementation": "**Quarterly Tabletops**: Tabletop exercises with incident response team covering various scenarios (ransomware, data breach, DDoS, insider threat). **Scenario Design**: Realistic scenarios based on current threats and organizational risks. **Participants**: Security team, engineering on-call, IT ops, legal, PR/communications, executives. **Exercise Objectives**: Test communication, decision-making, playbook procedures. **Lessons Learned**: Document gaps, update runbooks, assign remediation tasks. **Annual Full Simulation**: Full incident response simulation with live system interaction.",
            "evidence": "- Quarterly tabletop exercise agendas and attendees\n- Exercise scenario documents\n- Lessons learned and action items\n- Updated incident response runbooks\n- Annual simulation reports"
        },
        "security-incident-response": {
            "objective": "Detect, contain, investigate, and recover from security incidents to minimize impact and prevent recurrence.",
            "implementation": "**24/7 Monitoring**: SIEM and security alerts monitored continuously. **On-Call Rotation**: Security engineer on-call 24/7 via PagerDuty. **Severity Levels**: P0 (Critical - data breach, ransomware), P1 (High - system compromise), P2 (Medium - unsuccessful attack), P3 (Low - policy violation). **Response Steps**: Detect → Triage → Contain → Investigate → Remediate → Document → Post-Mortem. **Communication**: Security lead coordinates with engineering, legal, PR. **Documentation**: All incidents documented in ticketing system with timeline, actions, root cause, remediation.",
            "evidence": "- Incident response plan and runbooks\n- On-call schedule\n- Security incident tickets\n- Incident response metrics (MTTI, MTTC)\n- Post-mortem reports"
        }
    },
    "monitoring": {
        "endpoint-observability": {
            "objective": "Monitor endpoint health, security posture, and user activity to detect threats and ensure compliance.",
            "implementation": "**EDR Telemetry**: Endpoint Detection and Response (CrowdStrike, SentinelOne) collects process execution, network connections, file changes. **MDM Monitoring**: MDM reports device compliance (encryption enabled, OS updated, firewall on). **Centralized Logging**: EDR and MDM logs forwarded to SIEM. **Alerting**: EDR alerts on suspicious activity (malware, lateral movement, privilege escalation). **Dashboards**: Security team monitors endpoint health dashboard daily. **Response**: Security team investigates EDR alerts within SLA (Critical: 1 hour, High: 4 hours).",
            "evidence": "- EDR deployment status (100% coverage)\n- MDM compliance dashboards\n- SIEM endpoint log integration\n- EDR alert history\n- Incident response tickets from endpoint alerts"
        },
        "infrastructure-observability": {
            "objective": "Monitor cloud infrastructure for security events, performance issues, and compliance drift.",
            "implementation": "**CloudWatch**: Monitors EC2, RDS, Lambda, ELB metrics and logs. **CloudTrail**: Logs all AWS API calls for audit and investigation. **Security Hub**: Aggregates findings from GuardDuty, Inspector, Config. **Alerting**: CloudWatch alarms for critical events (root login, IAM policy changes, failed authentications, resource exhaustion). **Dashboards**: Engineering monitors infrastructure dashboards, security monitors security findings. **Log Retention**: CloudWatch Logs retained 1 year, CloudTrail logs 2 years.",
            "evidence": "- CloudWatch dashboard configurations\n- CloudTrail enabled in all regions\n- Security Hub findings reports\n- CloudWatch alarm configurations\n- Infrastructure monitoring logs"
        },
        "siem": {
            "objective": "Centralize security event logs from all sources for correlation, alerting, and investigation.",
            "implementation": "**SIEM Platform**: Splunk, Elastic SIEM, or cloud-native (AWS Security Lake). **Log Sources**: CloudTrail, VPC Flow Logs, ALB logs, application logs, EDR, IdP auth logs, SaaS audit logs. **Correlation Rules**: Detect patterns indicating attacks (brute force, privilege escalation, data exfiltration). **Alerting**: Security team receives alerts for critical events via PagerDuty. **Retention**: 1 year online, 2 years archived (compliance requirement). **Daily Monitoring**: Security team reviews SIEM daily for anomalies.",
            "evidence": "- SIEM architecture diagram\n- Log source inventory\n- Correlation rule configurations\n- SIEM alert history\n- Daily SIEM review logs"
        }
    },
    "network-security": {
        "cloud-network-security": {
            "objective": "Implement network segmentation, access controls, and traffic filtering in cloud environments to prevent unauthorized access and lateral movement.",
            "implementation": "**VPC Design**: Multi-tier VPC with public, private, and data subnets. **Security Groups**: Deny-by-default, only required ports open, documented business justification. **NACLs**: Network ACLs provide subnet-level controls as defense in depth. **Private Subnets**: Production data systems in private subnets, no direct internet access. **NAT Gateway**: Outbound internet via NAT gateway for private subnets. **VPC Flow Logs**: Enabled for traffic analysis and incident investigation. **Quarterly Reviews**: Review security group rules, remove overly permissive rules.",
            "evidence": "- VPC architecture diagrams\n- Security group configurations\n- NACL rules\n- VPC Flow Logs enabled\n- Quarterly security group audits"
        },
        "endpoint-network-security": {
            "objective": "Protect endpoints from network-based attacks through firewall, VPN, and secure network configurations.",
            "implementation": "**Host Firewall**: Enabled on all endpoints via MDM configuration profile, only required ports open. **VPN Required**: VPN mandatory for internal resource access from untrusted networks. **Network Segmentation**: Office network separates guest WiFi from corporate. **DNS Filtering**: Corporate DNS blocks malicious domains (via Pi-hole, Cisco Umbrella). **Zero Trust**: Cloud resource access via SSO and IAM, no corporate network trust assumptions. **WPA3**: Office WiFi uses WPA3 encryption or WPA2-Enterprise with certificate authentication.",
            "evidence": "- Host firewall configuration profiles\n- VPN usage logs\n- Network architecture diagrams\n- DNS filtering block logs\n- WiFi security configuration"
        }
    },
    "personnel-security": {
        "insider-threat-mitigation": {
            "objective": "Detect and mitigate insider threats through monitoring, access controls, and awareness.",
            "implementation": "**User Behavior Analytics**: SIEM or UEBA tool monitors for anomalous activity (unusual access times, mass downloads, privilege escalation). **Least Privilege**: Users granted minimum necessary access, elevated access logged and time-bound. **DLP**: Data Loss Prevention blocks large data transfers to external storage. **HR Coordination**: HR notifies IT immediately of terminations or performance issues. **Separation of Duties**: Critical actions require two-person approval (production deployments, infrastructure changes). **Awareness**: Security training includes insider threat indicators, reporting suspicious behavior.",
            "evidence": "- UEBA alerts and investigations\n- Least privilege access policies\n- DLP policy configuration\n- HR-IT coordination procedures\n- Separation of duties matrix"
        },
        "personnel-lifecycle-management": {
            "objective": "Securely manage employee access throughout hire, change, and termination lifecycle.",
            "implementation": "**Onboarding**: New hire access provisioned via ServiceNow request, approved by manager, completed by IT. Background check completed before start date. Security training completed within first week. **Changes**: Access changes (promotions, team transfers) follow same request/approval workflow. **Offboarding**: Termination initiated in HRIS, triggers automated workflow: account deactivation within 1 hour (via SCIM), device remote wipe, access reviews to catch missed removals. **Auditing**: Quarterly access reviews validate all users have appropriate access.",
            "evidence": "- Access provisioning tickets\n- Background check records\n- Onboarding checklists\n- Offboarding workflow logs\n- Quarterly access review results"
        },
        "rules-of-behavior": {
            "objective": "Define expected security behaviors for employees through documented rules and annual acknowledgment.",
            "implementation": "**Acceptable Use Policy**: Documented rules covering device use, data handling, password management, physical security, incident reporting. **Annual Acknowledgment**: All employees acknowledge AUP annually via LMS. **Consequences**: Policy violations may result in disciplinary action up to termination. **Training**: Annual security awareness training reinforces rules of behavior. **Exceptions**: Exceptions require security team approval, documented justification, executive sign-off for material risks. **Updates**: AUP reviewed annually, updated based on new threats and technologies.",
            "evidence": "- Acceptable Use Policy\n- Employee policy acknowledgments\n- Security awareness training completion\n- Policy exception requests and approvals\n- Annual policy review records"
        }
    },
    "physical-protection": {
        "office-security": {
            "objective": "Protect physical office locations through access controls, visitor management, and security awareness.",
            "implementation": "**Badge Access**: Office requires badge for entry, issued to employees only. **Visitor Management**: Visitors sign in, receive temporary badge, escorted by employee. **Desk Policy**: Clean desk policy for Confidential documents, lock screens when away. **Secure Areas**: Server rooms or equipment closets require additional access control. **Surveillance**: Security cameras in common areas (lobby, exits), not in private spaces. **Offboarding**: Badges deactivated and collected upon termination. **Remote Work**: Most employees remote, office physical security less critical than cloud/endpoint security.",
            "evidence": "- Badge access system records\n- Visitor logs\n- Clean desk policy\n- Secure area access logs\n- Badge deactivation records"
        }
    },
    "risk-management": {
        "organizational-risk-assessment": {
            "objective": "Identify, assess, and track organizational security risks to prioritize mitigation efforts and resource allocation.",
            "implementation": "**Annual Risk Assessment**: Security team conducts comprehensive risk assessment covering technology, people, processes. **Risk Identification**: Workshops with stakeholders, threat intelligence, vulnerability scans, past incidents. **Risk Scoring**: Likelihood (1-5) × Impact (1-5) = Risk Score. **Risk Register**: Tracked in GRC tool or spreadsheet, includes description, owner, score, mitigation status. **Mitigation Plans**: High/critical risks require documented mitigation plan with timeline. **Quarterly Reviews**: Security Committee reviews risk register, tracks remediation progress. **Metrics**: Track risk trends, time to mitigate, open high/critical risks.",
            "evidence": "- Annual risk assessment reports\n- Risk register\n- Risk scoring methodology\n- Mitigation plans for high/critical risks\n- Quarterly risk review meeting notes"
        },
        "vendor-risk-management": {
            "objective": "Assess and manage security risks from third-party vendors, especially those accessing systems or handling sensitive data.",
            "implementation": "**Vendor Inventory**: Maintain list of all vendors, categorize by risk (critical, high, medium, low). **Security Assessments**: Critical/high-risk vendors complete security questionnaire, provide SOC 2 report. **DPAs Required**: Data Processing Agreements for vendors processing customer personal data. **Contract Terms**: Contracts include security requirements, audit rights, breach notification obligations. **Ongoing Monitoring**: Annual reassessment for critical vendors, monitor for breaches via threat intelligence. **Offboarding**: Revoke vendor access when contract ends, ensure data deletion.",
            "evidence": "- Vendor inventory with risk ratings\n- Vendor security questionnaires and SOC 2 reports\n- Data Processing Agreements\n- Vendor risk assessment reports\n- Vendor offboarding documentation"
        }
    },
    "security-assurance": {
        "bug-bounty-program": {
            "objective": "Crowdsource vulnerability discovery through a bug bounty program, enabling independent researchers to report security issues.",
            "implementation": "**Bug Bounty Platform**: HackerOne or Bugcrowd manages program. **Scope**: Public-facing web applications and APIs in scope, internal systems out of scope. **Rewards**: Critical $500-$2000, High $200-$500, Medium $50-$200, Low discretionary. **Response SLA**: Triage within 2 business days, fix critical within 30 days. **Safe Harbor**: Policy protects researchers acting in good faith. **Private Program**: Consider starting with private (invite-only) program before going public. **Quarterly Reviews**: Review program metrics, adjust scope and rewards based on findings.",
            "evidence": "- Bug bounty program policy\n- Platform reports (submissions, resolutions, payouts)\n- Vulnerability remediation tickets\n- Program performance metrics\n- Researcher payouts"
        },
        "customer-security-communications": {
            "objective": "Transparently communicate security posture and incidents to customers, building trust and meeting contractual obligations.",
            "implementation": "**Security Portal**: Publicly accessible portal with SOC 2 report, security overview, compliance certifications. **Trust Center**: Website section covering security practices, data protection, compliance. **Incident Communication**: Notify affected customers of security incidents per contract SLAs and legal requirements. **Status Page**: Real-time system status and incident updates. **Security Newsletter**: Periodic updates to customers about security improvements. **Customer Questionnaires**: Respond to customer security questionnaires (standardized responses saved).",
            "evidence": "- Security portal access logs\n- Trust center documentation\n- Customer incident notifications\n- Status page incident history\n- Security questionnaire responses"
        },
        "penetration-tests": {
            "objective": "Validate security control effectiveness through independent penetration testing, identifying vulnerabilities before attackers do.",
            "implementation": "**Annual Pentest**: Third-party penetration testing firm tests production systems annually. **Scope**: External pentest (internet-facing systems), internal pentest (assumes breach), web application pentest, API pentest. **Rules of Engagement**: Define testing window, out-of-scope systems, emergency stop procedures. **Findings Remediation**: Critical findings fixed within 30 days, high within 60 days, medium within 90 days. **Retest**: Penetration testing firm retests critical/high findings after remediation. **Report**: Executive summary and detailed technical report provided to security team and executives.",
            "evidence": "- Penetration test reports (current and historical)\n- Remediation tracking for findings\n- Retest validation reports\n- Penetration test scoping documents\n- Vendor invoices and contracts"
        },
        "security-reviews": {
            "objective": "Review proposed system changes and new features for security implications before implementation.",
            "implementation": "**Trigger Criteria**: New features handling sensitive data, architecture changes, third-party integrations, new authentication mechanisms. **Review Process**: Engineer submits design doc, security team reviews within 3 business days. **Threat Modeling**: Identify threats using STRIDE methodology, document mitigations. **Security Requirements**: Security team provides specific requirements (encryption, access controls, logging). **Sign-Off**: Security team approves before implementation begins. **Post-Implementation**: Security team verifies requirements implemented correctly. **Quarterly Metrics**: Track reviews conducted, time to review, findings by severity.",
            "evidence": "- Security review request tickets\n- Design review documents with security sign-off\n- Threat models\n- Security requirements documents\n- Post-implementation verification"
        }
    },
    "security-engineering": {
        "automated-code-analysis": {
            "objective": "Identify security vulnerabilities in code automatically during development through static and dynamic analysis.",
            "implementation": "**SAST**: Static Application Security Testing (Snyk Code, SonarQube) integrated in CI/CD, scans code for vulnerabilities (SQL injection, XSS, hardcoded secrets). **Dependency Scanning**: Snyk or Dependabot scans dependencies for known vulnerabilities, creates PRs for updates. **Secret Scanning**: GitGuardian or TruffleHog blocks commits containing secrets. **PR Gates**: Critical/high vulnerabilities block PR merges. **Dashboards**: Engineering leadership monitors security findings, tracks remediation. **SLA**: Critical findings fixed within 7 days, high within 30 days.",
            "evidence": "- SAST tool configuration and findings\n- Dependency vulnerability reports\n- Secret scanning blocks\n- PR merge blocking events\n- Vulnerability remediation metrics"
        },
        "secure-code-review": {
            "objective": "Review code changes for security vulnerabilities through peer review and security-focused code reviews.",
            "implementation": "**Mandatory PR Review**: All code changes require at least one peer review before merge. **Security Checklist**: Reviewers check for common vulnerabilities (input validation, authentication, authorization, sensitive data handling). **Security Champion Review**: High-risk changes (authentication, payment processing, data export) reviewed by security champion or security team. **Automated Checks**: SAST, linting, and tests run automatically on PRs. **Training**: Developers receive secure coding training, security champions receive advanced training. **Metrics**: Track PR review time, security findings in review.",
            "evidence": "- GitHub PR review requirements\n- Security code review checklist\n- Security champion assignments\n- Secure coding training records\n- Code review metrics"
        },
        "secure-coding-standards": {
            "objective": "Define and enforce secure coding practices to prevent common vulnerabilities during development.",
            "implementation": "**Standards Documentation**: Secure coding guide covering OWASP Top 10, common vulnerability patterns, language-specific guidance. **Input Validation**: Validate all user input, use parameterized queries, escape output. **Authentication**: Use established libraries (OAuth, SAML), never roll custom crypto. **Authorization**: Implement least privilege, check authorization at resource level, don't trust client-side controls. **Secrets**: Never hardcode secrets, use secrets management service. **Logging**: Log authentication events, authorization failures, never log sensitive data. **Training**: Annual secure coding training for all engineers. **Code Review**: Standards enforced through peer review and automated scanning.",
            "evidence": "- Secure coding standards document\n- OWASP Top 10 remediation guidance\n- Secure coding training materials\n- Code review enforcement metrics\n- Vulnerability findings by category"
        }
    },
    "security-training": {
        "incident-response-training": {
            "objective": "Ensure incident response team members can effectively respond to security incidents through regular training and exercises.",
            "implementation": "**Incident Response Training**: Annual training for IR team covering procedures, tools, communication. **Role-Specific**: Engineers (containment, investigation), security (triage, coordination), legal (breach notification), PR (customer comms). **Hands-On Labs**: Practice using forensics tools, log analysis, containment procedures. **Quarterly Tabletops**: Tabletop exercises for realistic incident scenarios. **Runbooks**: Documented procedures for common incident types (ransomware, data breach, DDoS). **Post-Incident Review**: Every incident includes lessons learned, update training and runbooks based on gaps.",
            "evidence": "- IR team training materials\n- Training completion records\n- Tabletop exercise documentation\n- Incident response runbooks\n- Post-incident review improvements"
        },
        "secure-coding-training": {
            "objective": "Train developers on secure coding practices to prevent vulnerabilities from being introduced in code.",
            "implementation": "**Annual Training**: All engineers complete secure coding training annually (e.g., OWASP Top 10, secure coding practices for languages used). **Onboarding**: New engineers complete training within first month. **Hands-On**: Training includes vulnerable code examples, remediation exercises. **Topics**: Input validation, authentication, authorization, cryptography, secrets management, OWASP Top 10. **Security Champions**: Advanced secure coding training for security champions. **Assessment**: Knowledge check at end of training, minimum 80% to pass. **Tracking**: LMS tracks completion, managers notified of non-compliance.",
            "evidence": "- Secure coding training materials\n- Training completion reports (100% target)\n- Training assessment scores\n- Security champion advanced training\n- LMS training records"
        },
        "security-awareness-training": {
            "objective": "Train all employees on security threats, policies, and best practices to reduce human risk factors.",
            "implementation": "**Annual Training**: All employees complete security awareness training annually, new hires within first week. **Topics**: Phishing identification, password security, device security, data handling, physical security, incident reporting. **Phishing Simulations**: Quarterly simulated phishing campaigns, users who click receive remedial training. **Microlearning**: Monthly security tips via email or Slack. **Gamification**: Track training completion rates, leaderboards, prizes for participation. **Assessment**: Knowledge check at end of training, minimum 80% to pass. **Metrics**: Track completion rates (target 100%), phishing simulation click rates (target <5%).",
            "evidence": "- Security awareness training materials\n- Training completion reports\n- Phishing simulation results\n- Training assessment scores\n- Remedial training for phishing failures"
        }
    },
    "threat-detection": {
        "cloud-threat-detection": {
            "objective": "Detect malicious activity in cloud environments using threat intelligence and behavioral analysis.",
            "implementation": "**AWS GuardDuty**: Continuously monitors VPC Flow Logs, CloudTrail, DNS logs for threats (compromised instances, reconnaissance, unauthorized access). **Alerts**: GuardDuty findings sent to Security Hub and SIEM, critical alerts to PagerDuty. **Threat Intelligence**: GuardDuty uses AWS threat intelligence feeds and custom threat intel. **Response**: Security team investigates alerts within SLA (Critical: 1 hour, High: 4 hours). **Automated Remediation**: Lambda functions auto-remediate common issues (isolate compromised instance, block malicious IPs). **Quarterly Review**: Review GuardDuty findings, tune detection rules to reduce false positives.",
            "evidence": "- GuardDuty enabled in all regions and accounts\n- GuardDuty findings and remediation actions\n- SIEM integration logs\n- Threat detection SLA compliance\n- Quarterly threat detection reviews"
        },
        "endpoint-threat-detection": {
            "objective": "Detect and respond to malware, ransomware, and other threats on endpoint devices.",
            "implementation": "**EDR**: Endpoint Detection and Response (CrowdStrike Falcon, SentinelOne) deployed on all endpoints. **Real-Time Protection**: Antivirus, behavior monitoring, exploit prevention, ransomware protection. **Threat Hunting**: EDR enables proactive threat hunting queries across all endpoints. **Automated Response**: EDR can automatically isolate compromised endpoints. **SIEM Integration**: EDR alerts forwarded to SIEM for correlation with other security events. **24/7 Monitoring**: Security team monitors EDR console, receives critical alerts. **Metrics**: Track malware detections, response time, false positive rate.",
            "evidence": "- EDR deployment coverage (100% target)\n- Malware detection and remediation logs\n- Threat hunting query results\n- Endpoint isolation events\n- EDR alert response metrics"
        },
        "saas-threat-detection": {
            "objective": "Detect threats and anomalies in SaaS application usage through CASB and SaaS security tools.",
            "implementation": "**CASB**: Cloud Access Security Broker (Netskope, Zscaler) monitors SaaS usage, detects anomalies. **Anomaly Detection**: Alert on unusual behavior (login from new country, mass downloads, sharing data externally). **Shadow IT**: CASB discovers unauthorized SaaS apps. **DLP**: Data Loss Prevention policies block uploads of Confidential data to unapproved apps. **OAuth Monitoring**: Monitor OAuth grants, revoke suspicious third-party app access. **Threat Intelligence**: CASB incorporates threat intel to block access to malicious sites. **Response**: Security team investigates alerts, works with users to remediate.",
            "evidence": "- CASB deployment and configuration\n- Anomaly detection alerts and investigations\n- Shadow IT discovery reports\n- DLP policy violations\n- OAuth app reviews and revocations"
        }
    },
    "vulnerability-management": {
        "cloud-vulnerability-detection": {
            "objective": "Continuously identify vulnerabilities in cloud infrastructure through automated scanning and configuration assessments.",
            "implementation": "**AWS Inspector**: Scans EC2 instances for vulnerabilities, checks against CVEs and CIS benchmarks. **Config Rules**: AWS Config checks for misconfigurations (S3 public access, unencrypted storage, excessive permissions). **Security Hub**: Aggregates findings from Inspector, Config, and other sources. **Severity Scoring**: CVSS scores prioritize remediation (Critical: ≥9.0, High: 7.0-8.9). **SLAs**: Critical vulns fixed within 7 days, high within 30 days, medium within 90 days. **Quarterly Reviews**: Review vulnerability trends, update scanning coverage.",
            "evidence": "- AWS Inspector scan results\n- Config rule compliance reports\n- Security Hub findings dashboard\n- Vulnerability remediation tracking\n- Vulnerability management metrics"
        },
        "endpoint-vulnerability-detection": {
            "objective": "Identify vulnerabilities and missing patches on endpoint devices to maintain secure configurations.",
            "implementation": "**Patch Management**: MDM (Jamf, Intune) reports installed OS versions and patch levels. **Vulnerability Scanning**: EDR or vulnerability scanner identifies missing patches and vulnerable software. **Patch SLAs**: Critical OS patches within 7 days, high within 30 days. **Automated Patching**: MDM can push critical patches automatically after testing. **Application Updates**: Monitor for vulnerable applications (browsers, productivity software), notify users to update. **Compliance Reporting**: Weekly reports on endpoint patch compliance, escalate non-compliant devices.",
            "evidence": "- MDM patch compliance reports\n- Vulnerability scan results\n- Patch deployment logs\n- Patch compliance metrics by severity\n- Non-compliant device escalations"
        },
        "vulnerability-management-process": {
            "objective": "Establish systematic process for identifying, prioritizing, and remediating vulnerabilities across all systems.",
            "implementation": "**Continuous Scanning**: Automated vulnerability scanning (AWS Inspector, EDR, dependency scanning) runs continuously. **Centralized Tracking**: Vulnerabilities tracked in GRC tool or ticketing system. **Risk-Based Prioritization**: Prioritize by CVSS score, exploitability, asset criticality, data sensitivity. **SLAs**: Critical 7 days, High 30 days, Medium 90 days. **Ownership**: Vulnerabilities assigned to responsible teams (engineering, IT, security). **Metrics Dashboard**: Track open vulns by severity, MTTR, SLA compliance. **Quarterly Reviews**: Security Committee reviews vulnerability trends, addresses recurring issues.",
            "evidence": "- Vulnerability scanning configuration\n- Vulnerability tracking database\n- Remediation SLA compliance reports\n- Vulnerability metrics dashboard\n- Quarterly vulnerability management reviews"
        }
    }
}

def get_control_content(family, filename):
    """Get appropriate content for a control based on family and filename."""
    slug = filename.replace('.md', '')

    if family in CONTROL_CONTENT and slug in CONTROL_CONTENT[family]:
        return CONTROL_CONTENT[family][slug]

    # Fallback: Generate generic content based on control title
    return None

def fill_template_control(file_path):
    """Fill a template control with realistic content."""
    content = file_path.read_text()

    # Check if it's a template
    if '[Control objective]' not in content:
        return False

    # Extract metadata
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return False

    frontmatter = match.group(1)
    body = match.group(2)

    # Parse frontmatter
    metadata = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()

    family = metadata.get('family', '')
    title = metadata.get('title', '')
    filename = file_path.name

    # Get control content
    control_data = get_control_content(family, filename)

    if not control_data:
        # Skip controls without predefined content for now
        return False

    # Replace template sections
    new_content = content.replace(
        '[Control objective]',
        control_data['objective']
    ).replace(
        '[How this control is implemented]',
        control_data['implementation']
    ).replace(
        '[Audit evidence for this control]',
        control_data['evidence']
    )

    file_path.write_text(new_content)
    return True

def main():
    controls_dir = Path("docs/controls")

    if not controls_dir.exists():
        print(f"Error: {controls_dir} does not exist")
        return

    print("Filling template controls...\n")

    filled = []
    skipped = []

    for control_file in sorted(controls_dir.rglob("*.md")):
        if '[Control objective]' in control_file.read_text():
            if fill_template_control(control_file):
                print(f"✓ {control_file.relative_to(controls_dir)}")
                filled.append(str(control_file.relative_to(controls_dir)))
            else:
                print(f"⏭️  {control_file.relative_to(controls_dir)} (no content defined)")
                skipped.append(str(control_file.relative_to(controls_dir)))

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Filled: {len(filled)} controls")
    print(f"Skipped: {len(skipped)} controls (need content)")

    if filled:
        print(f"\nFilled controls:")
        for path in filled:
            print(f"  ✓ {path}")

if __name__ == '__main__':
    main()
