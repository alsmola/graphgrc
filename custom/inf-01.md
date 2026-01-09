# INF-01: Cloud Security Configuration (AWS)
  
**Category: **Infrastructure Security
  
## Objective
Maintain secure AWS infrastructure configuration.
  
## Description
AWS infrastructure follows security best practices. Security Groups, NACLs, and IAM policies are configured with least privilege. Infrastructure as Code is used for consistent secure configurations.
  
## Implementation Guidance
**Network Segmentation**: Production VPC separate from development. Public subnets for load balancers, private subnets for application/database.
  
**Security Groups**: Default deny all inbound. Explicit allow rules for necessary traffic. No 0.0.0.0/0 for sensitive ports.
  
**Infrastructure as Code**: Terraform for all infrastructure. Peer review required. Terraform state in encrypted S3 with DynamoDB locking.
  
**AWS Config**: Enabled in all regions. Rules check for security misconfigurations (unencrypted resources, public S3 buckets, etc.).
  
  
## Examples of Good Implementation
- Production RDS databases in private subnet, not internet-accessible
- Security groups allow only necessary ports (443 for HTTPS, 5432 for Postgres)
- AWS Config rule alerts when S3 bucket becomes public
- All infrastructure changes require Terraform PR with security review
  
## Audit Evidence
- Network architecture diagram
- Terraform code repository
- AWS Config compliance dashboard
- Security group rules audit
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.6](../soc2/cc66.md)
- [CC7.2](../soc2/cc72.md)
  