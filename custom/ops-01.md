# OPS-01: Change Management
  
**Category: **Operational Security
  
## Objective
Minimize risk from production changes through controlled processes.
  
## Description
Changes to production systems follow a defined process. Changes are reviewed, tested, and approved. Emergency changes are documented after the fact. Rollback procedures are in place.
  
## Implementation Guidance
**Change Process**: All production changes require GitHub pull request with peer review. Terraform changes require approval from senior engineer.
  
**Testing**: Changes deployed to staging environment first. Automated tests must pass. Manual QA sign-off for risky changes.
  
**Change Window**: Standard changes deployed during business hours. High-risk changes during maintenance window with customer notice.
  
**Emergency Changes**: Allowed for critical security/availability issues. Post-mortem required within 48 hours.
  
  
## Examples of Good Implementation
- All infrastructure changes require Terraform PR with two approvals
- Application deployed to staging, passes automated tests, then promoted to production
- Database schema change tested in staging, deployed during maintenance window
- Emergency patch deployed for critical vulnerability, post-mortem completed next day
  
## Audit Evidence
- Change management procedure
- GitHub pull request history showing reviews and approvals
- Deployment logs with timestamps
- Emergency change post-mortems
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC8.1](../soc2/cc81.md)
  