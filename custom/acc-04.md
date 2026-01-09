# ACC-04: Privileged Access Management
  
**Category: **Access Control
  
## Objective
Protect critical systems through enhanced controls on privileged accounts.
  
## Description
Administrative and privileged access is tightly controlled, monitored, and audited. Break-glass procedures exist for emergency access.
  
## Implementation Guidance
**Admin Accounts**: Separate admin accounts (admin@) from regular user accounts. MFA required for all admin access.
  
**AWS Root Account**: Root account MFA enabled with hardware token. Root credentials stored in physical safe. Access requires two executives.
  
**Session Recording**: All privileged sessions recorded using AWS CloudTrail and CloudWatch Logs.
  
**Break Glass**: Emergency access procedures documented. Break-glass account usage triggers alert to security team and CEO.
  
  
## Examples of Good Implementation
- AWS root account credentials locked in company safe, requires CEO + CFO
- All admin actions logged to immutable S3 bucket with CloudTrail
- Engineers use elevated privileges via AWS SSO with automatic 4-hour timeout
- Break-glass account last used 6 months ago during critical outage, fully documented
  
## Audit Evidence
- Privileged account inventory
- AWS CloudTrail logs for admin actions
- Break-glass procedure documentation
- Physical safe access log for root credentials
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.2](../soc2/cc62.md)
- [CC6.8](../soc2/cc68.md)
  