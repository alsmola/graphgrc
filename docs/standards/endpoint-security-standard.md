---
type: standard
id: standard-endpoint-security
title: Endpoint Security Standard
owner: it-team
last_reviewed: 2025-01-09
review_cadence: quarterly
applies_to: [all-employees]
---

# Endpoint Security Standard

Baseline security requirements for employee endpoints (macOS laptops).

## Scope

All company-issued and BYOD laptops used to access company resources.

## Requirements

### Device Management

- All endpoints enrolled in MDM (Jamf, Kandji, Fleet)
- Company-owned devices provisioned with standard image
- BYOD devices must meet minimum security requirements

### Operating System

- macOS only (no Windows, Linux, or ChromeOS without exception)
- Latest stable macOS version or previous major version (N-1)
- Automatic updates enabled for security patches
- Critical security updates installed within 7 days

### Encryption

- FileVault full-disk encryption enabled
- Recovery key escrowed in MDM
- No unencrypted external drives containing Confidential data

### Authentication

- Strong password required (12+ characters)
- Password changes on macOS user account trigger company password reset
- Screen lock after 5 minutes of inactivity
- Biometric unlock (Touch ID) permitted

### Endpoint Protection

- Endpoint Detection and Response (EDR) agent installed (CrowdStrike, SentinelOne, or similar)
- Real-time malware scanning enabled
- No unauthorized system extensions or kernel modifications
- Firewall enabled

### Software Management

- Approved software list maintained by IT
- Software installation requires admin approval (standard users non-admin)
- Homebrew allowed for engineering team with restrictions on casks
- Quarterly software inventory and cleanup

### Network Security

- Default deny untrusted networks
- VPN required for accessing internal resources from untrusted networks
- No direct connection to production systems from public WiFi without VPN

### Data Loss Prevention

- No Confidential or Restricted data stored on local disk (use cloud storage)
- USB device restrictions (read-only or blocked)
- Screenshot/recording tools monitored in sensitive applications

## BYOD Requirements

If allowing BYOD (approved by security team):
- Separate user profile for work apps
- Work email/Slack/GitHub in containerized apps only
- Remote wipe capability for work data
- No access to production systems

## Lost/Stolen Device Response

- Report to IT immediately
- Remote lock initiated within 1 hour
- Remote wipe after 24 hours if not recovered
- Password reset on all company accounts

## References

- Related controls: END-01, END-02, END-03, DAT-01
- Related process: device-provisioning-process.md (if exists)

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Device Management (macOS MDM)](../controls/endpoint-security/device-management-macos-mdm.md) ^[All endpoints enrolled in MDM (Jamf, Kandji, Fleet) with standard image provisioning and configuration management]
- [Endpoint Protection](../controls/endpoint-security/endpoint-protection.md) ^[EDR agent installed (CrowdStrike, SentinelOne) with real-time malware scanning and firewall enabled]
- [Software Updates](../controls/endpoint-security/software-updates.md) ^[Automatic macOS security updates enabled, critical patches within 7 days, latest or N-1 macOS version required]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[FileVault full-disk encryption enabled with recovery key escrowed in MDM]
- [Password Management](../controls/iam/password-management.md) ^[Strong password required (12+ characters), screen lock after 5 minutes, biometric unlock permitted]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA enforced through device-level security and SSO integration]
- [Endpoint Network Security](../controls/network-security/endpoint-network-security.md) ^[Firewall enabled, VPN required for internal resource access from untrusted networks]
- [Endpoint Hardening](../controls/configuration-management/endpoint-hardening.md) ^[Standard users non-admin, software installation requires approval, USB restrictions, no unauthorized kernel modifications]
- [Endpoint Inventory](../controls/asset-management/endpoint-inventory.md) ^[All endpoints tracked in MDM for inventory management, quarterly software inventory and cleanup]

---

<!-- Backlinks auto-generated below -->
