# GraphGRC Documentation

A comprehensive, interconnected GRC (Governance, Risk, and Compliance) documentation system with bidirectional linking between controls, standards, processes, policies, and framework requirements.

## Table of Contents

- [Charter](#charter)
- [Policies](#policies)
- [Standards](#standards)
- [Processes](#processes)
- [Custom Controls](#custom-controls)
- [Frameworks](#frameworks)
  - [SOC 2](#soc-2)
  - [GDPR](#gdpr)

---

## Charter

Strategic governance documents defining the information security program.

| Document | Description |
|----------|-------------|
| [Information Security Program Charter](charter/information-security-program-charter.md) | Mission, scope, governance structure, and program components |
| [Risk Management Strategy](charter/risk-management-strategy.md) | Risk appetite, assessment methodology, and treatment framework |

---

## Policies

Security policies defining requirements for all personnel.

| Policy | Applies To | Description |
|--------|-----------|-------------|
| [Baseline Security Policy](policies/baseline-security-policy.md) | All Employees | Minimum security practices for account security, data handling, devices, and incident reporting |
| [Engineering Security Policy](policies/engineering-security-policy.md) | Engineers | Secure coding, secrets management, code review, and deployment security |
| [Data Access Policy](policies/data-access-policy.md) | Engineers, Data Team, Support | Requirements for accessing, handling, and protecting customer and employee data |

---

## Standards

Technical security standards and baseline configurations.

| Standard | Owner | Description |
|----------|-------|-------------|
| [AWS Security Standard](standards/aws-security-standard.md) | Infrastructure Team | Baseline security configurations for all AWS resources |
| [Cryptography Standard](standards/cryptography-standard.md) | Security Team | Requirements for encryption at rest, in transit, and key management |
| [Data Classification Standard](standards/data-classification-standard.md) | Security Team | Four-tier data classification system (Public, Internal, Confidential, Restricted) |
| [Data Retention Standard](standards/data-retention-standard.md) | Security Team | Retention periods and secure deletion requirements |
| [Endpoint Security Standard](standards/endpoint-security-standard.md) | IT Team | Baseline security for employee endpoints (macOS laptops) |
| [GitHub Security Standard](standards/github-security-standard.md) | Engineering Team | Security requirements for GitHub organizations and repositories |
| [Incident Response Standard](standards/incident-response-standard.md) | Security Team | Requirements for detecting, responding to, and recovering from incidents |
| [Logging and Monitoring Standard](standards/logging-monitoring-standard.md) | Infrastructure Team | Requirements for security logging, monitoring, and alerting |
| [SaaS IAM Standard](standards/saas-iam-standard.md) | IT Team | Identity and access management requirements for SaaS applications |
| [Vulnerability Management Standard](standards/vulnerability-management-standard.md) | Security Team | Requirements for identifying, assessing, and remediating vulnerabilities |

---

## Processes

Step-by-step operational procedures.

| Process | Owner | Description |
|---------|-------|-------------|
| [Access Provisioning Process](processes/access-provisioning-process.md) | IT Team | Steps for granting new user access with MFA enrollment and role-based permissions |
| [Access Review Process](processes/access-review-process.md) | Security Team | Quarterly access reviews by managers with documentation and certification |
| [Backup and Recovery Process](processes/backup-recovery-process.md) | Infrastructure Team | Automated backups, monitoring, quarterly recovery testing, and annual DR drills |
| [Change Management Process](processes/change-management-process.md) | Engineering Team | Managing changes to production systems with testing, review, and rollback procedures |
| [Data Breach Response Process](processes/data-breach-response-process.md) | Security Team | 10-step response for unauthorized data access with GDPR notification requirements |
| [Incident Response Process](processes/incident-response-process.md) | Security Team | 9-step process for detecting, investigating, and responding to security incidents |
| [Security Training Process](processes/security-training-process.md) | Security Team | Training program with new hire, annual refresher, role-specific, and phishing simulations |
| [Vendor Risk Assessment Process](processes/vendor-risk-assessment-process.md) | Security Team | 8-step vendor assessment with questionnaires, SOC 2 review, and DPA negotiation |
| [Vulnerability Management Process](processes/vulnerability-management-process.md) | Security Team | Automated scanning, triage, risk assessment, remediation, and verification |

---

## Custom Controls

Organization-specific security controls mapped to SOC 2 and GDPR.

### Access Control (ACC)

| Control | Title | Objective |
|---------|-------|-----------|
| [ACC-01](custom/acc-01.md) | Identity & Authentication | Ensure all users are uniquely identified and authenticated using strong, phishing-resistant methods |
| [ACC-02](custom/acc-02.md) | Least Privilege & RBAC | Ensure users have only the minimum access necessary for their job function |
| [ACC-03](custom/acc-03.md) | Access Reviews | Periodically review and certify that user access remains appropriate |
| [ACC-04](custom/acc-04.md) | Privileged Access Management | Secure, monitor, and audit all privileged (admin) access |

### Data Protection (DAT)

| Control | Title | Objective |
|---------|-------|-----------|
| [DAT-01](custom/dat-01.md) | Data Classification | Classify data based on sensitivity to enable appropriate protection controls |
| [DAT-02](custom/dat-02.md) | Encryption | Protect data confidentiality through encryption at rest and in transit |
| [DAT-03](custom/dat-03.md) | Data Retention & Deletion | Retain data only as long as necessary and securely delete when no longer needed |
| [DAT-04](custom/dat-04.md) | Data Privacy (GDPR Compliance) | Comply with GDPR and CCPA privacy requirements |

### Endpoint Security (END)

| Control | Title | Objective |
|---------|-------|-----------|
| [END-01](custom/end-01.md) | Device Management (macOS MDM) | Ensure all endpoints are enrolled in MDM with security configurations enforced |
| [END-02](custom/end-02.md) | Endpoint Protection | Detect and prevent malware and unauthorized software on endpoints |
| [END-03](custom/end-03.md) | Software Updates | Ensure endpoints have latest security patches to prevent exploitation |

### Governance (GOV)

| Control | Title | Objective |
|---------|-------|-----------|
| [GOV-01](custom/gov-01.md) | Security Policies | Establish and maintain security policies that define organizational security requirements |
| [GOV-02](custom/gov-02.md) | Risk Assessment | Identify, assess, and manage information security risks |

### Infrastructure (INF)

| Control | Title | Objective |
|---------|-------|-----------|
| [INF-01](custom/inf-01.md) | Cloud Security Configuration (AWS) | Ensure cloud infrastructure is securely configured according to best practices |
| [INF-02](custom/inf-02.md) | Network Security | Protect network perimeter and segment internal networks |
| [INF-03](custom/inf-03.md) | Logging & Monitoring | Detect and respond to security events through comprehensive logging |
| [INF-04](custom/inf-04.md) | Backup & Recovery | Ensure business continuity through regular backups and tested recovery procedures |

### Operations (OPS)

| Control | Title | Objective |
|---------|-------|-----------|
| [OPS-01](custom/ops-01.md) | Change Management | Manage changes to production systems to maintain security and stability |
| [OPS-02](custom/ops-02.md) | Vulnerability Management | Identify and remediate security vulnerabilities in a timely manner |
| [OPS-03](custom/ops-03.md) | Incident Response | Detect, respond to, and recover from security incidents |
| [OPS-04](custom/ops-04.md) | Business Continuity | Ensure critical operations can continue during disruptions |

### People (PEO)

| Control | Title | Objective |
|---------|-------|-----------|
| [PEO-01](custom/peo-01.md) | Background Checks | Verify trustworthiness of employees before granting access |
| [PEO-02](custom/peo-02.md) | Security Training | Ensure all personnel are aware of security policies and threats |
| [PEO-03](custom/peo-03.md) | Offboarding | Ensure access is promptly removed when employment ends |

### Vendor (VEN)

| Control | Title | Objective |
|---------|-------|-----------|
| [VEN-01](custom/ven-01.md) | Third-Party Risk Assessment | Assess security and privacy risks of third-party vendors before onboarding |
| [VEN-02](custom/ven-02.md) | Vendor Contracts & DPAs | Ensure vendors are contractually obligated to protect data |

---

## Frameworks

### SOC 2

SOC 2 Trust Services Criteria controls with backlinks showing which custom controls satisfy them.

| Control | Title |
|---------|-------|
| [CC1.1](cc11.md) | Management and board demonstrate commitment to integrity and ethical values |
| [CC1.2](cc12.md) | Board demonstrates independence and oversight |
| [CC1.4](cc14.md) | Management demonstrates commitment to competence |
| [CC2.1](cc21.md) | Communication of information security responsibilities |
| [CC2.2](cc22.md) | Internal and external communication of system objectives |
| [CC3.1](cc31.md) | Risk identification and assessment |
| [CC3.2](cc32.md) | Assessment of fraud risk |
| [CC3.4](cc34.md) | Risk response and acceptance |
| [CC6.1](cc61.md) | Logical access security software |
| [CC6.2](cc62.md) | User registration and authorization before access |
| [CC6.3](cc63.md) | Access removal on termination |
| [CC6.6](cc66.md) | Access restricted to information assets |
| [CC6.7](cc67.md) | Transmission, movement, and removal protection |
| [CC6.8](cc68.md) | Encryption in transit and at rest |
| [CC7.1](cc71.md) | Detection of processing errors and security issues |
| [CC7.2](cc72.md) | Monitoring of system components |
| [CC7.3](cc73.md) | System capacity evaluation |
| [CC7.4](cc74.md) | System availability monitoring and incident response |
| [CC7.5](cc75.md) | System availability protection |
| [CC8.1](cc81.md) | Authorization and testing before implementation |
| [CC9.1](cc91.md) | Identification and mitigation of risks from vendors |
| [CC9.2](cc92.md) | Assessment of vendor compliance |
| [A1.1](a11.md) | System availability and commitments |
| [A1.2](a12.md) | System capacity meets commitments |
| [A1.3](a13.md) | Environmental safeguards for system availability |

[View all SOC 2 controls →](soc2/)

### GDPR

GDPR articles with backlinks showing which custom controls help achieve compliance.

| Article | Title |
|---------|-------|
| [Article 5](art5.md) | Principles relating to processing of personal data |
| [Article 6](art6.md) | Lawfulness of processing |
| [Article 15](art15.md) | Right of access by the data subject |
| [Article 17](art17.md) | Right to erasure (right to be forgotten) |
| [Article 20](art20.md) | Right to data portability |
| [Article 24](art24.md) | Responsibility of the controller |
| [Article 28](art28.md) | Processor obligations and data processing agreements |
| [Article 30](art30.md) | Records of processing activities |
| [Article 32](art32.md) | Security of processing |
| [Article 33](art33.md) | Notification of a personal data breach to the supervisory authority |
| [Article 34](art34.md) | Communication of a personal data breach to the data subject |

[View all GDPR articles →](gdpr/)

---

## About This Documentation

This documentation system uses:
- **Bidirectional linking**: Navigate from controls to frameworks and back
- **Semantic markdown**: Pure markdown with YAML frontmatter (Obsidian and GitHub Pages compatible)
- **Automated backlinks**: `make generate-backlinks` creates Referenced By sections automatically
- **Four-tier architecture**: Charter → Policies → Standards/Processes → Custom Controls → Frameworks

For more information:
- [Documentation Structure Guide](STRUCTURE.md)
- [Project README](README.md)
- [GitHub Repository](https://github.com/alsmola/graphgrc/)

---

*Documentation generated with [GraphGRC](https://github.com/alsmola/graphgrc/) • Last updated: 2025-01-13*
