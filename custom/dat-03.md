# DAT-03: Data Retention & Deletion
**Category: **Data Protection
  
## Objective
Minimize data retention and enable secure deletion.
  
## Description
Data is retained according to policy and legal requirements. Data is securely deleted when no longer needed. Customers can request deletion of their data.
  
## Implementation Guidance
**Retention Policy**: Application logs retained 90 days. Audit logs retained 7 years. Customer data retained per contract + 90 days.
  
**Automated Deletion**: S3 lifecycle policies automatically delete old data. Automated scripts clean up aged development/test data.
  
**Customer Deletion**: API endpoint allows customers to request data deletion. Deletion completed within 30 days and confirmed.
  
**Backup Retention**: Database backups retained 30 days, then deleted. Long-term archives encrypted and access-controlled.
  
  
## Examples of Good Implementation
- S3 lifecycle policy deletes CloudTrail logs older than 7 years
- Customer data deletion requests processed via ticketing system with audit trail
- Development environments automatically wipe test data after 90 days
- Deleted customer data verified absent from all systems including backups
  
## Audit Evidence
- Data retention policy
- S3 lifecycle policies
- Customer deletion request logs
- Backup retention settings
  
---
  
## Mapped framework controls
### GDPR
- [Art 17](../gdpr/art17.md)
- [Art 5](../gdpr/art5.md)
  
### SOC 2
- [CC6.5](../soc2/cc65.md)
  