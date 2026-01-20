# GraphGRC Documentation

Comprehensive GRC (Governance, Risk, and Compliance) documentation system with bidirectional linking between controls, standards, processes, policies, and framework requirements.

## Structure

This documentation follows a hierarchical model:
- **Charter** → Defines mission, principles, and governance
- **Policies** → Role-based security requirements
- **Standards** → Technical security baselines
- **Processes** → Step-by-step operational procedures
- **Controls** → Specific security controls organized by family
- **Frameworks** → External compliance frameworks (SOC 2, GDPR, ISO 27001, etc.)

## Charter

Strategic governance documents defining the information security program.

| Document | Description |
|----------|-------------|
| [Governance](charter/governance.md) | Mission, scope, governance structure, and program components |
| [Risk Management](charter/risk-management.md) | Risk appetite, assessment methodology, and treatment framework |

## Policies

Role-based security policies defining requirements for personnel.

| Policy | Applies To | Description |
|--------|-----------|-------------|
| [Employee](policies/employee.md) | All Employees | Baseline security practices for all personnel |
| [Engineer](policies/engineer.md) | Engineers | Secure coding, code review, production access |
| [IT Administrator](policies/it-administrator.md) | IT Team | Privileged access, account management, SaaS administration |
| [HR Administrator](policies/hr-administrator.md) | HR Team | Employee data protection, HRIS administration |
| [Product Administrator](policies/product-administrator.md) | Product/Support | Customer data access, support operations |
| [Security Team](policies/security-team.md) | Security Team | Security operations, risk management, compliance |

## Standards

Technical security standards and baseline configurations.

| Standard                                                                  | Owner               | Description                                 |
| ------------------------------------------------------------------------- | ------------------- | ------------------------------------------- |
| [Cloud Security](standards/cloud-security.md)                             | Infrastructure Team | Baseline configurations for cloud resources |
| [Cryptography](standards/cryptography.md)                                 | Security Team       | Encryption requirements and key management  |
| [Customer Support Data Access](standards/customer-support-data-access.md) | Support Team        | Requirements for accessing customer data    |
| [Data Classification](standards/data-classification.md)                   | Security Team       | Four-tier data classification system        |
| [Data Isolation](standards/data-isolation.md)                             | Engineering Team    | Multi-tenancy and data separation           |
| [Data Retention](standards/data-retention.md)                             | Security Team       | Retention periods and deletion requirements |
| [Infrastructure Hardening](standards/infrastructure-hardening.md)         | Infrastructure Team | Baseline hardening for infrastructure       |
| [SaaS IAM](standards/saas-iam.md)                                         | IT Team             | Identity and access management for SaaS     |
| [Security Change Management](standards/security-change-management.md)     | Engineering Team    | Security review for changes                 |
| [Security Communications](standards/security-communications.md)           | Security Team       | Customer security communications            |
| [Version Control Security](standards/version-control-security.md)         | Engineering Team    | Git/GitHub security requirements            |
| [Vulnerability Management](standards/vulnerability-management.md)         | Security Team       | Vulnerability scanning and remediation      |

## Processes

Step-by-step operational procedures.

| Process | Owner | Description |
|---------|-------|-------------|
| [Access Review](processes/access-review.md) | Security Team | Quarterly access reviews |
| [Data Breach Response](processes/data-breach-response.md) | Security Team | Response to unauthorized data access |
| [External Audit](processes/external-audit.md) | Security Team | SOC 2 and other external audits |
| [GRC Change](processes/grc-change.md) | Security Team | Process for updating GRC docs |
| [Internal Audit](processes/internal-audit.md) | Security Team | Self-assessment of controls |
| [Organizational Risk Assessment](processes/organizational-risk-assessment.md) | Security Team | Annual comprehensive risk review |
| [Penetration Testing](processes/penetration-testing.md) | Security Team | Third-party penetration testing |
| [Personal Data Request](processes/personal-data-request.md) | Security Team | GDPR/CCPA data subject requests |
| [Security Alert Triage](processes/security-alert-triage.md) | Security Team | Triage and respond to security alerts |
| [Security Code Review](processes/security-code-review.md) | Security Team | Review code for security issues |
| [Security Design Review](processes/security-design-review.md) | Security Team | Review designs for security risks |
| [Security Incident Response](processes/security-incident-response.md) | Security Team | Detect, investigate, and respond to incidents |
| [Security Tabletop Exercises](processes/security-tabletop-exercises.md) | Security Team | Practice incident response |
| [Vendor Risk Review](processes/vendor-risk-review.md) | Security Team | Assess security of third-party vendors |

