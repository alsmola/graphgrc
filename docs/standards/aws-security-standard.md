---
type: standard
title: AWS Security Standard
owner: infrastructure-team
last_reviewed: 2025-01-09
review_cadence: quarterly
applies_to: [engineers, infrastructure-team]
---

# AWS Security Standard

This standard defines baseline security configurations for all AWS resources.

## Scope

Applies to all AWS accounts in the organization, including production, staging, and development environments.

## Requirements

### Account Security

- Enable MFA on root account, store credentials in vault
- Use AWS Organizations with Service Control Policies (SCPs)
- Enable CloudTrail in all regions, logs to centralized S3 bucket
- Enable AWS Config for compliance monitoring
- Use IAM Identity Center (AWS SSO) for human access, no long-lived IAM user credentials

### Network Security

- Default deny all inbound traffic on security groups
- No publicly accessible RDS instances
- Use VPC endpoints for AWS services where possible
- Enable VPC Flow Logs for all VPCs

### Data Protection

- Encrypt all S3 buckets at rest (SSE-S3 or SSE-KMS)
- Enable S3 Block Public Access at account level
- Encrypt all EBS volumes
- Encrypt all RDS instances with KMS
- Enable encryption in transit (TLS 1.2+ only)

### IAM and Access Control

- Use role-based access with least privilege
- No wildcard (*) permissions in production
- Require MFA for privileged actions
- IAM roles must have maximum session duration ≤ 12 hours
- Tag all resources with Owner, Environment, DataClassification

### Logging and Monitoring

- Enable CloudTrail API logging for all regions
- Forward logs to centralized security account
- Enable GuardDuty for threat detection
- Alert on critical security events (root login, IAM policy changes, security group changes)

### Compliance and Auditing

- Use AWS Config rules to enforce standards
- Quarterly access reviews of IAM roles and policies
- Automated compliance scanning with open-source tools (Prowler, ScoutSuite)

---
## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [ACC-01: Identity & Authentication](../custom/acc-01.md) ^[IAM Identity Center for cloud access with MFA and SSO]
- [ACC-02: Least Privilege & RBAC](../custom/acc-02.md) ^[IAM policies with least privilege, no wildcard permissions in production]
- [ACC-03: Access Reviews](../custom/acc-03.md) ^[Quarterly IAM role and policy access reviews]
- [ACC-04: Privileged Access Management](../custom/acc-04.md) ^[Root account MFA with hardware token stored in vault, CloudTrail logging]
- [DAT-02: Encryption](../custom/dat-02.md) ^[S3 encryption at rest (SSE-S3/SSE-KMS), RDS encryption with KMS, TLS 1.2+ in transit]
- [INF-01: Cloud Security Configuration (AWS)](../custom/inf-01.md) ^[VPC configuration, security groups default deny, VPC Flow Logs enabled]
- [INF-02: Network Security](../custom/inf-02.md) ^[No publicly accessible RDS, VPC endpoints for AWS services]
- [INF-03: Logging & Monitoring](../custom/inf-03.md) ^[CloudTrail in all regions, GuardDuty enabled, centralized logging to S3]