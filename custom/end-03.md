# END-03: Software Updates
**Category: **Endpoint Security
  
## Objective
Reduce vulnerability exposure through timely patching.
  
## Description
Operating systems and applications are kept up to date with security patches. Critical security updates are applied within 7 days. Patch status is monitored.
  
## Implementation Guidance
**Automatic Updates**: MDM policy enables automatic macOS security updates. Users cannot disable.
  
**Patch Schedule**: Critical security patches applied within 7 days. Other updates within 30 days.
  
**Application Updates**: Homebrew or automatic updaters for development tools. Security-critical apps (browsers) auto-update.
  
**Monitoring**: MDM dashboard shows OS version for all devices. Outdated devices flagged and users notified.
  
  
## Examples of Good Implementation
- 95% of employee Macs on latest macOS version within 30 days of release
- Critical macOS security update deployed to all devices within 5 days
- Chrome browser automatically updates to latest version within 24 hours
- MDM report shows zero devices more than 60 days behind on patches
  
## Audit Evidence
- MDM update policy configuration
- Device OS version report
- Patch deployment timeline for recent critical updates
- Update compliance dashboard
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC7.1](../soc2/cc71.md)
- [CC8.1](../soc2/cc81.md)
  