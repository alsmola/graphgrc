---
type: policy
title: HR Administrator Security Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: hr-administrators
---

# HR Administrator Security Policy

Security requirements for HR administrators handling employee personal data.

## Extends

All requirements from Employee Security Policy plus:

## Employee Data Protection

- Access employee PII only when required for HR duties
- Never share employee data externally without authorization
- Use encrypted channels for transmitting employee documents
- Store employee documents in approved HR system only (no local copies)
- Redact sensitive data when sharing documents

## HRIS Administration

- MFA required for HRIS access
- Least privilege access (role-based permissions)
- Log all access to employee records
- Review access permissions quarterly

## Onboarding/Offboarding

- Coordinate with IT for account provisioning/deprovisioning
- Verify identity before provisioning access
- Initiate offboarding process same day as termination
- Ensure all company property returned
- Conduct exit interviews for security awareness

## Background Checks

- Conduct background checks for all new hires before granting access
- Document background check completion
- Follow local regulations for data retention

## Data Subject Requests

- Process employee data subject requests (GDPR/CCPA)
- Respond within regulatory timelines
- Coordinate with Legal and Security teams
- Document request handling

## Confidential Information

- Do not discuss employee matters in public or open channels
- Use private channels for sensitive HR discussions
- Lock HR documents when not actively working on them

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Employee Personal Data](../controls/data-privacy/employee-personal-data.md) ^[Access employee PII only when required, never share externally without authorization, use encrypted channels]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA required for HRIS access]
- [SaaS IAM](../controls/iam/saas-iam.md) ^[HR administrators review HRIS access permissions quarterly, all access to employee records is logged]
- [Personnel Lifecycle Management](../controls/personnel-security/personnel-lifecycle-management.md) ^[Coordinate with IT for account provisioning/deprovisioning, verify identity before provisioning, same-day offboarding initiation]
- [Offboarding](../controls/personnel-security/offboarding.md) ^[Initiate offboarding same day as termination, ensure company property returned, conduct exit interviews]
- [Background Checks](../controls/personnel-security/background-checks.md) ^[Conduct background checks before granting access, document completion, follow local data retention regulations]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[Use encrypted channels for transmitting employee documents]
- [Data Retention and Deletion](../controls/data-management/data-retention-and-deletion.md) ^[Store employee documents in approved HR system only, follow retention regulations]
