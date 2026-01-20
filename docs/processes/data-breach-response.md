---
type: process
title: Data Breach Response
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Data Breach Response

Specialized incident response process for confirmed or suspected unauthorized access to personal data (PII). Triggered when [Security Incident Response](security-incident-response.md) determines personal data was exposed. Ensures regulatory compliance (GDPR 72-hour notification, state breach laws, contractual obligations).

## Scope

**In scope** (triggers data breach process in addition to security incident response):

- **Customer PII**: Names, email addresses, phone numbers, payment information, account credentials, usage data tied to individuals
- **Employee PII**: SSN, salary, health information, background checks, personnel files
- **EU data subjects**: Any personal data of EU residents (GDPR applies regardless of company location)
- **Regulated data**: Health information (HIPAA), financial data (PCI DSS), children's data (COPPA)

**Breach scenarios**:

- Confirmed unauthorized access (attacker accessed database, logs show data exfiltration)
- Suspected unauthorized access with reasonable likelihood (compromised admin account had access to PII, cannot rule out access)
- Accidental exposure (S3 bucket misconfiguration, email to wrong recipient, lost laptop)
- Insider threat (employee accessed PII without business need, exfiltrated data)

**Not a breach** (no notification required, but may still be security incident):

- Encrypted data accessed but encryption keys not compromised
- Properly anonymized data (cannot be re-identified)
- Internal-only incident with no PII accessed
- Unsuccessful attack attempts with no data access

**Notification thresholds** vary by jurisdiction and regulation. When in doubt, Legal advises. GDPR default: notify if "risk to rights and freedoms" of individuals.

## Roles

**Incident Commander** ([Security Team](../policies/security-team.md) Lead): Coordinates response per [Security Incident Response](security-incident-response.md), determines breach occurred, estimates data subjects affected, leads data impact assessment.

**Legal Counsel**: Primary decision-maker on notification requirements, drafts regulatory notifications and customer communications, coordinates with external counsel if needed, manages regulator interactions.

**Privacy Officer** (if applicable): GDPR compliance lead, maintains data processing records, validates DPA notification obligations, coordinates with Data Protection Authority (DPA).

**Executive Sponsor** (CTO/CEO): Approves notification strategy, allocates resources, communicates with Board, signs regulatory notifications, speaks to press if needed.

**PR/Communications**: Drafts customer-facing communications, manages press inquiries, coordinates public statements, monitors social media/reputation impact.

**Customer Support**: Handles customer inquiries post-notification, provides scripted responses, escalates complex questions to Security/Legal.

## Steps

### 1. Breach Determination & Data Impact Assessment

**Triggered when** [Security Incident Response](security-incident-response.md) investigation determines personal data may have been accessed.

**Security Team assesses**:

**What data was accessed/exfiltrated?**

- Database tables, file shares, backups, logs
- Fields exposed (names, emails, passwords, SSN, payment info)
- Data elements per individual (single field vs comprehensive profile)

**How many individuals affected?**

- Query databases for affected user IDs or date ranges
- Review logs for scope of attacker access
- Estimate if precise count unavailable (e.g., "approximately 10,000-15,000 users")

**What type of data?**

- Identify data classification: public, internal, confidential, restricted
- Flag sensitive categories: SSN, financial, health, children, biometric
- Determine if encrypted (and whether keys compromised)

**Likelihood of harm to individuals**:

- **High**: SSN, passwords, financial data, health info → identity theft, fraud
- **Medium**: Email, phone, address → phishing, spam
- **Low**: Public information only, encrypted with keys secure

**Output**: Data impact assessment documenting data types, individual count, likelihood of harm. Legal uses this to determine notification requirements.

### 2. Regulatory Notification Determination

**Legal assesses** notification obligations:

**GDPR** (if EU data subjects affected):

- **Notify supervisory authority within 72 hours** if breach likely to result in risk to individuals
- **Notify data subjects without undue delay** if high risk (cannot mitigate risk through measures like encryption)
- **Exception**: No notification if data was encrypted and keys not compromised, or if risk is low

**State breach laws** (US):

- Each state has different requirements (all 50 states + territories have laws)
- Generally: notify residents if unencrypted PII accessed
- Timeline varies: "without unreasonable delay", "most expedient time", specific day counts
- Some states require notification to Attorney General or credit bureaus

**Contractual obligations**:

- Review customer contracts for breach notification SLAs (common: 24-72 hours)
- May be stricter than regulatory requirements
- Failure to notify on time = breach of contract

**Industry regulations**:

- **HIPAA** (health data): Notify HHS within 60 days, media if >500 individuals
- **PCI DSS** (payment cards): Notify card brands and acquiring bank per PCI requirements

