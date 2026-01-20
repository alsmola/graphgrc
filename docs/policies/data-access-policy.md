---
type: policy
title: Data Access Policy
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: [engineers, data-team, customer-success, support]
---

# Data Access Policy

Requirements for accessing, handling, and protecting customer and employee data.

## Purpose

This policy governs access to Confidential and Restricted data to protect customer privacy, comply with regulations (GDPR, CCPA), and prevent data breaches. Applies in addition to baseline-security-policy.md.

## Scope

Applies to employees and contractors who require access to Confidential or Restricted data as part of their job duties, including:
- Engineers (production database access)
- Data analysts and data scientists
- Customer success and support teams
- Security and infrastructure teams

## Data Classification Review

- **Public:** No restrictions (marketing materials)
- **Internal:** Employees only (source code, internal docs)
- **Confidential:** Sensitive business/customer data (customer PII, contracts, usage data)
- **Restricted:** Highly sensitive with regulatory requirements (payment data, health info, credentials)

See data-classification-standard.md for complete definitions.

## Access Principles

### Least Privilege

- Access granted based on job role and specific business need
- Default to no access, request access explicitly
- Elevated access (admin, write) requires justification

### Need-to-Know

- Access data only for legitimate business purposes
- Do not browse data out of curiosity
- Do not access your own account data or friend/family data without approval

### Purpose Limitation

- Use data only for the approved purpose (e.g., customer support ticket, analytics project)
- Do not repurpose data for other uses without approval
- Do not share data with other teams without proper authorization

## Accessing Confidential Data

### Requirements

- Access to Confidential data requires manager approval and documented business justification
- MFA required for all systems containing Confidential data
- Access logged and monitored (audit trails)
- Quarterly access reviews (ACC-03) certify access is still appropriate
- Use query tools and dashboards (Metabase, Redash), not direct database access where possible

### Responsibilities

- Request minimum access needed (read-only, specific tables, time-limited)
- Do not download large data exports without approval
- Access data through approved tools and environments only (no local copies)
- Log out when done with session

## Accessing Restricted Data

### Requirements

- Access to Restricted data requires Security Team approval in addition to manager approval
- Extremely limited access (only when absolutely necessary)
- Enhanced monitoring (all queries logged, reviewed by security team)
- Quarterly access reviews and justification re-certification
- Use dedicated secure environments (bastion hosts, dedicated VPCs)

### Responsibilities

- Access only when no alternative exists (anonymized data, synthetic data)
- Document every access (ticket with business justification and date/time)
- Never copy Restricted data outside approved systems
- Report any suspected unauthorized access immediately

## Production Database Access

### Requirements

- Production database access restricted to on-call engineers and SREs
- Read-only access by default, write access only for incident response
- All queries logged with user ID and timestamp
- Use read replicas for analytics queries (not primary database)
- No direct queries from local laptop (use bastion host/jump server)

### Responsibilities

- Test queries in staging before running in production
- Use LIMIT clauses on SELECT statements (prevent accidentally querying entire table)
- Do not run UPDATE/DELETE without DRY RUN and peer review
- Kill long-running queries if affecting performance

## Data Exfiltration Prevention

### Requirements

- Large data exports (>10,000 rows) require approval
- Downloaded data stored only in company-approved cloud storage (Google Drive, AWS S3)
- No data on local laptop hard drives (use cloud storage with access controls)
- Encryption required for any data in transit (TLS, VPN)
- Do not email or Slack Confidential/Restricted data (use secure file sharing links)

### Responsibilities

- Minimize data exports (export only what you need, not entire database)
- Delete data when project complete (follow retention policies)
- Do not store data on personal devices or accounts
- Shred or securely delete physical printouts

## Customer Data Requests

### GDPR Data Subject Requests

- Customers have right to access, rectify, erase, or port their data
- Forward requests to legal/security team (do not respond directly)
- Respond within 30 days (GDPR requirement)

### Support Access

- Customer success/support may access customer data to resolve support tickets
- Access must be tied to specific ticket/case
- Do not proactively browse customer accounts
- Log access in ticketing system

## Employee Data

### Requirements

- Employee data (HR records, payroll, performance reviews) restricted to HR team
- Managers may access direct report data only
- Do not access your own HR data through backend systems (use HR portal)

