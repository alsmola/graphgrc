---
type: policy
title: Engineer Security Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: engineers
---

# Engineer Security Policy

Security requirements for engineers with code and infrastructure access.

## Extends

All requirements from Employee Security Policy plus:

## Secure Coding

- Follow secure coding standards
- No secrets in code repositories
- Use Secrets Manager for credentials
- Input validation and output encoding
- Parameterized queries (prevent SQL injection)

## Code Review

- All code reviewed by peer before merge
- Security review for high-risk changes
- SAST/DAST scans must pass

## Access Control

- Least privilege access to production
- MFA required for cloud console access
- Just-in-time access where possible
- No shared accounts

## Production Data

- Minimize access to production data
- Never copy production data to local machine
- Use approved tools for database access
- Log all production data access

## Third-Party Dependencies

- Review dependencies before adding
- Keep dependencies up to date
- Scan for known vulnerabilities
- Document license compatibility

## Infrastructure Changes

- Use Infrastructure as Code (IaC)
- Peer review for infrastructure changes
- Test in non-production first
- Follow change management process

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Secure Coding Standards](../controls/security-engineering/secure-coding-standards.md) ^[Follow secure coding standards, input validation, parameterized queries]
- [Secure Code Review](../controls/security-engineering/secure-code-review.md) ^[All code reviewed by peer before merge, security review for high-risk changes]
- [Automated Code Analysis](../controls/security-engineering/automated-code-analysis.md) ^[SAST/DAST scans must pass before merge]
- [Secrets Management](../controls/iam/secrets-management.md) ^[No secrets in code repositories, use Secrets Manager for credentials]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[MFA required for cloud console access, just-in-time access where possible, log all production data access]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA required for cloud console and production access]
- [Change Management](../controls/operational-security/change-management.md) ^[Use Infrastructure as Code, peer review for infrastructure changes, test in non-production first]
