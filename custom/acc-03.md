# ACC-03: Access Reviews
  
**Category: **Access Control
  
## Objective
Ensure access remains appropriate and remove unnecessary permissions.
  
## Description
User access rights are reviewed quarterly. Terminated employees have access revoked immediately. Role changes trigger access recertification.
  
## Implementation Guidance
**Quarterly Reviews**: Managers review team access to AWS, GitHub, production systems. Document reviews in ticketing system.
  
**Automated Reports**: Generate quarterly access reports from SSO and AWS IAM Identity Center showing user permissions.
  
**Deprovisioning**: Automated employee offboarding removes all access within 1 hour of termination.
  
**Role Changes**: Transfer or promotion triggers access review within 5 business days.
  
  
## Examples of Good Implementation
- Q1 2025 access review completed with all managers certifying team permissions
- SCIM integration automatically provisions/deprovisions users in Okta
- GitHub organization access reviewed quarterly with inactive members removed
- AWS access report shows no users with permissions exceeding their role
  
## Audit Evidence
- Quarterly access review records
- Manager approval documentation
- Deprovisioning logs
- Before/after snapshots of user permissions
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.3](../soc2/cc63.md)
  