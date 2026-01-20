---
type: policy
title: Employee Security Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: all-employees
---

# Employee Security Policy

Baseline security requirements for all employees.

## Account Security

- Use strong passwords (12+ characters)
- Enable MFA on all company accounts
- Never share credentials
- Use approved password manager only

## Data Handling

- Classify and handle data appropriately
- No Confidential data on local devices
- No customer data shared externally without authorization
- Report suspected data breaches immediately

## Device Security

- Use company-issued or MDM-enrolled devices
- Enable disk encryption
- Install security updates within 7 days
- Lock screen after 5 minutes
- Report lost/stolen devices immediately

## Network Security

- Use VPN for internal resources on untrusted networks
- No production access from public WiFi without VPN
- Use secure WiFi only (WPA2/WPA3)

## Email Security

- Watch for phishing (unexpected links, urgent requests)
- Verify sensitive requests through secondary channel
- Report phishing to security team

## Physical Security

- Lock screen when away from device
- Don't expose sensitive information in public
- Badge required for office access

## Training

- Complete annual security awareness training
- Complete role-specific training as assigned

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Password Management](../controls/iam/password-management.md) ^[Strong passwords (12+ characters), approved password manager only, never share credentials]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA enabled on all company accounts]
- [Data Classification](../controls/data-management/data-classification.md) ^[Classify and handle data appropriately, no Confidential data on local devices]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[Enable FileVault disk encryption on macOS devices]
- [Device Management (macOS MDM)](../controls/endpoint-security/device-management-macos-mdm.md) ^[Use company-issued or MDM-enrolled devices, report lost/stolen immediately]
- [Software Updates](../controls/endpoint-security/software-updates.md) ^[Install security updates within 7 days]
- [Endpoint Network Security](../controls/network-security/endpoint-network-security.md) ^[Use VPN for internal resources on untrusted networks, secure WiFi only (WPA2/WPA3)]
- [Security Awareness Training](../controls/security-training/security-awareness-training.md) ^[Complete annual security awareness training and role-specific training]
- [Office Security](../controls/physical-protection/office-security.md) ^[Badge required for office access, lock screen when away from device]
- [Rules of Behavior](../controls/personnel-security/rules-of-behavior.md) ^[Employee Security Policy defines rules of behavior: strong passwords, MFA, data classification, device security, VPN usage, annual training]
