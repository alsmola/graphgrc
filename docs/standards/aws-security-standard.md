---
type: standard
id: standard-aws-security
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
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Cloud IAM](../controls/iam/cloud-iam.md) ^[IAM Identity Center (AWS SSO) for human access, no long-lived IAM credentials, role-based access]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA required on root account and for privileged actions, stored in vault]
- [Single Sign-On](../controls/iam/single-sign-on.md) ^[IAM Identity Center provides SSO for AWS account access]
- [Cloud IAM](../controls/iam/cloud-iam.md) ^[Quarterly access reviews of IAM roles and policies validate least privilege]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Root account MFA with hardware token stored in vault, CloudTrail logging of admin actions]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[S3 buckets encrypted (SSE-S3/SSE-KMS), EBS volumes encrypted, RDS encryption with KMS]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[TLS 1.2+ only for all AWS service communications]
- [Cloud Security Configuration (AWS)](../controls/infrastructure-security/cloud-security-configuration-aws.md) ^[AWS Organizations with SCPs, AWS Config for compliance monitoring, resource tagging requirements]
- [Cloud Network Security](../controls/network-security/cloud-network-security.md) ^[Security groups default deny inbound, VPC Flow Logs enabled, VPC endpoints for AWS services]
- [Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md) ^[CloudTrail in all regions with centralized S3 logging, GuardDuty for threat detection, critical event alerts]
- [Cloud Threat Detection](../controls/threat-detection/cloud-threat-detection.md) ^[GuardDuty enabled for threat detection, alerts on root login and IAM policy changes]
- [Cloud Hardening](../controls/configuration-management/cloud-hardening.md) ^[S3 Block Public Access at account level, no publicly accessible RDS instances]
- [Cloud Inventory](../controls/asset-management/cloud-inventory.md) ^[AWS resource tagging with Owner, Environment, DataClassification for inventory tracking]
- [Capacity Planning](../controls/availability/capacity-planning.md) ^[Auto-scaling groups automatically add capacity during traffic spikes, quarterly capacity trend analysis ensures adequate resources]