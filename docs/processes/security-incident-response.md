---
type: process
title: Security Incident Response
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Security Incident Response

Structured response to security events affecting confidentiality, integrity, or availability of systems and data. Minimize impact, contain threats, restore operations, learn from incidents. Activates [Governance Incident Response Team](../charter/governance.md#communication) for major incidents.

## Scope

**In scope** (triggers this process):

- Unauthorized access to systems or data
- Malware/ransomware detection on endpoints or servers
- Data exfiltration or data loss
- Denial of service affecting customer-facing systems
- Compromised credentials or accounts
- Insider threats or policy violations
- Third-party security incidents affecting organization
- Vulnerability exploitation attempts

**Related processes**:

- **Data breach** (customer/employee PII exposure): Follow [Data Breach Response](data-breach-response.md) in addition to this process for GDPR/privacy obligations
- **Availability incidents** (non-security outages): Follow standard incident management, escalate to security if malicious activity suspected
- **Vulnerability disclosure**: Not an active incident, follow vulnerability management process

**Severity levels** (determines response intensity):

| Severity | Definition | Response Time | Escalation |
| -------- | ---------- | ------------- | ---------- |
| **Critical** | Active data breach, ransomware, customer data exposure, production system compromise | Immediate (24/7) | Executive, Legal, PR |
| **High** | Confirmed unauthorized access, malware on production-adjacent systems, credential compromise | <1 hour during business hours | Security Team + Engineering Lead |
| **Medium** | Suspicious activity, failed attack attempts, non-production compromise | <4 hours during business hours | Security Team |
| **Low** | Policy violations, non-malicious data exposure, low-impact events | <24 hours | Security Team triages |

## Roles

**Incident Commander** (Security Team Lead): Coordinates response, makes containment decisions, communicates with stakeholders, declares incident resolved. Single decision-maker to avoid confusion.

**Security Team**: Investigates root cause, performs forensics, identifies indicators of compromise (IOCs), contains threat, documents timeline, leads post-mortem.

**Engineering On-Call**: Executes technical containment (isolate systems, rotate credentials, deploy patches), provides system expertise, restores services.

**IT Operations**: Endpoint containment (isolate laptops, reimage systems), network isolation, access revocation, assists with evidence collection.

**Legal**: Advises on notification requirements, attorney-client privilege for forensics, regulatory obligations, customer communication approval.

**PR/Communications**: Customer notification, public statements, press inquiries. Coordinates with Legal before external communication.

**Executive Sponsor** (CTO/CEO): Informed of Critical/High incidents, approves notification strategy, allocates resources, approves business continuity trade-offs.

**HR**: Investigates insider threats, coordinates employee actions, handles personnel issues discovered during investigation.

## Steps

### 1. Detection & Triage (Immediate)

**Security Team receives alert** from:

- Automated detection: EDR, SIEM, cloud security tools (see [Endpoint Threat Detection](../controls/threat-detection/endpoint-threat-detection.md), [Cloud Threat Detection](../controls/threat-detection/cloud-threat-detection.md))
- Manual report: Employee notices suspicious activity, phishing report, third-party notification
- Vulnerability scanning: Critical vulnerability exploited in the wild

**Security Team performs initial triage** (15-30 min):

- **Validate**: Is this a true security incident or false positive?
- **Scope**: What systems/data affected? How many users/customers?
- **Impact**: Confidentiality, integrity, or availability? Still ongoing or contained?
- **Severity**: Use table above to assign Critical/High/Medium/Low

**Declare incident** if validated security event. Assign unique incident ID, create incident channel (Slack/Teams), notify relevant roles per severity.

**Output**: Incident ticket with severity, initial scope, assigned Incident Commander

### 2. Containment (Immediate - within SLA)

**Goal**: Stop ongoing damage while preserving evidence for forensics.

**Incident Commander coordinates** containment actions:

**Short-term containment** (stop the bleeding):

- **Compromised account**: Revoke credentials, terminate active sessions, reset MFA (see [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md))
- **Malware infection**: Isolate affected endpoints from network, prevent lateral movement
- **Data exfiltration**: Block attacker IPs, revoke API keys, disable compromised integrations
- **Vulnerability exploitation**: Deploy emergency patch or disable vulnerable service, implement WAF rules

**Evidence preservation**:

- Take disk/memory snapshots before remediation
- Preserve logs (endpoint, network, application, cloud trails)
- Document attacker actions from forensic timeline
- Maintain chain of custody for potential legal proceedings

**Do NOT**:

- Delete attacker accounts/tools immediately (preserve for forensics)
- Notify attacker they've been detected (may destroy evidence)
- Communicate externally before Legal approval (regulatory implications)

**Output**: Threat contained, no ongoing unauthorized access or data exfiltration

### 3. Investigation & Eradication (Hours - Days)

**Security Team investigates** to understand full scope:

**Root cause analysis**:

- How did attacker gain initial access? (phishing, vulnerability, credential stuffing, insider)
- What vulnerabilities or control gaps enabled this?
- When did compromise occur? How long had attacker been present?
- What actions did attacker take? (lateral movement, data access, exfiltration, persistence mechanisms)

**Scope expansion**:

- Check for additional compromised accounts/systems using IOCs
- Search logs for similar attacker techniques across environment
- Assess if this is isolated incident or part of broader campaign

**Eradication** (remove attacker presence):

- Delete malware, backdoors, persistence mechanisms
- Patch vulnerabilities exploited
- Rotate all potentially compromised credentials (see [Password Management](../controls/iam/password-management.md), [Secrets Management](../controls/iam/secrets-management.md))
- Remove attacker accounts, revoke access tokens

**Data impact assessment** (for potential breach):

- What data did attacker access? Customer PII, employee data, business secrets?
- Was data exfiltrated or just accessed?
- How many individuals affected?
- If PII involved, trigger [Data Breach Response](data-breach-response.md) for notification obligations

**Output**: Attacker fully removed, data impact quantified, remediation plan for control gaps

### 4. Recovery (Hours - Days)

**Engineering and IT restore normal operations**:

- Rebuild compromised systems from clean backups or fresh images
- Restore data from pre-incident backups if integrity compromised
- Re-enable disabled services/features once secured
- Validate system integrity before returning to production
- Enhanced monitoring for recurrence (watch for IOCs)

**Validation**:

- Confirm attacker access fully revoked
- Verify systems functioning normally
- Check for any missed persistence mechanisms
- Monitor for 7-14 days for reinfection

**Output**: Systems restored to secure operational state, business continuity resumed

### 5. Communication & Notification

**Internal communication** (Incident Commander):

- Real-time updates in incident channel during active response
- Executive briefing for High/Critical incidents (twice daily or more during active response)
- All-hands communication if company-wide impact or employee action required

**External communication** (Legal + PR approval required):

**Customer notification** (if customer data affected):

- Assess contractual SLAs (e.g., notify within 24/72 hours)
- Draft notification with specifics: what happened, what data, what actions taken, customer actions needed
- Legal and PR review before sending
- Send via email, in-app notification, or as contractually required

**Regulatory notification** (if personal data breach):

- GDPR: Notify supervisory authority within 72 hours if risk to individuals (see [Data Breach Response](data-breach-response.md))
- State breach laws: Vary by jurisdiction, Legal advises
- Industry regulations: HIPAA, PCI DSS, etc. as applicable

**Third-party notification**:

- Affected vendors/partners if their data exposed
- Cloud providers if their services involved
- Law enforcement if criminal activity (FBI, IC3)

**Output**: All required notifications sent within regulatory/contractual timelines

### 6. Post-Incident Review (Within 1 week)

**Security Team leads blameless post-mortem** (60-90 min) with all involved parties:

**Timeline review**: Reconstruct incident from detection to resolution, identify delays or confusion

**What went well**: Effective actions, good decisions, heroic efforts

**What went wrong**: Control failures, detection gaps, slow response, communication issues

**Root cause**: Why did this happen? (Not "who is to blame" - focus on process/control gaps)

**Action items**:

- Fix control gaps (patch, configuration, policy update)
- Improve detection (new alerts, better logging)
- Enhance response (playbook updates, training, tools)
- Assign owners and deadlines for each action

**Add to risk register**: Document systemic risks identified per [Organizational Risk Assessment](organizational-risk-assessment.md)

**Update metrics** per [Governance Metrics](../charter/governance.md#metrics):

- Detection time (alert to investigation start)
- Containment time (investigation start to contained)
- Total incident duration (detection to resolution)
- Customer impact (users affected, downtime)

**Output**: Post-mortem report with lessons learned and action items, archived for compliance evidence

---

## Control Mapping

---

## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*