## Controls

Organization-specific security controls organized by family, mapped to SOC 2, GDPR, and other frameworks.

### Asset Management

| Control | Title |
|---------|-------|
| [SaaS Inventory](controls/asset-management/saas-inventory.md) | Inventory of SaaS applications |
| [Cloud Inventory](controls/asset-management/cloud-inventory.md) | Inventory of cloud resources |
| [Endpoint Inventory](controls/asset-management/endpoint-inventory.md) | Inventory of employee devices |

### Availability

| Control | Title |
|---------|-------|
| [Disaster Recovery](controls/availability/disaster-recovery.md) | Disaster recovery planning and testing |
| [Availability Monitoring](controls/availability/availability-monitoring.md) | Monitor service availability |
| [Capacity Planning](controls/availability/capacity-planning.md) | Plan for capacity needs |

### Change Management

| Control | Title |
|---------|-------|
| [Change Management](controls/change-management/change-management.md) | Manage changes to production systems |

### Compliance

| Control | Title |
|---------|-------|
| [Contract Management](controls/compliance/contract-management.md) | Manage security contracts and obligations |
| [Internal Audits](controls/compliance/internal-audits.md) | Conduct internal security audits |
| [GRC Function](controls/compliance/grc-function.md) | Maintain GRC program |
| [External Audits](controls/compliance/external-audits.md) | Coordinate external audits |
| [Documentation Review](controls/compliance/documentation-review.md) | Review and update documentation |

### Configuration Management

| Control | Title |
|---------|-------|
| [SaaS Hardening](controls/configuration-management/saas-hardening.md) | Harden SaaS applications |
| [Endpoint Hardening](controls/configuration-management/endpoint-hardening.md) | Harden employee endpoints |
| [Cloud Hardening](controls/configuration-management/cloud-hardening.md) | Harden cloud infrastructure |

### Cryptography

| Control | Title |
|---------|-------|
| [Code Signing](controls/cryptography/code-signing.md) | Sign code and releases |
| [Encryption at Rest](controls/cryptography/encryption-at-rest.md) | Encrypt data at rest |
| [Encryption in Transit](controls/cryptography/encryption-in-transit.md) | Encrypt data in transit |
| [Key Management](controls/cryptography/key-management.md) | Manage cryptographic keys |

### Data Management

| Control | Title |
|---------|-------|
| [Cloud Data Inventory](controls/data-management/cloud-data-inventory.md) | Inventory data in cloud |
| [SaaS Data Inventory](controls/data-management/saas-data-inventory.md) | Inventory data in SaaS apps |
| [Data Classification](controls/data-management/data-classification.md) | Classify data by sensitivity |
| [Data Retention and Deletion](controls/data-management/data-retention-and-deletion.md) | Retain and delete data appropriately |

### Data Privacy

| Control | Title |
|---------|-------|
| [Customer Personal Data](controls/data-privacy/customer-personal-data.md) | Protect customer personal data |
| [Employee Personal Data](controls/data-privacy/employee-personal-data.md) | Protect employee personal data |

### IAM

| Control | Title |
|---------|-------|
| [SaaS IAM](controls/iam/saas-iam.md) | Identity and access management for SaaS |
| [Password Management](controls/iam/password-management.md) | Password policies and management |
| [Secrets Management](controls/iam/secrets-management.md) | Manage application secrets |
| [Single Sign-On](controls/iam/single-sign-on.md) | SSO for applications |
| [Cloud IAM](controls/iam/cloud-iam.md) | IAM for cloud infrastructure |
| [Multi-Factor Authentication](controls/iam/multi-factor-authentication.md) | MFA for authentication |

### Incident Response

| Control | Title |
|---------|-------|
| [Security Incident Response](controls/incident-response/security-incident-response.md) | Respond to security incidents |
| [Data Breach Response](controls/incident-response/data-breach-response.md) | Respond to data breaches |
| [Incident Response Exercises](controls/incident-response/incident-response-exercises.md) | Practice incident response |

### Monitoring

