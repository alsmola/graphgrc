---
type: policy
title: IT Administrator Security Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: it-administrators
---

# IT Administrator Security Policy

Security requirements for IT administrators with privileged access to corporate systems.

## Extends

All requirements from Employee Security Policy plus:

## Privileged Access

- Use separate admin account for privileged operations
- MFA required for all admin access
- Just-in-time privileged access where possible
- Admin sessions monitored and logged

## Account Management

- Provision access based on role and approval
- Review access quarterly
- Deprovision immediately upon termination
- Follow least privilege principle

## SaaS Administration

- Configure MFA enforcement for all users
- Enable SSO where possible
- Configure security logging
- Review and harden application settings
- Monitor for unauthorized configuration changes

## Endpoint Management

- Enroll all devices in MDM
- Enforce disk encryption
- Deploy security agents (EDR, antivirus)
- Enforce patch management policies
- Remote wipe for lost/stolen devices

## Password Management

- Do not reuse admin passwords
- Rotate service account passwords quarterly
- Store admin credentials in approved vault
- Never share admin credentials

## Change Management

- Test changes in non-production first
- Document changes in ticketing system
- Follow change approval process for production
- Have rollback plan for all changes

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Separate admin account for privileged operations, just-in-time access, all admin sessions monitored and logged]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA required for all admin access]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[IT administrators review privileged access quarterly, deprovision immediately upon termination]
- [SaaS IAM](../controls/iam/saas-iam.md) ^[Configure MFA enforcement, enable SSO, configure security logging, monitor for unauthorized config changes]
- [SaaS Hardening](../controls/configuration-management/saas-hardening.md) ^[Review and harden application settings, enable security logging]
- [Device Management (macOS MDM)](../controls/endpoint-security/device-management-macos-mdm.md) ^[Enroll all devices in MDM, enforce disk encryption, deploy EDR agents, enforce patch management, remote wipe capability]
- [Password Management](../controls/iam/password-management.md) ^[Do not reuse admin passwords, store admin credentials in approved vault, never share]
- [Secrets Management](../controls/iam/secrets-management.md) ^[Rotate service account passwords quarterly]
- [Change Management](../controls/operational-security/change-management.md) ^[Test changes in non-production, document in ticketing system, follow approval process, have rollback plan]
