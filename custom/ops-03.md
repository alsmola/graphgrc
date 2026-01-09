# OPS-03: Incident Response
**Category: **Operational Security
  
## Objective
Respond effectively to security incidents and minimize impact.
  
## Description
Security incident response procedures are documented and tested. Incidents are detected, contained, and remediated. Post-incident reviews are conducted. Incidents are reported as required by regulation.
  
## Implementation Guidance
**Detection**: AWS GuardDuty, CloudWatch alarms, CrowdStrike EDR generate alerts. Employee reporting via security@company.com.
  
**Response Process**: Incident severity classification (P0-P3). On-call engineer paged for P0/P1. Incident commander assigned. War room (Slack/Zoom).
  
**Containment**: Isolate affected systems. Revoke compromised credentials. Preserve evidence for investigation.
  
**Post-Incident**: Post-incident review (PIR) within 5 days for P0/P1. Document findings, root cause, action items. Track remediation.
  
  
## Examples of Good Implementation
- GuardDuty detected compromised EC2 instance, paged on-call, instance isolated within 15 minutes
- Phishing email reported by employee, security team investigated and blocked sender
- Quarterly tabletop exercise practiced ransomware response
- 2024: 12 security incidents, all with completed PIRs and remediation action items
  
## Audit Evidence
- Incident response policy and runbooks
- Incident log with severity, timeline, resolution
- Post-incident review documents
- Tabletop exercise documentation
  
---
  
## Mapped framework controls
### GDPR
- [Art 33](../gdpr/art33.md)
- [Art 34](../gdpr/art34.md)
  
### SOC 2
- [CC7.3](../soc2/cc73.md)
- [CC7.4](../soc2/cc74.md)
- [CC7.5](../soc2/cc75.md)
  