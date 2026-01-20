---
type: policy
title: Product Administrator Security Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: product-administrators
---

# Product Administrator Security Policy

Security requirements for product administrators with customer data access.

## Extends

All requirements from Employee Security Policy plus:

## Customer Data Access

- Access customer data only when necessary for support/troubleshooting
- Log all customer data access (who, what, when, why)
- Use approved tools for customer data access (no direct database queries)
- Never copy customer data to local machine
- Redact PII when creating bug reports or documentation

## Support Operations

- Verify customer identity before accessing account
- Use read-only access unless write access required
- Time-box support sessions (close access when done)
- Document all actions taken in customer account
- Obtain customer consent for data access when required

## Data Privacy

- Understand GDPR/CCPA requirements for customer data
- Process data subject requests (access, deletion, portability)
- Respond to requests within regulatory timelines
- Coordinate with Legal for complex requests

## Third-Party Tools

- Only use approved tools for customer interaction
- Do not paste customer data into unapproved tools (ChatGPT, etc.)
- Ensure third-party tools have appropriate security controls
- Review data processing agreements

## Incident Response

- Report suspected data breaches immediately
- Do not disclose breach information publicly without authorization
- Follow breach notification process
- Coordinate with Security team for customer communications

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Customer Personal Data](../controls/data-privacy/customer-personal-data.md) ^[Access customer data only when necessary, verify identity before access, obtain consent when required, process data subject requests within timelines]
- [Data Classification](../controls/data-management/data-classification.md) ^[Never copy customer data to local machine, redact PII in bug reports and documentation]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Use read-only access unless write required, time-box support sessions]
- [Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md) ^[Log all customer data access (who, what, when, why), document actions in customer account]
- [Data Breach Response](../controls/incident-response/data-breach-response.md) ^[Report suspected data breaches immediately, do not disclose publicly without authorization, follow breach notification process]
- [SaaS Hardening](../controls/configuration-management/saas-hardening.md) ^[Only use approved tools for customer interaction, ensure third-party tools have appropriate security controls]
- [Vendor Risk Management](../controls/risk-management/vendor-risk-management.md) ^[Do not paste customer data into unapproved tools, review data processing agreements for third-party tools]
