---
type: standard
id: standard-data-classification
title: Data Classification Standard
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: [all-employees]
---

# Data Classification Standard

Defines how to classify data based on sensitivity and required protection levels.

## Scope

All data created, processed, stored, or transmitted by the organization.

## Classification Levels

### Public

**Definition:** Information intended for public consumption.

**Examples:** Marketing materials, published blog posts, public documentation

**Requirements:**
- No access restrictions required
- Can be shared freely

### Internal

**Definition:** Information for internal business use, not sensitive.

**Examples:** Project plans, internal wikis, company announcements, source code

**Requirements:**
- Accessible to employees only
- Do not share outside the organization without approval
- OK to store in SaaS tools (Slack, Google Workspace)

### Confidential

**Definition:** Sensitive business or customer information that could cause harm if disclosed.

**Examples:** Customer PII (names, emails, addresses), financial data, contracts, security assessments, non-public product roadmaps

**Requirements:**
- Encrypt at rest and in transit
- Access logged and monitored
- Access based on role/need-to-know
- Cannot be stored on local laptops (use cloud storage only)
- Do not share in Slack/email without encryption
- Annual access reviews required

### Restricted

**Definition:** Highly sensitive data with regulatory requirements or severe impact if disclosed.

**Examples:** Payment card data (PCI), health information (HIPAA), passwords/secrets, cryptographic keys, social security numbers, authentication tokens

**Requirements:**
- All Confidential requirements plus:
- Encrypt with KMS customer-managed keys
- MFA required for access
- Quarterly access reviews
- Cannot be logged or transmitted to third-party services
- Must be stored in approved systems only (no general-purpose databases)

## Labeling Requirements

- AWS resources: Use `DataClassification` tag
- S3 buckets: Bucket name or tag indicates classification
- Documentation: Header or filename indicates classification
- Databases: Schema/table naming conventions

## References

- Related controls: DAT-01, DAT-02, DAT-03
- Related policies: baseline-security-policy.md

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Data Classification](../controls/data-management/data-classification.md) ^[Four-tier classification: Public, Internal, Confidential, Restricted with specific protection requirements for each level]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[Confidential and Restricted data must be encrypted at rest with KMS customer-managed keys for Restricted]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[Confidential and Restricted data must be encrypted in transit]
- [Key Management](../controls/cryptography/key-management.md) ^[Restricted data requires customer-managed KMS keys with separate keys per environment]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Access to Confidential and Restricted data based on role and need-to-know]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Access to Confidential data reviewed annually, Restricted data quarterly to enforce least privilege]
- [Cloud Data Inventory](../controls/data-management/cloud-data-inventory.md) ^[AWS resources tagged with DataClassification for inventory tracking]
- [SaaS Data Inventory](../controls/data-management/saas-data-inventory.md) ^[Data classification applied to SaaS tool data storage]

---

<!-- Backlinks auto-generated below -->
