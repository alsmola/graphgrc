# ACC-01: Identity & Authentication
  
**Category: **Access Control
  
## Objective
Ensure all users are uniquely identified and authenticated using strong, phishing-resistant methods.
  
## Description
All access to systems requires authentication using WebAuthn/passkeys or SSO with MFA. Password-only authentication is not permitted for any production systems.
  
## Implementation Guidance
**User Authentication**: Okta or Google Workspace for SSO with MFA required. WebAuthn/passkeys enforced for all users. AWS IAM Identity Center for cloud access.
  
**No Passwords**: No service account passwords - use IAM roles or workload identity instead.
  
**Access Methods**: SSO login for all SaaS tools. AWS access via SSO only (no long-lived credentials). GitHub protected by SSO + WebAuthn. API keys rotated every 90 days.
  
  
## Examples of Good Implementation
- All employees use Yubikeys for WebAuthn authentication
- AWS access requires SSO through Okta with MFA
- Password-only authentication disabled for all production systems
- Service accounts use IAM roles instead of credentials
  
## Audit Evidence
- SSO configuration showing MFA enforcement
- User directory with MFA enrollment status
- AWS IAM policy requiring SSO
- Access logs showing authentication methods
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.1](../soc2/cc61.md)
- [CC6.2](../soc2/cc62.md)
- [CC6.3](../soc2/cc63.md)
  