| Control | Title |
|---------|-------|
| [Infrastructure Observability](controls/monitoring/infrastructure-observability.md) | Monitor infrastructure |
| [Endpoint Observability](controls/monitoring/endpoint-observability.md) | Monitor endpoints |
| [SIEM](controls/monitoring/siem.md) | Security information and event management |

### Network Security

| Control | Title |
|---------|-------|
| [Endpoint Network Security](controls/network-security/endpoint-network-security.md) | Network security for endpoints |
| [Cloud Network Security](controls/network-security/cloud-network-security.md) | Network security for cloud |

### Personnel Security

| Control | Title |
|---------|-------|
| [Insider Threat Mitigation](controls/personnel-security/insider-threat-mitigation.md) | Mitigate insider threats |
| [Personnel Lifecycle Management](controls/personnel-security/personnel-lifecycle-management.md) | Onboard and offboard personnel |
| [Rules of Behavior](controls/personnel-security/rules-of-behavior.md) | Define expected behavior |

### Physical Protection

| Control | Title |
|---------|-------|
| [Office Security](controls/physical-protection/office-security.md) | Physical security for offices |

### Risk Management

| Control | Title |
|---------|-------|
| [Vendor Risk Management](controls/risk-management/vendor-risk-management.md) | Assess and manage vendor risks |
| [Organizational Risk Assessment](controls/risk-management/organizational-risk-assessment.md) | Assess organizational risks |

### Security Assurance

| Control | Title |
|---------|-------|
| [Security Reviews](controls/security-assurance/security-reviews.md) | Review security of systems |
| [Penetration Tests](controls/security-assurance/penetration-tests.md) | Third-party penetration testing |
| [Bug Bounty Program](controls/security-assurance/bug-bounty-program.md) | Crowdsourced vulnerability discovery |
| [Customer Security Communications](controls/security-assurance/customer-security-communications.md) | Communicate security posture |

### Security Engineering

| Control | Title |
|---------|-------|
| [Automated Code Analysis](controls/security-engineering/automated-code-analysis.md) | SAST/DAST scanning |
| [Secure Code Review](controls/security-engineering/secure-code-review.md) | Manual code security reviews |
| [Secure Coding Standards](controls/security-engineering/secure-coding-standards.md) | Standards for secure coding |

### Security Training

| Control | Title |
|---------|-------|
| [Secure Coding Training](controls/security-training/secure-coding-training.md) | Train engineers on secure coding |
| [Security Awareness Training](controls/security-training/security-awareness-training.md) | Train all employees on security |
| [Incident Response Training](controls/security-training/incident-response-training.md) | Train on incident response |

### Threat Detection

| Control | Title |
|---------|-------|
| [Endpoint Threat Detection](controls/threat-detection/endpoint-threat-detection.md) | Detect threats on endpoints |
| [SaaS Threat Detection](controls/threat-detection/saas-threat-detection.md) | Detect threats in SaaS apps |
| [Cloud Threat Detection](controls/threat-detection/cloud-threat-detection.md) | Detect threats in cloud |

### Vulnerability Management

| Control | Title |
|---------|-------|
| [Cloud Vulnerability Detection](controls/vulnerability-management/cloud-vulnerability-detection.md) | Scan cloud for vulnerabilities |
| [Endpoint Vulnerability Detection](controls/vulnerability-management/endpoint-vulnerability-detection.md) | Scan endpoints for vulnerabilities |
| [Vulnerability Management Process](controls/vulnerability-management/vulnerability-management-process.md) | Process for managing vulnerabilities |

## Frameworks

External compliance frameworks with mappings to controls.

- **[SOC 2](frameworks/soc2/)** - Trust Services Criteria
- **[GDPR](frameworks/gdpr/)** - EU General Data Protection Regulation
- **[ISO 27001](frameworks/iso27001/)** - Information security management
- **[ISO 27002](frameworks/iso27002/)** - Security controls
- **[NIST 800-53](frameworks/nist80053/)** - Security and privacy controls

## About This Documentation

- **Bidirectional linking**: Navigate from controls to frameworks and back
- **Semantic markdown**: Pure markdown with YAML frontmatter
- **Automated backlinks**: `make generate-backlinks` creates Referenced By sections
- **Hierarchical architecture**: Charter → Policies → Standards/Processes → Controls → Frameworks

---

*Documentation generated with [GraphGRC](https://github.com/engseclabs/graphgrc/) • Last updated: 2025-01-14*
