# PEO-03: Offboarding
**Category: **People Security
  
## Objective
Protect company assets during employee departure.
  
## Description
Access is revoked immediately upon termination. Company property is returned. Exit interviews cover confidentiality and data handling obligations. Terminated employee accounts are monitored.
  
## Implementation Guidance
**Immediate Access Revocation**: HR notifies IT of termination. SCIM automatically disables SSO account within 1 hour. AWS, GitHub, other access removed.
  
**Property Return**: Employee returns laptop, Yubikey, badges. Equipment wiped and returned to inventory.
  
**Exit Process**: Manager and HR complete offboarding checklist. Exit interview covers non-disclosure agreement and return of confidential data.
  
**Monitoring**: Terminated employee accounts monitored for 30 days for attempted access. Alerts escalated to security team.
  
  
## Examples of Good Implementation
- Terminated employee account disabled in Okta within 30 minutes of HR notification
- Returned MacBook wiped via MDM remote wipe command, FileVault recovery key used
- Exit interview checklist completed for all voluntary and involuntary terminations
- Attempted login by terminated employee blocked and security team notified
  
## Audit Evidence
- Offboarding procedure
- Termination and access revocation logs
- Exit interview documentation
- Equipment return records
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.3](../soc2/cc63.md)
  