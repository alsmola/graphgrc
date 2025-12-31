# VEN-02: Vendor Contracts & DPAs
**Category: **Vendor Management
  
## Objective
Ensure vendors meet security and privacy obligations through contractual controls.
  
## Description
Vendor contracts include security, privacy, and compliance requirements. Data Processing Agreements (DPAs) are executed with vendors processing customer data. Vendor compliance is monitored.
  
## Implementation Guidance
**Contract Requirements**: All vendor contracts reviewed by legal and security. Include security standards, SLA, audit rights, termination clause.
  
**DPAs**: DPAs executed with any vendor processing customer personal data (GDPR requirement). Standard DPA template approved by legal.
  
**SLA Monitoring**: Monitor vendor SLAs for availability, incident notification, data deletion. Escalate breaches to vendor management.
  
**Contract Repository**: Central repository (DocuSign, Ironclad) for vendor contracts and DPAs. Track expiration and renewal dates.
  
  
## Examples of Good Implementation
- AWS DPA executed and covers all regions where customer data resides
- Support ticketing system vendor signed DPA before handling customer PII
- Contract repository shows 100% of high-risk vendors have executed DPAs
- Vendor missed SLA for incident notification, escalated and process improved
  
## Audit Evidence
- Vendor contract templates
- DPA template and executed DPAs
- Contract repository/register
- SLA monitoring and escalation records
  
---
  
## Mapped framework controls
### GDPR
- [Art 28](../gdpr/art28.md)
  
### SOC 2
- [CC9.2](../soc2/cc92.md)
  