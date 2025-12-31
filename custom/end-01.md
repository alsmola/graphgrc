# END-01: Device Management (macOS MDM)
**Category: **Endpoint Security
  
## Objective
Secure employee endpoints through centralized management.
  
## Description
All employee devices are managed through MDM. Security policies are enforced including disk encryption, screen lock, and automatic updates. Lost devices can be remotely wiped.
  
## Implementation Guidance
**MDM Solution**: Jamf Pro or Kandji for Mac management. All devices enrolled before provision to employee.
  
**Required Policies**: FileVault enabled, screen lock after 5 minutes, automatic updates enabled, malware protection installed.
  
**Compliance Monitoring**: MDM dashboard shows device compliance. Non-compliant devices flagged and user notified.
  
**Remote Wipe**: Lost or stolen device remotely wiped via MDM. Terminated employee devices wiped within 1 hour.
  
  
## Examples of Good Implementation
- 100% of employee Macs enrolled in Jamf with FileVault enabled
- MDM enforces automatic macOS security updates within 7 days of release
- Lost laptop remotely wiped within 2 hours of employee report
- Non-compliant device blocked from network access until remediated
  
## Audit Evidence
- MDM enrollment report showing all devices
- Device compliance dashboard
- Remote wipe logs
- MDM policy configuration
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.6](../soc2/cc66.md)
- [CC6.7](../soc2/cc67.md)
  