# DAT-01: Data Classification
**Category: **Data Protection
  
## Objective
Ensure appropriate protection based on data sensitivity.
  
## Description
All data is classified as Public, Internal, Confidential, or Restricted. Handling requirements are defined for each classification level.
  
## Implementation Guidance
**Classification Levels**: Public (marketing), Internal (business docs), Confidential (customer PII), Restricted (payment data, PHI).
  
**Labeling**: Sensitive data stored in dedicated S3 buckets/RDS databases with classification tags.
  
**Handling Rules**: Restricted data requires encryption at rest and in transit. Access logged and monitored. Cannot be stored on endpoints.
  
**Training**: Annual data classification training for all employees.
  
  
## Examples of Good Implementation
- Customer PII stored in S3 bucket tagged 'DataClassification=Confidential'
- No Restricted or Confidential data permitted in Slack or email
- Source code classified as Internal, deployed apps handle Confidential customer data
- Marketing materials classified as Public, customer contracts as Confidential
  
## Audit Evidence
- Data classification policy
- AWS resource tags showing classifications
- Training completion records
- Data inventory with classifications
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.6](../soc2/cc66.md)
- [CC6.7](../soc2/cc67.md)
  