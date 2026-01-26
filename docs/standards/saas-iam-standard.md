---
type: standard
id: standard-saas-iam
title: SaaS IAM Standard
owner: it-team
last_reviewed: 2025-01-09
review_cadence: quarterly
applies_to: [it-team, managers]
---

# SaaS IAM Standard

Identity and access management requirements for SaaS applications.

## Scope

All third-party SaaS applications used by employees (Slack, GitHub, AWS, Google Workspace, etc.).

## Requirements

### Single Sign-On (SSO)

- All SaaS applications must support SSO integration (SAML/OIDC)
- Use centralized identity provider (Okta, Google Workspace, Azure AD)
- Provision users via SSO, no local accounts
- Exceptions require security team approval (document in vendor assessment)

### Multi-Factor Authentication (MFA)

- MFA required for all SaaS applications
- Enforced at IdP level (not application level)
- Acceptable factors: Authenticator app (TOTP), hardware keys (FIDO2/WebAuthn)
- Prohibited: SMS, email-based OTP (unless no other option available)

### Provisioning and Deprovisioning

- Automated user provisioning via SCIM where supported
- For non-SCIM apps: API-based automation or manual provisioning documented
- Deprovisioning triggered by HR offboarding, completed within 1 hour
- Quarterly access reviews to identify orphaned accounts

### Access Control

- Role-based access control (RBAC) configured in each SaaS app
- Default to least privilege (Viewer/Read-only)
- Elevated permissions require manager approval
- Admin accounts limited to IT/Security teams

### Session Management

- Maximum session lifetime: 12 hours for standard users, 1 hour for admins
- Re-authenticate for sensitive actions (payment, config changes)
- Idle timeout: 30 minutes

### Audit Logging

- Enable audit logging in all SaaS applications
- Forward logs to centralized SIEM where possible
- Retain logs for minimum 1 year (2 years for SOC 2 compliance)
- Monitor for anomalous access: unusual location, failed auth attempts, permission changes

## Inventory Management

- Maintain inventory of all approved SaaS applications (IT asset management system)
- Shadow IT detection via SSO logs and network monitoring
- Quarterly review of SaaS inventory

## References

- Related controls: ACC-01, ACC-02, ACC-03, PEO-03
- Related process: access-provisioning-process.md, access-review-process.md

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [SaaS IAM](../controls/iam/saas-iam.md) ^[All SaaS apps must support SSO (SAML/OIDC), automated provisioning via SCIM, role-based access control]
- [Single Sign-On](../controls/iam/single-sign-on.md) ^[Centralized IdP (Okta, Google Workspace, Azure AD), no local accounts, provision users via SSO]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA required for all SaaS apps enforced at IdP level, authenticator app or hardware keys, no SMS]
- [Identity & Authentication](../controls/iam/identity-authentication.md) ^[SSO integration (SAML/OIDC) mandatory, MFA enforced centrally, session management (12hr standard, 1hr admin)]
- [SaaS IAM](../controls/iam/saas-iam.md) ^[Quarterly access reviews identify orphaned accounts in SaaS applications, audit logs monitor anomalous access]
- [Offboarding](../controls/personnel-security/offboarding.md) ^[Automated deprovisioning via SCIM completed within 1 hour of HR offboarding trigger]
- [SaaS Inventory](../controls/asset-management/saas-inventory.md) ^[Maintain inventory in IT asset management system, shadow IT detection, quarterly inventory review]
- [SaaS Hardening](../controls/configuration-management/saas-hardening.md) ^[Audit logging enabled in all SaaS apps, logs forwarded to SIEM, 2-year retention for SOC 2]
- [SaaS Threat Detection](../controls/threat-detection/saas-threat-detection.md) ^[Monitor for anomalous access patterns: unusual location, failed auth attempts, permission changes]

---

<!-- Backlinks auto-generated below -->