**Legal documents** notification requirements with timelines and determines notification content requirements.

### 3. Containment & Remediation

**Parallel to notification**, Security Team completes containment per [Security Incident Response](security-incident-response.md):

- Eradicate attacker access
- Patch vulnerability exploited
- Rotate credentials
- Restore systems to secure state

**Additional breach-specific actions**:

**Credential compromise** (passwords, API keys, tokens):

- Force password reset for all affected accounts
- Revoke sessions and tokens
- Enable additional monitoring on affected accounts for 90 days
- Consider temporary MFA enforcement if not already required

**Financial data compromise** (credit cards, bank accounts):

- Offer credit monitoring services to affected individuals (typically 12-24 months)
- Coordinate with payment processors for card reissuance if needed
- Report to credit bureaus if SSN involved

**Health data compromise** (HIPAA):

- Document breach in compliance tracker
- Prepare for potential HHS investigation

### 4. Notification Execution

**Internal notification first**:

- Brief executive team on breach details, notification plan, potential impact
- Prepare customer support team with FAQs and talking points
- Alert PR team to prepare for potential press inquiries

**Regulatory notifications** (Legal drafts, Executive signs):

**GDPR supervisory authority notification** (within 72 hours):

- Nature of breach (how it happened)
- Categories and approximate number of data subjects
- Likely consequences
- Measures taken or proposed to address breach
- Contact point (DPO or Security Team)

**State Attorney General notifications** (as required by state law)

**Federal notifications** (HHS for HIPAA, FTC for certain breaches)

**Customer/data subject notifications**:

**Timing**: Per regulatory requirements (GDPR: without undue delay for high risk, state laws: varies, contracts: per SLA)

**Content** (Legal drafts, PR reviews):

- What happened (brief, non-technical explanation)
- What data was involved (be specific: "email and password" vs vague "account information")
- When it happened (date range)
- What we're doing about it (containment, investigation, remediation)
- What individuals should do (change password, monitor accounts, use credit monitoring if offered)
- How to contact us (dedicated email/phone for questions)
- Apology and commitment to improvement

**Channels**: Email preferred (documented, direct), may supplement with in-app notification, website banner, or postal mail for serious breaches or if email unavailable

**Press/public statement** (if breach is material or public interest):

- PR drafts statement, Legal reviews, Executive approves
- Post on company blog/security page
- Proactive outreach to press if major breach (get ahead of story)

### 5. Post-Breach Activities

**Credit monitoring** (for SSN or financial data breaches):

- Contract with credit monitoring service (Experian, Equifax, TransUnion)
- Provide affected individuals with enrollment codes
- Cover cost for 12-24 months (industry standard)

**Customer support**:

- Monitor support queue for breach-related inquiries
- Track common questions and update FAQs
- Escalate anomalies or additional concerns to Security Team

**Regulatory cooperation**:

- Respond to DPA or AG inquiries promptly
- Provide investigation updates as requested
- Cooperate with potential audits or enforcement actions

**Post-incident review** (within 2 weeks):

- Conduct blameless post-mortem per [Security Incident Response](security-incident-response.md)
- Document lessons learned specific to breach response (notification timing, communication effectiveness)
- Update breach response playbook with improvements
- Add to risk register if systemic control gaps identified

**Metrics tracking** per [Governance Metrics](../charter/governance.md#metrics):

- Time from breach discovery to regulatory notification
- Time from breach discovery to customer notification
- Number of individuals affected
- Notification accuracy (did we notify correct count/scope?)
- Customer support inquiry volume and resolution time
- Regulatory outcome (fines, consent decrees, no action)

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Data Breach Response](../controls/incident-response/data-breach-response.md) ^[6-step process: immediate containment, impact assessment, regulatory notification (GDPR 72 hours), customer notification, remediation, post-incident review]
- [Customer Personal Data](../controls/data-privacy/customer-personal-data.md) ^[GDPR and state breach law notification requirements, data subject notification for high-risk breaches]
- [Employee Personal Data](../controls/data-privacy/employee-personal-data.md) ^[Employee PII breach notification requirements and procedures]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Breach response integrates with incident response process for investigation, containment, and forensics]
- [Contract Management](../controls/compliance/contract-management.md) ^[Review customer contracts for breach notification SLAs (24-72 hours typical)]
- [Customer Security Communications](../controls/security-assurance/customer-security-communications.md) ^[Customer notification templates, security support inbox, FAQ development, communications coordination with PR/Legal]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Breach notification records archived for regulatory compliance, post-mortem documentation]
