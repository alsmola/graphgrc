---
type: charter
title: Risk Management
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
audience: leadership
---

# Risk Management

Framework for identifying, assessing, and managing information security and privacy risks. Enables business objectives through calculated risk-taking with clear ownership, decision authority, and accountability.

## Philosophy

**Risk-Informed**: Balance security with usability. Accept calculated risks to enable business velocity. Document all decisions with clear rationale and ownership.

**Continuous**: Risk management integrated into daily operations. [Organizational risk assessments](../processes/organizational-risk-assessment.md) run annually. Reassess when environment changes (new systems, threats, incidents).

**Shared Responsibility**: [Security Team](../policies/security-team.md) owns framework and methodology. Everyone identifies and manages risks in their domain. Engineering owns technical risks, HR owns people risks, etc.

## Risk Appetite

**Overall**: Moderate risk appetite. Prioritize protecting customer trust while enabling rapid innovation.

**Low tolerance**: Customer data confidentiality breaches, privacy violations (GDPR, data subject rights), compliance failures (SOC 2, contractual obligations).

**Moderate tolerance**: Availability risks with recovery plans, emerging technology adoption risks, controlled technical debt.

**High tolerance**: Internal operational inefficiencies, non-customer-facing system downtime, experimental feature risks.

## Risk Identification

**Proactive assessments** triggered by:

- New project/product initiative: [Security design review](../processes/security-design-review.md) before development starts
- New vendor/third party: [Vendor risk review](../processes/vendor-risk-review.md) before contract signature
- Annual comprehensive review: [Organizational risk assessment](../processes/organizational-risk-assessment.md)

**Reactive assessments** triggered by:

- [Security incidents](../processes/security-incident-response.md): Root cause analysis identifies systemic risks
- [Data breaches](../processes/data-breach-response.md): Assess similar exposure across systems
- Regulatory changes: Gap analysis against new requirements
- [Audit findings](../processes/external-audit.md): Escalate control deficiencies to risk register


## Risk Register
### Risk Treatment

**Mitigate**: Implement controls to reduce likelihood or impact. Most common approach. Track remediation in risk register with owner and deadline.

**Accept**: Document risk, obtain appropriate approval per decision authority table, set review date. Use when mitigation cost exceeds risk value or timeline constraints exist.

**Avoid**: Change project approach to eliminate risk. Use when risk exceeds appetite and cannot be sufficiently mitigated (e.g., reject vendor, cancel feature).

**Transfer**: Shift risk to third party via insurance, outsourcing, contractual terms. Use for risks outside core competency or requiring specialized expertise.
### Risk Scoring

Risks scored using **Risk Score = Likelihood × Impact** with values 1-3 for each dimension producing scores 1-9.

See [Organizational Risk Assessment](../processes/organizational-risk-assessment.md#risk-scoring-methodology) for detailed scoring methodology, likelihood/impact definitions, and examples.

**Maintained by**: [Security Team](../policies/security-team.md) in collaboration with risk owners.

###  **Review cadence**

- Monthly: New risks and status updates. Security Team + Engineering Leadership per [Governance Communication](governance.md#communication).
- Quarterly: All open risks. Security Committee reviews trends, escalates stalled items, reallocates resources.
- Annually: Comprehensive review. Archive closed risks, reassess accepted risks, validate scoring methodology.

### Decision Authority

Authority to accept or approve treatment plans scales with risk severity. See [Governance Ownership](governance.md#ownership) for role definitions.

| Risk Level | Decision Authority | Documentation Required | Review Frequency |
| ---------- | ------------------ | ---------------------- | ---------------- |
| Low | Security Team | Risk register entry | Annual |
| Medium | Security Team + Engineering Lead | Email approval with mitigation plan | Quarterly |
| High | CTO/Executive Sponsor | Written approval, compensating controls | Quarterly |
| Critical | CEO/Board | Formal approval, escalation plan | Monthly |

High and Critical risk acceptances require documented compensating controls and specific timeline for reassessment or mitigation.

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Risk Assessment](../controls/governance/risk-assessment.md) ^[Risk-informed philosophy, risk appetite framework (low/moderate/high tolerance), risk scoring methodology (Likelihood × Impact)]
- [Organizational Risk Assessment](../controls/risk-management/organizational-risk-assessment.md) ^[Annual comprehensive risk assessment, risk register maintenance, risk scoring with likelihood/impact dimensions, monthly/quarterly/annual review cadence]
- [Vendor Risk Management](../controls/risk-management/vendor-risk-management.md) ^[Vendor risk review before contract signature, third-party security assessments]
- [Security Reviews](../controls/security-assurance/security-reviews.md) ^[Security design reviews before development, proactive assessments for new projects/products]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Reactive risk assessments triggered by security incidents, root cause analysis identifies systemic risks]
- [Data Breach Response](../controls/incident-response/data-breach-response.md) ^[Breach-triggered risk assessments to identify similar exposures across systems]
- [External Audits](../controls/compliance/external-audits.md) ^[Audit findings escalated to risk register, control deficiencies treated as risks]
- [Internal Audits](../controls/compliance/internal-audits.md) ^[Internal audit findings incorporated into risk assessment process]
- [Security Policies](../controls/governance/security-policies.md) ^[Decision authority table for risk acceptance scaled by severity (Low: Security Team, Medium: +Engineering Lead, High: CTO, Critical: CEO/Board)]
