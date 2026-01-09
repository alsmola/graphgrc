# END-02: Endpoint Protection
**Category: **Endpoint Security
  
## Objective
Protect endpoints from malware and data loss.
  
## Description
All endpoints run antivirus/anti-malware software. Full disk encryption is enabled. Endpoint detection and response (EDR) capabilities are deployed.
  
## Implementation Guidance
**Antivirus**: macOS built-in XProtect supplemented with CrowdStrike or SentinelOne for enhanced threat detection.
  
**Full Disk Encryption**: FileVault required on all Mac devices. Verified via MDM. Recovery keys escrowed to MDM.
  
**EDR**: CrowdStrike Falcon or SentinelOne for behavioral detection, threat hunting, and response.
  
**USB Restrictions**: USB storage blocked via MDM policy. Approved devices (Yubikey) allow-listed.
  
  
## Examples of Good Implementation
- CrowdStrike deployed on all employee Macs with real-time protection
- FileVault enabled on 100% of devices, verified weekly via MDM report
- USB storage devices blocked - attempted use generates security alert
- CrowdStrike detected and quarantined malware from phishing email attachment
  
## Audit Evidence
- Antivirus deployment status
- FileVault encryption status from MDM
- EDR agent deployment report
- Malware detection and remediation logs
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.8](../soc2/cc68.md)
- [CC7.2](../soc2/cc72.md)
  