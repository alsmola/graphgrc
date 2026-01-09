# DAT-02: Encryption
  
**Category: **Data Protection
  
## Objective
Protect data confidentiality through cryptographic controls.
  
## Description
All data is encrypted in transit using TLS 1.2+. Sensitive data is encrypted at rest using AES-256. Encryption keys are managed through AWS KMS.
  
## Implementation Guidance
**In Transit**: All external APIs use HTTPS with TLS 1.2+. Internal services use TLS for inter-service communication. No plaintext protocols.
  
**At Rest**: S3 buckets use SSE-KMS encryption. RDS databases use encryption at rest. EBS volumes encrypted.
  
**Key Management**: AWS KMS for encryption keys. Keys rotated annually. Access to keys controlled via IAM.
  
**Endpoints**: macOS FileVault full disk encryption required on all employee devices.
  
  
## Examples of Good Implementation
- All S3 buckets have default encryption enabled with AWS KMS
- RDS instances configured with encryption at rest using customer managed KMS keys
- Application enforces TLS 1.2 minimum, TLS 1.0/1.1 disabled
- All employee MacBooks have FileVault enabled and verified quarterly
  
## Audit Evidence
- S3 bucket encryption settings
- RDS encryption configuration
- TLS configuration for load balancers/applications
- MDM reports showing FileVault status on all devices
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.1](../soc2/cc61.md)
- [CC6.7](../soc2/cc67.md)
  