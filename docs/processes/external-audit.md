---
type: process
title: External Audit
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# External Audit

Annual SOC 2 Type II audit conducted by independent third-party auditor. Validates security controls operate effectively over defined audit period (typically 12 months). Provides customer assurance and competitive requirement for enterprise sales. Tracks compliance per [Governance Metrics](../charter/governance.md#metrics).

## Scope

**SOC 2 Type II Audit**:

- **Trust Service Criteria**: Security (required), Availability, Confidentiality, Processing Integrity, Privacy (as applicable to business)
- **Audit period**: 12 months (e.g., January 1 - December 31)
- **Systems in scope**: Production infrastructure, customer data systems, security controls, administrative systems affecting security
- **Controls tested**: ~20-50 controls depending on scope (access management, change management, monitoring, incident response, risk management, vendor management)

**Other potential audits** (if applicable):

- **ISO 27001 certification**: Alternative to SOC 2, common in Europe
- **PCI DSS**: If processing credit cards
- **HIPAA**: If processing health information
- **FedRAMP**: If selling to US government

This process focuses on SOC 2 as most common. Adapt for other audit types with similar steps.

## Roles

**Executive Sponsor** (CTO/CEO): Approves audit scope and budget, reviews draft report, signs management assertions, communicates results to Board and customers.

**Security Team**: Primary audit liaison, coordinates evidence collection, responds to auditor requests, remediates findings, manages audit project timeline, prepares for and attends audit meetings.

**IT Operations**: Provides evidence for infrastructure controls (access logs, change tickets, patch reports, backup validation).

**Engineering**: Provides evidence for development controls (code review records, security testing results, deployment logs).

**HR**: Provides evidence for personnel controls (background checks, training completion, termination procedures, access provisioning/deprovisioning).

**External Auditor**: Independent CPA firm, performs testing of controls, issues audit opinion, identifies exceptions/findings, provides SOC 2 report.

## Steps

### 1. Audit Planning & Scope (2-3 months before audit start)

**Select auditor** (if new or re-bidding):

- Engage 2-3 CPA firms with SOC 2 experience
- Request proposals with pricing, timeline, team qualifications
- Check auditor references from similar companies
- Select based on expertise, cost, cultural fit

**Define audit scope** (Security Team + Executive):

- Determine Trust Service Criteria (Security always included, add Availability/Confidentiality/Privacy as needed)
- Define system boundaries (what's in scope vs out of scope)
- Set audit period (typically calendar year or align with contract cycles)
- Identify controls to be tested based on risk assessment

**Establish timeline**:

- **Readiness assessment** (optional, 1-2 months before audit): Auditor performs pre-audit to identify gaps
- **Fieldwork** (typically 2-4 weeks): Auditor tests controls, interviews staff, reviews evidence
- **Draft report review** (1-2 weeks): Company reviews findings before finalization
- **Final report** (target date, e.g., March 31 for calendar year audit)

**Assign internal resources**:

- Audit project manager (typically Security Team lead)
- Control owners for each domain (IT, Engineering, HR)
- Evidence collectors and coordinators

### 2. Pre-Audit Readiness (Ongoing, intensifies 1-2 months before)

**Security Team conducts** [Internal Audit](internal-audit.md) to validate control effectiveness:

- Test each control in scope
- Document control procedures and evidence
- Identify and remediate gaps before external auditor arrives
- Conduct mock auditor interviews with control owners

**Prepare evidence repository**:

- Centralize evidence in shared folder (Google Drive, Confluence, GRC tool)
- Organize by control domain (access, change, monitoring, etc.)
- Include evidence for full audit period (12 months of quarterly access reviews, monthly vulnerability scans, etc.)
- Prepare narratives describing control implementation

**Train personnel**:

- Brief control owners on what to expect in auditor interviews
- Review control descriptions and evidence with each owner
- Emphasize honest, concise answers (don't speculate, say "I'll follow up" if unsure)
- Remind about confidentiality and professional demeanor

**Remediate known gaps**:

- Address findings from internal audit or previous year's audit
- Document compensating controls if unable to remediate before audit
- Update policies and procedures to reflect actual practices

### 3. Audit Fieldwork (2-4 weeks)

**Kick-off meeting** (auditor + Security Team + executives):

- Confirm scope, timeline, logistics
- Identify key contacts and evidence repository access
- Schedule interviews
- Set communication protocols (daily check-ins, Slack channel, etc.)

**Control testing** (auditor performs):

**Inquiry**: Interview control owners about how controls operate

**Inspection**: Review documented policies, procedures, evidence (logs, tickets, reports)

**Observation**: Watch controls in action (e.g., observe access review meeting)

**Reperformance**: Auditor independently performs control (e.g., query access logs, test configuration)

**Sampling**: For controls performed repeatedly, auditor selects samples across audit period (e.g., test 25 change tickets from 12 months)

**Security Team supports**:

- Respond to auditor requests for evidence within 24-48 hours
- Coordinate interviews (schedule, ensure attendance, follow up on action items)
- Clarify questions about control implementation
- Flag potential issues to executives immediately (don't surprise them at end)

**Daily/weekly status updates**:

- Auditor shares progress, open items, preliminary observations
- Security Team tracks outstanding evidence requests
- Escalate delays or challenges to audit project manager

### 4. Findings Review & Remediation

**Auditor identifies exceptions**:

- **Exception**: Control did not operate effectively in one or more instances
- **Deficiency**: Control design is inadequate or control did not operate throughout period
- **Material weakness**: Deficiency that could materially impact objectives

**Security Team responds** to each finding:

**Understand root cause**:

- Why did control fail? (Human error, process gap, tool limitation, policy unclear)
- How frequent was failure? (One-time mistake vs systemic issue)
- What is impact? (Actual harm vs potential risk)

**Develop remediation plan**:

- Immediate fix (e.g., complete missing access review)
- Process improvement (e.g., automate reminder emails)
- Documentation update (e.g., clarify policy language)
- Training (e.g., re-train control owners)
- Assign owner and deadline

**Negotiate with auditor**:

- Provide context and compensating controls
- Request reclassification if warranted (e.g., deficiency → observation)
- Agree on remediation timeline (most remediation occurs post-audit)

**Management responses** included in final report:

- Acknowledge finding (don't dispute unless factually incorrect)
- Describe remediation plan with timeline
- Assign executive owner (demonstrates commitment)

### 5. Report Review & Finalization

**Auditor provides draft report**:

- Opinion (unqualified/clean opinion vs qualified with exceptions)
- System description (what's in scope)
- Control descriptions (how controls work)
- Tests performed and results
- Exceptions and management responses

**Security Team + Legal review**:

- Verify accuracy of system description and control descriptions
- Check for confidential information that should be redacted in customer-shared version
- Ensure management responses are clear and commitments are realistic
- Provide comments/corrections to auditor

**Auditor finalizes report**:

- Incorporates feedback
- Issues final signed SOC 2 Type II report
- Provides restricted-use version (full detail) and customer-ready version (may have internal details redacted)

**Executive signs** management assertion letter (included in report).

### 6. Post-Audit Activities

**Remediation execution**:

- Implement remediation plans per committed timelines
- Track remediation status in risk register
- Validate fixes with internal testing
- Document completion for next year's audit

**Customer communication**:

- Upload SOC 2 report to security portal or trust center
- Proactively share with key customers
- Respond to customer questions about findings (with Legal input if needed)

**Board/executive reporting**:

- Brief Board on audit results, findings, remediation plans
- Report to [Security Committee](../charter/governance.md#communication) on control effectiveness trends

**Continuous monitoring**:

- Track control effectiveness monthly via [Internal Audit](internal-audit.md)
- Update evidence repository throughout year (don't wait until next audit)
- Address gaps as identified (don't accumulate issues)

**Metrics tracking** per [Governance Metrics](../charter/governance.md#metrics):

- SOC 2 audit findings: Target 0 exceptions (track trend year over year)
- Control effectiveness: >95%
- Remediation completion: 100% by next audit

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [External Audits](../controls/compliance/external-audits.md) ^[Annual SOC 2 Type II audit process: planning, pre-audit readiness, fieldwork, report review, remediation, continuous monitoring]
- [Internal Audits](../controls/compliance/internal-audits.md) ^[Internal audits conducted before external audit to validate control effectiveness and identify gaps]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Evidence repository preparation with 12 months of control evidence organized by domain]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Incident response procedures and records reviewed during audit]
