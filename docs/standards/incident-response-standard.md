---
type: standard
id: standard-incident-response
title: Incident Response Standard
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: [security-team, infrastructure-team, engineering-leads]
---

# Incident Response Standard

Requirements for detecting, responding to, and recovering from security incidents.

## Scope

All security incidents affecting confidentiality, integrity, or availability of systems or data.

## Incident Severity Levels

### Severity 1 (Critical)

- Active data breach or confirmed unauthorized access to Confidential/Restricted data
- Ransomware or destructive malware
- Complete service outage affecting all customers
- Response time: Immediate (page on-call)

### Severity 2 (High)

- Suspected data breach under investigation
- Successful phishing with credential compromise
- Vulnerability actively being exploited
- Partial service outage
- Response time: Within 1 hour

### Severity 3 (Medium)

- Security policy violation
- Malware detected and contained
- Vulnerability discovered (not exploited)
- Failed intrusion attempt
- Response time: Within 4 hours

### Severity 4 (Low)

- Suspicious activity (false positive likely)
- Policy violation with minimal risk
- Response time: Within 24 hours

## Detection Methods

- Automated alerts from monitoring systems (GuardDuty, SIEM)
- User reports (phishing, suspicious activity)
- Third-party notification (vendor, researcher)
- Security scanning and audits

## Response Requirements

### Immediate Actions

1. **Contain:** Isolate affected systems, revoke compromised credentials
2. **Assess:** Determine scope and severity
3. **Notify:** Alert security team, page on-call if Sev 1/2
4. **Document:** Create incident ticket with timeline

### Investigation

- Collect logs and forensic evidence before remediation
- Identify root cause and entry vector
- Determine data/systems impacted
- Preserve evidence for potential legal action

### Remediation

- Remove attacker access
- Patch vulnerabilities
- Restore from clean backups if needed
- Reset credentials for affected systems/users

### Communication

- **Internal:** Notify leadership, affected teams
- **External:** Notify customers if data breach (see data-breach-response-process.md)
- **Regulatory:** GDPR breach notification within 72 hours if applicable

### Post-Incident

- Document lessons learned
- Update runbooks and detections
- Implement preventive controls
- Security team reviews within 7 days

## Evidence Retention

- All incident artifacts retained for 7 years
- Chain of custody maintained for forensic evidence

## Testing

- Tabletop exercises: Quarterly
- Simulated incident response: Annually

## References

- Related controls: OPS-03
- Related process: incident-response-process.md, data-breach-response-process.md
- NIST SP 800-61r2: Computer Security Incident Handling Guide

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Four severity levels with response times: Sev 1 (immediate), Sev 2 (1hr), Sev 3 (4hrs), Sev 4 (24hrs), containment and remediation procedures]
- [Data Breach Response](../controls/incident-response/data-breach-response.md) ^[GDPR breach notification within 72 hours, customer notification for data breaches, evidence preservation]
- [Incident Response Exercises](../controls/incident-response/incident-response-exercises.md) ^[Tabletop exercises quarterly, simulated incident response annually]
- [Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md) ^[Automated alerts from GuardDuty/SIEM for detection, centralized log collection for forensic investigation]
- [Cloud Threat Detection](../controls/threat-detection/cloud-threat-detection.md) ^[GuardDuty automated detection, user reports, third-party notifications as detection methods]
- [Customer Personal Data](../controls/data-privacy/customer-personal-data.md) ^[Customer notification requirements for personal data breaches, GDPR compliance procedures]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Incident artifacts retained for 7 years, lessons learned documentation, runbook updates]
- [Business Continuity](../controls/operational-security/business-continuity.md) ^[Incident response procedures support business continuity by enabling rapid detection, containment, and recovery from disruptions]

---

<!-- Backlinks auto-generated below -->
