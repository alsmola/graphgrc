---
type: process
title: Data Breach Response Process
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [security-team, legal, executive-team, customer-success]
---

# Data Breach Response Process

Process for responding to confirmed or suspected unauthorized access to customer or employee data.

## Roles and Responsibilities

- **Security Team:** Investigation, containment, technical response
- **Legal:** Regulatory compliance, notification requirements
- **Executive Team:** Decision-making on customer notification, media response
- **Customer Success:** Customer communication and support
- **PR/Communications:** External communications (if needed)

## Prerequisites

- Incident response process (parent process)
- Data breach notification templates
- Legal counsel identified
- Customer communication channels ready

## Process Steps

### Step 1: Breach Confirmation

Security team determines if incident qualifies as a data breach.

**Data breach definition:**
- Unauthorized access to Confidential or Restricted data
- Exfiltration of customer PII, employee data, or sensitive business data
- Ransomware with data theft
- Accidental exposure (misconfigured S3 bucket, email to wrong recipient)

**Initial assessment:**
- What data was accessed/exfiltrated?
- How many individuals affected (customers, employees)?
- Scope: all data or subset?
- Likelihood of harm to individuals

**Owner:** Security Team
**Duration:** Hours (during incident response investigation phase)

### Step 2: Immediate Notification to Leadership

Security team immediately notifies executive team and legal counsel.

**Initial notification includes:**
- Summary of breach (what happened, when discovered)
- Data types affected
- Estimated number of individuals
- Preliminary assessment of regulatory obligations
- Recommended immediate actions

**Notification method:** Emergency meeting (in-person or video), followed by written summary

**Owner:** Security Team
**Duration:** Within 2 hours of breach confirmation

### Step 3: Regulatory Notification Timeline Assessment

Legal determines notification obligations and deadlines.

**Regulations considered:**
- **GDPR:** 72 hours to notify supervisory authority (from awareness of breach)
- **State breach laws (US):** Varies by state, typically "without unreasonable delay"
- **SOC 2:** Notify auditor within contractual timeframe
- **Customer contracts:** May have specific notification SLAs

**Deliverable:** Regulatory notification plan with deadlines

**Owner:** Legal
**Duration:** Within 6 hours of breach confirmation

### Step 4: Data Breach Assessment

Security team completes detailed assessment of breach scope.

**Assessment includes:**
- Complete list of affected individuals (names, contact info)
- Specific data elements compromised (PII categories, account details, etc.)
- Root cause analysis
- Timeline of unauthorized access
- Whether data was encrypted
- Likelihood of misuse
- Actions taken to contain breach and prevent recurrence

**Deliverable:** Data breach report (internal document)

**Owner:** Security Team
**Duration:** 24-48 hours

### Step 5: Regulatory Authority Notification (if required)

Legal submits breach notification to regulatory authorities within deadlines.

**GDPR supervisory authority notification (if applicable):**
- Submit within 72 hours
- Include: nature of breach, categories of data, number of individuals, likely consequences, measures taken
- Use official notification form/portal

**State attorney general notifications (if applicable):**
- Follow state-specific requirements
- May require notification to state AG before or concurrent with customer notification

**Owner:** Legal
**Duration:** Within regulatory deadlines (72 hours for GDPR)

### Step 6: Individual Notification Planning

Exec team and legal decide on customer/employee notification approach.

**Decision factors:**
- Regulatory requirements
- Likelihood of harm to individuals
- Media/PR risk
- Customer contract obligations

**Notification content:**
- What happened (in plain language)
- What data was affected
- When breach occurred and when discovered
- Steps taken to contain breach
- Risks to individuals
- Actions individuals can take (e.g., credit monitoring, password reset)
- Contact information for questions
- Resources offered (free credit monitoring if appropriate)

**Owner:** Legal, Executive Team, Customer Success
**Duration:** 24-48 hours after breach confirmation

### Step 7: Individual Notification Execution

Send breach notification to affected individuals.

**Notification methods:**
- Email (primary)
- In-app notification
- Postal mail (if required by regulation or no email available)
- Website notice

**Timing:**
- GDPR: "Without undue delay" after authority notification
- US states: Per state requirements (varies)
- Best practice: As soon as feasible, typically within 7-14 days

**Owner:** Customer Success (customers), HR (employees)
**Duration:** 1-2 days for sending (after approval)

### Step 8: External Notifications (if needed)

Notify other parties as required.

**Parties to notify:**
- SOC 2 auditor (per contract)
- Cyber insurance carrier
- Credit bureaus (if large breach, per state law)
- Media (if proactive disclosure strategy)
- Law enforcement (if criminal activity)

**Owner:** Legal, Executive Team
**Duration:** Days to weeks

### Step 9: Customer Support and Monitoring

Provide resources and support to affected individuals.

**Support includes:**
- Dedicated email/phone line for breach questions
- FAQ document
- Credit monitoring service (if appropriate)
- Password reset assistance

**Monitoring:**
- Track questions and concerns
- Monitor social media and news for reactions
- Provide updates to leadership on customer sentiment

**Owner:** Customer Success
**Duration:** Ongoing (weeks to months)

### Step 10: Post-Breach Review and Remediation

Conduct thorough review and implement preventive controls.

**Review:**
- Root cause analysis
- Preventive controls to implement
- Policy/process updates
- Training needs

**Deliverable:** Post-breach report with lessons learned and action items

**Owner:** Security Team
**Duration:** 2-4 weeks after incident closure

## Documentation Requirements

**Required documentation (retain for 7 years):**
- Data breach report (internal)
- Regulatory notifications submitted
- Individual notifications sent
- Customer support logs
- Post-breach review report
- Legal correspondence

## Testing

- Breach notification tabletop exercise annually
- Review notification templates and contact lists quarterly

## References

- Related controls: OPS-03, DAT-04
- Related process: incident-response-process.md
- Related standards: incident-response-standard.md
- GDPR Article 33 (Authority notification) and Article 34 (Individual notification)

---

<!-- Backlinks auto-generated below -->
