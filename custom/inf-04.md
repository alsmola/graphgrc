# INF-04: Backup & Recovery
**Category: **Infrastructure Security
  
## Objective
Ensure business continuity through reliable backup and recovery capabilities.
  
## Description
Critical systems and data are backed up regularly. Backups are encrypted and tested. Disaster recovery procedures are documented and tested annually.
  
## Implementation Guidance
**Database Backups**: RDS automated backups daily with 30-day retention. Manual snapshots before major changes.
  
**Infrastructure Backups**: Terraform state backed up. AMI snapshots of critical EC2 instances. S3 versioning enabled for application data.
  
**Backup Testing**: Quarterly restore test from backup to verify recovery. Document restore time and success.
  
**DR Plan**: Written disaster recovery plan tested annually. Defines RTO (4 hours) and RPO (1 hour) targets.
  
  
## Examples of Good Implementation
- RDS production database has automated daily backups retained 30 days
- Q4 2024 backup restore test successfully restored production database in 45 minutes
- S3 versioning enabled on all production buckets with MFA delete protection
- Annual DR tabletop exercise completed with documented findings
  
## Audit Evidence
- Backup configuration showing schedule and retention
- Quarterly backup restore test results
- Disaster recovery plan document
- Annual DR exercise documentation
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [A1.2](../soc2/a12.md)
- [CC9.1](../soc2/cc91.md)
  