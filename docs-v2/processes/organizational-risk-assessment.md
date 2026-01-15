---
type: process
title: Organizational Risk Assessment
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Organizational Risk Assessment

Comprehensive annual assessment of information security and privacy risks across the organization. Implements the [Risk Management Charter](../charter/risk-management.md) methodology.

## Purpose

Identify, score, and prioritize organizational risks. Maintain risk register with treatment plans and ownership. Enable risk-informed decision making per [Governance](../charter/governance.md).

## Scope

**Systems**: All production infrastructure, SaaS applications, development environments, endpoints, networks.

**Data**: Customer data, employee data, intellectual property, business data across all classifications.

**Processes**: Engineering, operations, sales, support, HR, finance. Focus on security-relevant workflows.

**Third parties**: Critical vendors, service providers, data processors. Coordinated with [Vendor Risk Review](vendor-risk-review.md).

## Roles

**Security Team**: Leads assessment, facilitates interviews, scores risks, maintains register, reports to leadership.

**Engineering Leadership**: Identifies technical risks, validates scoring, owns remediation for infrastructure/application risks.

**IT Operations**: Identifies endpoint and access risks, owns remediation for IT systems.

**Department Heads**: Identify business process risks, approve risk acceptance in their domains.

**Executive Sponsor** (CTO/CEO): Reviews High/Critical risks, approves risk acceptance, allocates remediation resources.

## Risk Scoring Methodology

**Risk Score = Likelihood × Impact**

### Likelihood Assessment

**Low (1)**: <10% probability in next 12 months

- No known threat actors targeting this area
- Strong preventive controls in place
- No recent incidents or near-misses

**Medium (2)**: 10-50% probability in next 12 months

- Known threat actors but not actively targeting
- Some preventive controls, gaps identified
- Occasional incidents or near-misses

**High (3)**: >50% probability in next 12 months

- Active threats in this area
- Weak or missing preventive controls
- Recent incidents or ongoing vulnerability

### Impact Assessment

**Low (1)**: <$10k financial impact

- Minimal customer impact (< 100 users, < 1 hour)
- No regulatory reporting required
- Internal data only, limited scope
- Quick recovery (< 4 hours)

**Medium (2)**: $10k-$100k financial impact

- Moderate customer impact (100-1000 users, 1-8 hours)
- Possible regulatory notification
- Limited customer/employee data exposure
- Recovery within 24 hours

**High (3)**: >$100k financial impact

- Significant customer impact (>1000 users, >8 hours)
- Required regulatory breach notification
- Material data breach (PII, credentials, financial)
- Extended recovery (>24 hours) or data loss

### Risk Level Matrix

| Score | Level | Response Time | Decision Authority |
| ----- | ----- | ------------- | ------------------ |
| 1-2 | Low | Accept or mitigate opportunistically | Security Team |
| 3-4 | Medium | Mitigate within 90 days | Security + Engineering Lead |
| 6 | High | Mitigate within 30 days | CTO/Executive |
| 9 | Critical | Mitigate within 7 days | CEO/Board |

See [Risk Management Charter](../charter/risk-management.md#decision-authority) for approval requirements.

## Steps

### 1. Preparation (Week 1)

**Security Team**:

- Schedule interviews with all department heads and key technical leads
- Review previous year's risk register for closed/ongoing risks
- Gather inputs: recent [incidents](security-incident-response.md), [audit findings](external-audit.md), vulnerability scans, threat intelligence
- Prepare risk assessment templates and scoring guides

### 2. Risk Identification (Weeks 2-4)

**Security Team facilitates**:

- Interview each department (30-60 min): What keeps you up at night? Recent close calls? Planned changes?
- Review architecture diagrams and data flows with Engineering
- Analyze [vendor assessments](vendor-risk-review.md) for third-party risks
- Review compliance requirements for regulatory risks
- Examine incident trends for systemic issues

**Output**: Initial risk list with descriptions, categories, affected systems/data, potential impact

### 3. Risk Scoring (Week 5)

**Security Team with risk owners**:

- Score each risk for likelihood and impact using methodology above
- Calculate risk score (L × I)
- Validate scores with technical leads and department heads
- Document scoring rationale for each High/Critical risk

**Output**: Scored risk register with severity levels

### 4. Treatment Planning (Week 6)

**For each risk, identify treatment**:

- **Mitigate**: Define specific controls, assign owner, set deadline based on severity
- **Accept**: Document rationale, obtain required approval, set review date
- **Avoid**: Identify alternative approach that eliminates risk
- **Transfer**: Identify insurance, outsourcing, or contractual transfer option

**Output**: Treatment plan for each risk with owner and timeline

### 5. Review & Approval (Week 7)

**Security Team presents to Executive Sponsor**:

- High/Critical risks with treatment plans
- Medium risks requiring resource allocation
- Accepted risks requiring formal approval
- Risk trends vs previous year

**Executive approves**: Resource allocation, high-risk acceptances, escalations to Board

**Output**: Approved risk register and remediation roadmap

### 6. Ongoing Monitoring

**Monthly**: Security Team + Engineering Leadership review new risks and remediation progress per [Governance Communication](../charter/governance.md#communication)

**Quarterly**: Security Committee reviews all open risks, trends, stalled items

**Annually**: Repeat full assessment process

## Frequency

**Annual comprehensive assessment**: 7-week process documented above

**Continuous updates**: Add risks as identified via [security design reviews](security-design-review.md), [vendor reviews](vendor-risk-review.md), [incidents](security-incident-response.md)

**Reassessment triggers**: Major architecture changes, new compliance requirements, significant incidents, material business changes

## Tools

**Risk Register**: Spreadsheet or GRC tool tracking ID, description, category, likelihood, impact, score, owner, status, treatment, approval, dates

**Interview Templates**: Standardized questions for department heads and technical leads

**Scoring Guide**: This document's methodology with examples for consistency

**Reporting Dashboard**: Risk trends, aging, remediation velocity for [Governance Metrics](../charter/governance.md#metrics)

---

## Control Mapping

---

## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*
