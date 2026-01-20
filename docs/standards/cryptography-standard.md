---
type: standard
id: standard-cryptography
title: Cryptography Standard
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: [engineers, infrastructure-team]
---

# Cryptography Standard

Requirements for encryption at rest, in transit, and cryptographic key management.

## Scope

All systems that store, process, or transmit Confidential or Restricted data.

## Encryption at Rest

### Approved Algorithms

- **Symmetric:** AES-256-GCM (preferred), AES-256-CBC
- **Asymmetric:** RSA 2048+ bits, ECDSA P-256+
- **Hashing:** SHA-256, SHA-512, bcrypt (for passwords)
- **Prohibited:** DES, 3DES, MD5, SHA-1, RC4

### Data Storage Requirements

- AWS S3: SSE-S3 or SSE-KMS
- AWS RDS: Encryption enabled with KMS
- AWS EBS: Encryption enabled
- SaaS applications: Verify encryption at rest in vendor assessment

## Encryption in Transit

### TLS Requirements

- Minimum version: TLS 1.2 (TLS 1.3 preferred)
- Prohibited: SSL 3.0, TLS 1.0, TLS 1.1
- Use managed certificates (AWS ACM, Let's Encrypt)
- Certificate validity ≤ 397 days
- HSTS enabled for all HTTPS endpoints

### API Security

- All APIs must use HTTPS (no plain HTTP in production)
- Internal service-to-service communication uses TLS with mTLS where feasible
- API keys transmitted only in headers (not query params)

## Key Management

### Key Storage

- Use AWS KMS or similar managed key service
- No hardcoded keys in source code
- Application secrets stored in AWS Secrets Manager or similar
- Customer-managed KMS keys for Restricted data
- Automatic key rotation enabled (annual minimum)

### Key Access

- Principle of least privilege for key usage
- Separate keys per environment (prod, staging, dev)
- Log all key usage with CloudTrail

## Certificate Management

- Use managed certificate services (AWS ACM, Let's Encrypt)
- Automated renewal before expiration
- Alert 30 days before certificate expiry
- No self-signed certificates in production

## References

- Related controls: DAT-02, INF-01
- NIST SP 800-175B: Guideline for Using Cryptographic Standards
- OWASP Cryptographic Storage Cheat Sheet

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[AES-256-GCM/CBC algorithms, S3 SSE-S3/SSE-KMS, RDS and EBS encryption with KMS]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[TLS 1.2+ minimum (1.3 preferred), HSTS enabled, managed certificates with automated renewal]
- [Key Management](../controls/cryptography/key-management.md) ^[AWS KMS for key storage, no hardcoded keys, automatic rotation, separate keys per environment]
- [Code Signing](../controls/cryptography/code-signing.md) ^[RSA 2048+ bits for code signing certificates]
- [Cloud Hardening](../controls/configuration-management/cloud-hardening.md) ^[AWS S3 encryption requirements, RDS and EBS encryption standards]

---

<!-- Backlinks auto-generated below -->
