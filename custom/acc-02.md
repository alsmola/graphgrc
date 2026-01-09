# ACC-02: Least Privilege & RBAC
**Category: **Access Control
  
## Objective
Minimize risk by ensuring users only have access needed for their role.
  
## Description
Access to systems and data is granted based on job function using role-based access control. Users receive minimum necessary permissions. Production access requires additional approval.
  
## Implementation Guidance
**RBAC Model**: Define roles for Engineering, Support, Admin, etc. Map users to roles in identity provider.
  
**AWS Access**: Use AWS SSO permission sets tied to job functions. No direct IAM user access. Separate read-only and admin roles.
  
**Production Access**: Requires manager approval. Time-limited sessions using AWS SSO or just-in-time access tools.
  
**Service Accounts**: Use AWS IAM roles with scoped policies. No broad wildcard permissions.
  
  
## Examples of Good Implementation
- Engineers have read-only production access by default
- Admin access to production requires manager approval and expires after 8 hours
- AWS IAM roles follow principle of least privilege with no wildcard (*) permissions
- Support team has limited read access to customer data based on support case
  
## Audit Evidence
- RBAC role definitions and mappings
- AWS IAM policies showing least privilege
- Production access approval logs
- Access review documentation
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.1](../soc2/cc61.md)
- [CC6.2](../soc2/cc62.md)
- [CC6.3](../soc2/cc63.md)
  