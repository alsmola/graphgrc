---
type: process
title: Incident Response Process
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [security-team, infrastructure-team, engineering-leads, legal, executive-team]
---

# Incident Response Process

Process for responding to security incidents from detection through resolution.

## Roles and Responsibilities

- **Incident Commander (IC):** Leads response, coordinates teams, makes decisions (Security Team Lead)
- **Security Team:** Investigation, containment, forensics
- **Infrastructure Team:** System remediation, infrastructure changes
- **Engineering Team:** Application-level remediation, code changes
- **Legal:** Regulatory compliance, external notifications
- **Executive Team:** Business decisions, customer communication

## Prerequisites

- Incident response plan approved and documented
- On-call rotation defined for security team
- Communication channels established (Slack #security-incidents, PagerDuty)
- Incident response runbooks and playbooks available

## Process Steps

### Step 1: Detection and Reporting

Incident is detected via automated alert or reported by user/third party.

**Detection sources:**
- SIEM alerts (GuardDuty, CloudWatch)
- User reports (phishing, suspicious activity)
- Vendor notification
- Penetration test findings
- Security researcher disclosure

**Actions:**
- Create incident ticket
- Page on-call security engineer for Sev 1/2
- Post to #security-incidents Slack channel

**Owner:** Anyone (reporter), Security Team (triage)
**Duration:** Immediate

### Step 2: Initial Assessment

On-call security engineer performs initial triage and assigns severity.

**Assessment criteria:**
- Data confidentiality impact (is data compromised?)
- System integrity impact (is code/config modified?)
- Availability impact (is service down?)
- Scope (one user vs. all customers?)

**Severity assignment:** See incident-response-standard.md

**Actions:**
- Assign incident commander (IC)
- Escalate to security team lead if Sev 1/2
- Notify infrastructure/engineering if needed

**Owner:** Security Team
**Duration:** 15 minutes for Sev 1/2, 1 hour for Sev 3/4

### Step 3: Containment

IC coordinates immediate containment to prevent further damage.

**Containment actions (examples):**
- Isolate compromised EC2 instance (security group rules to deny all)
- Revoke compromised credentials (IAM user, API keys)
- Block attacker IP at WAF/CloudFront
- Disable compromised user accounts
- Take snapshot of affected systems before remediation (forensics)

**Goal:** Stop the bleeding, preserve evidence

**Owner:** Security Team, Infrastructure Team
**Duration:** 15-30 minutes for Sev 1, 1-2 hours for Sev 2/3

### Step 4: Investigation

Security team investigates root cause and determines full scope.

**Investigation tasks:**
- Review logs (CloudTrail, application logs, VPC Flow Logs)
- Identify entry vector (how did attacker get in?)
- Determine timeline (when did breach start?)
- Assess data accessed (query audit logs for data access)
- Check for persistence mechanisms (backdoors, additional compromised accounts)

**Tools:** Log analysis (CloudWatch Insights, Athena), forensics (disk imaging if needed)

**Owner:** Security Team
**Duration:** Hours to days depending on complexity

### Step 5: Eradication

Remove attacker access and remediate root cause.

**Eradication actions:**
- Patch vulnerability that was exploited
- Remove malware/backdoors
- Reset all potentially compromised credentials
- Apply security controls to prevent recurrence
- Rebuild compromised systems from clean images if needed

**Owner:** Security Team, Infrastructure Team, Engineering Team
**Duration:** Hours to days

### Step 6: Recovery

Restore systems to normal operation.

**Recovery actions:**
- Bring systems back online
- Verify no attacker access remains
- Monitor closely for signs of re-compromise
- Restore data from backups if needed

**Owner:** Infrastructure Team
**Duration:** Minutes to hours

### Step 7: Communication

Notify stakeholders based on severity and impact.

**Internal communication:**
- Update #security-incidents channel with regular status updates
- Notify executive team for Sev 1/2
- Brief all-hands if customer-impacting

**External communication:**
- Customer notification if data breach (follow data-breach-response-process.md)
- GDPR breach notification within 72 hours if required
- Regulatory notifications (SOC 2 auditor, cyber insurance)

**Owner:** Incident Commander, Legal, Executive Team
**Duration:** Varies (GDPR 72 hours deadline)

### Step 8: Post-Incident Review

Conduct blameless retrospective within 7 days of incident closure.

**Review topics:**
- What happened (timeline)
- What went well
- What could be improved
- Root cause analysis
- Action items to prevent recurrence

**Deliverable:** Post-incident report with lessons learned

**Owner:** Security Team
**Duration:** 1-2 hour meeting, written report within 7 days

### Step 9: Follow-up Actions

Implement improvements identified in post-incident review.

**Examples:**
- Deploy additional monitoring/alerting
- Update runbooks and playbooks
- Security training for teams
- Architecture changes
- Policy updates

**Owner:** Security Team, Engineering Team
**Duration:** Weeks (tracked in backlog)

## Validation and Evidence

- Incident ticket with full timeline
- Investigation notes and log exports
- Remediation actions documented
- Communication records (emails, Slack messages)
- Post-incident report
- Retain all evidence for 7 years

## Severity-Specific Response Times

- **Sev 1:** Immediate response, page on-call, IC assigned within 15 min
- **Sev 2:** Response within 1 hour, IC assigned within 2 hours
- **Sev 3:** Response within 4 hours, next business day for IC
- **Sev 4:** Response within 24 hours

## References

- Related controls: OPS-03
- Related standards: incident-response-standard.md, logging-monitoring-standard.md
- Related process: data-breach-response-process.md
- NIST SP 800-61r2: Computer Security Incident Handling Guide

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [OPS-03: Incident Response](../custom/ops-03.md) ^[9-step incident response: detection, assessment, containment, investigation, eradication, recovery, communication, PIR, follow-up]
- [INF-03: Logging & Monitoring](../custom/inf-03.md) ^[CloudTrail, CloudWatch, and GuardDuty used for detection and investigation]
- [DAT-04: Data Privacy (GDPR Compliance)](../custom/dat-04.md) ^[GDPR breach notification within 72 hours, legal team involvement for external communication]

---

<!-- Backlinks auto-generated below -->
## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*

