---
type: process
title: Internal Audit
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Internal Audit

Quarterly self-assessment of security control effectiveness. Validates controls operate as designed, identifies gaps before external audit, drives continuous improvement. Complements [External Audit](external-audit.md) and tracks compliance per [Governance Metrics](../charter/governance.md#metrics).

## Scope

**Controls tested quarterly**:

- **Access management**: [Access reviews](access-review.md) completed on time, orphaned accounts removed, admin access justified
- **Change management**: Changes approved and documented, separation of duties, rollback capability
- **Monitoring**: Security alerts triaged, logs retained, anomaly detection functioning
- **Incident response**: Incidents documented, post-mortems completed, action items tracked
- **Risk management**: Risk register current, high/critical risks reviewed monthly, remediation on track
- **Vendor management**: New vendors assessed, annual reviews completed, vendor inventory current
- **Security assurance**: Design reviews for major changes, code review findings addressed, penetration tests scheduled
- **Personnel security**: Background checks completed, security training current, offboarding timely

**Evidence reviewed**:

- Logs and reports (access logs, vulnerability scans, change tickets, monitoring dashboards)
- Documentation (policies updated, procedures followed, meeting minutes, approval emails)
- Interviews (control owners confirm process adherence)
- System configurations (spot-check settings match requirements)

**Sampling approach**:

- Monthly controls: Test 1 month per quarter (rotating)
- Quarterly controls: Test current quarter
- Annual controls: Test completion status, review upcoming deadlines
- Event-driven controls: Test sample of recent events (e.g., 5 recent incidents, 5 recent vendor reviews)

## Roles

**Security Team**: Conducts internal audit, documents findings, reports to [Security Committee](../charter/governance.md#communication), tracks remediation, validates fixes, maintains audit evidence repository.

**Control Owners** (varies by control): Provide evidence, respond to audit requests, explain control operation, remediate findings within SLA.

**Engineering/IT/HR**: Assist with evidence collection for controls they own (infrastructure, development, personnel).

**Executive Sponsor** (CTO/CEO): Reviews quarterly audit results, approves risk acceptance for findings not remediated, allocates resources for remediation.

## Steps

### 1. Audit Planning (Week 1)

**Security Team prepares**:

- **Select controls to test**: All critical controls every quarter, rotate medium-risk controls, sample low-risk controls annually
- **Determine testing procedures**: What evidence to collect, what to inspect, who to interview
- **Assign auditors**: If multiple security team members, divide controls to avoid auditing own work
- **Schedule interviews**: Book time with control owners (30-60 min per domain)
- **Notify stakeholders**: Alert control owners 1 week ahead with list of evidence needed

**Prepare audit checklist**:

- Control description and expected operation
- Testing procedure (what to check)
- Evidence required (logs, screenshots, documentation)
- Pass/fail criteria
- Space for observations and findings

### 2. Evidence Collection (Week 2)

**Security Team requests** evidence from control owners:

**Access management**:

- Access review completion records (Q1 access review attestations)
- Orphaned account remediation logs (terminated employees, contractors)
- Admin account justifications and approval emails

**Change management**:

- Sample of change tickets with approvals (5-10 recent changes)
- Separation of duties validation (different person approves vs deploys)
- Rollback capability documentation

**Monitoring & logging**:

- Security alert triage logs (all Critical/High alerts from sample month)
- Log retention validation (confirm logs available for required period)
- SIEM dashboard screenshots showing coverage

**Incident response**:

- All incidents from quarter with post-mortem documentation
- Action item tracking showing status and ownership
- Notification timelines (for breaches, customer impact events)

**Risk management**:

- Current risk register
- Monthly risk review meeting notes
- High/Critical risk remediation progress updates

**Vendor management**:

- New vendor assessments completed this quarter
- Annual re-assessment completion for vendors with renewal dates
- Vendor inventory showing all active vendors

**Control owners provide** evidence within 3 business days. Security Team follows up on missing items.

### 3. Control Testing (Week 3)

**Security Team tests each control**:

**Inspection** (review documentation):

- Policies match actual practices?
- Procedures clearly documented?
- Evidence complete for required period?

**Reperformance** (independently verify):

- Query access logs to validate access review findings
- Check SIEM for security alerts not in triage log (missed?)
- Review risk register for overdue remediation items
- Spot-check vendor inventory against procurement records

**Inquiry** (interview control owners):

- How does this control work in practice?
- What challenges did you face this quarter?
- Any changes to the process since last quarter?
- How do you know control is effective?

**Observation** (if applicable):

- Attend access review meeting, risk review meeting, incident response drill

**Document results** for each control:

- **Pass**: Control operated effectively, no exceptions found
- **Pass with observation**: Control operated but minor improvement suggested (not a finding)
- **Fail**: Control did not operate effectively (finding requiring remediation)

### 4. Findings Documentation & Remediation Planning (Week 3-4)

**For each finding, Security Team documents**:

- **Control that failed**: Which control, what should have happened
- **What went wrong**: Specific instance(s) of failure, evidence of gap
- **Root cause**: Why did it fail? (Process gap, lack of automation, unclear ownership, training needed)
- **Impact**: What risk does this create? Use [Risk Scoring](organizational-risk-assessment.md#risk-scoring-methodology)
- **Remediation recommendation**: Specific actions to fix (automate, update procedure, train, assign owner)

**Security Team meets with control owner**:

- Review finding and root cause
- Agree on remediation plan
- Assign owner and deadline (based on risk severity: Critical <7d, High <30d, Medium <90d)
- Identify any dependencies or resource needs

**Findings categories**:

- **Critical**: Control completely ineffective, high risk exposure (immediate escalation to executives)
- **High**: Control partially effective, gaps create significant risk (30-day remediation)
- **Medium**: Control mostly effective, minor gaps (90-day remediation)
- **Low/Observation**: Control effective, opportunity for improvement (track but not urgent)

**Document compensating controls** (if remediation delayed):

- What temporary measures reduce risk?
- When will permanent fix be implemented?
- Who approved delay and risk acceptance?

### 5. Reporting & Governance (Week 4)

**Security Team prepares** quarterly audit report for [Security Committee](../charter/governance.md#communication):

**Executive summary**:

- Controls tested (number, domains)
- Pass rate (e.g., "95% of controls operating effectively")
- Findings by severity (Critical/High/Medium/Low)
- Comparison to prior quarter (improving, stable, declining)

**Findings detail**:

- Each finding with description, impact, remediation plan, owner, deadline
- Status of prior quarter findings (closed, in progress, overdue)

**Trend analysis**:

- Common root causes (training gaps, automation opportunities, policy clarity issues)
- Control domains with recurring issues
- Effectiveness improvements year over year

**Recommendations**:

- Process improvements (automate manual controls)
- Resource needs (tools, headcount, training)
- Policy updates (unclear language, gaps in coverage)

**Security Committee reviews** (quarterly meeting):

- Discuss findings and remediation progress
- Approve risk acceptance for delayed remediation
- Allocate resources for improvements
- Set priorities for next quarter

**Metrics tracked** per [Governance Metrics](../charter/governance.md#metrics):

- Internal audit completion: 100% quarterly
- Control effectiveness: >95%
- Remediation within SLA: >90%
- Audit findings trend (should decrease over time as controls mature)

### 6. Remediation Tracking & Validation

**Control owners** execute remediation plans with Security Team monitoring:

- Monthly check-ins on remediation status
- Escalate overdue items to management
- Validate completed remediation before closing

**Security Team validates** remediation via:

- Retest control with same procedure
- Review updated documentation
- Confirm process change implemented
- Close finding once validated effective

**Continuous improvement**:

- Update control descriptions if actual practice differs from documentation (document reality, then improve if needed)
- Automate manual controls where feasible (reduce human error)
- Enhance training based on common gaps
- Revise testing procedures based on lessons learned

**Evidence retention**:

- Archive audit workpapers, evidence, findings for [External Audit](external-audit.md)
- Demonstrate control effectiveness over time (for SOC 2 Type II)
- Support trending and year-over-year analysis

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Internal Audits](../controls/compliance/internal-audits.md) ^[Quarterly internal control testing with sampling, evidence collection, deficiency identification, and tracking]
- [External Audits](../controls/compliance/external-audits.md) ^[Internal audits support external audit preparation by identifying and remediating gaps]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Internal audit workpapers archived for compliance evidence and trend analysis]
- [Change Management](../controls/operational-security/change-management.md) ^[Internal audit reviews change approval and testing evidence]