### Responsibilities

- Treat employee data with same sensitivity as customer data
- Do not gossip or share employee data inappropriately

## Data Anonymization and Masking

### Requirements

- Use anonymized or synthetic data for development and testing
- Mask PII in non-production environments (email → fake email, names → random names)
- Redact sensitive fields in logs (passwords, credit cards, SSNs)

### Responsibilities

- Prefer anonymized datasets for analytics where possible
- Review queries and reports to ensure no accidental PII exposure
- Test anonymization to ensure re-identification not possible

## Third-Party Data Sharing

### Requirements

- Sharing customer data with third parties (vendors, partners) requires Security and Legal approval
- Data Processing Agreement (DPA) required before sharing
- Share minimum data necessary
- Ensure third party has adequate security controls (SOC 2, ISO 27001)

### Responsibilities

- Document all third-party data sharing (what data, why, which vendor)
- Verify vendor on approved vendor list (see VEN-01)
- Monitor vendor for security incidents or breaches

## Data Breach Response

### Requirements

- Report suspected unauthorized data access immediately (security@company.com)
- Do not delete evidence (logs, queries, emails)
- Follow data-breach-response-process.md

**Reportable incidents:**
- Accidental email to wrong recipient (customer data)
- Misconfigured database or S3 bucket (public access)
- Compromised credentials with data access
- Ransomware or data theft
- Unauthorized access by employee or contractor

### Responsibilities

- When in doubt, report it (false positives better than missing real breach)
- Preserve evidence for investigation
- Do not discuss breach publicly (including social media)

## Monitoring and Auditing

### Automated Monitoring

- All database queries logged with user ID and timestamp
- Automated alerts for suspicious activity:
  - Large data exports (>10,000 rows)
  - Access to sensitive tables (payment, health, credentials)
  - Queries outside business hours
  - Access from unusual locations

### Audit Reviews

- Security team reviews data access logs monthly
- Quarterly access reviews with manager certification
- Random sampling of queries for compliance check

## Training

- Complete data privacy training during onboarding
- Annual GDPR/CCPA training for roles with data access
- Annual review of this policy

## Exceptions

Requests for exceptions require written approval from Security Team Lead and Data Protection Officer with business justification. Exceptions reviewed quarterly.

## Related Documents

- Standards: data-classification-standard.md, data-retention-standard.md, cryptography-standard.md
- Processes: access-review-process.md, data-breach-response-process.md
- Controls: DAT-01, DAT-04, ACC-03

## References

- GDPR Article 5 (Principles of data processing)
- GDPR Article 32 (Security of processing)
- CCPA: https://oag.ca.gov/privacy/ccpa

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Data Classification](../controls/data-management/data-classification.md) ^[Four-tier classification with access principles: least privilege, need-to-know, purpose limitation]
- [Customer Personal Data](../controls/data-privacy/customer-personal-data.md) ^[GDPR data subject requests (access, rectify, erase, port), respond within 30 days, support access tied to tickets]
- [Employee Personal Data](../controls/data-privacy/employee-personal-data.md) ^[Employee data restricted to HR team, managers access direct reports only, do not access own HR data through backend]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Access granted based on job role and specific business need, elevated access requires justification]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Quarterly access reviews ensure least privilege, manager certification required, enhanced monitoring for Restricted data]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Production database access restricted to on-call engineers, Security Team approval for Restricted data access]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[Downloaded data stored in approved cloud storage only, no local laptop hard drives]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[Encryption required for data in transit (TLS, VPN), do not email or Slack Confidential/Restricted data]
- [Data Retention and Deletion](../controls/data-management/data-retention-and-deletion.md) ^[Delete data when project complete, follow retention policies, data minimization required]
- [Cloud Data Inventory](../controls/data-management/cloud-data-inventory.md) ^[All database queries logged with user ID and timestamp for audit trails]
- [Data Breach Response](../controls/incident-response/data-breach-response.md) ^[Report suspected unauthorized data access immediately, preserve evidence, follow breach response process]
- [Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md) ^[Automated alerts for large data exports, access to sensitive tables, unusual access patterns]

---

<!-- Backlinks auto-generated below -->
