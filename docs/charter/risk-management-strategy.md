---
type: charter
title: Risk Management Strategy
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
audience: leadership
---

# Risk Management Strategy

Framework for identifying, assessing, and managing information security and privacy risks.

## Purpose

Define the organization's approach to risk management, including risk appetite, assessment methodology, and decision-making processes.

## Risk Management Philosophy

### Risk-Informed, Not Risk-Averse

- Security exists to enable business, not prevent it
- Accept calculated risks when business value outweighs security concerns
- Balance security with usability, performance, and cost
- Make informed risk decisions with data and analysis

### Continuous Risk Management

- Risk management integrated into daily operations (not annual exercise)
- Monitor evolving threats and vulnerabilities
- Reassess risks when environment changes (new technology, new threats)
- Learn from incidents and near-misses

### Shared Responsibility

- Security team owns risk framework, but risk management is everyone's job
- Engineering teams assess technical risks
- Business teams assess business impact
- Leadership makes risk acceptance decisions

## Risk Appetite

### Definition

Risk appetite is the level of risk the organization is willing to accept in pursuit of business objectives.

### Overall Risk Appetite: Moderate

- **Low tolerance** for risks affecting customer data confidentiality or privacy (GDPR violations, data breaches)
- **Moderate tolerance** for availability risks (some downtime acceptable if mitigations in place)
- **Moderate tolerance** for emerging technology risks (experiment with new tech, but not in production without controls)
- **High tolerance** for internal operational risks (flexible internal tools and processes)

### Risk Thresholds

- **Critical risks:** Unacceptable - must remediate immediately or escalate for acceptance
- **High risks:** Require executive approval to accept, with compensating controls and monitoring
- **Medium risks:** Acceptable with documented mitigation plan and timeline
- **Low risks:** Acceptable, track and reassess periodically

## Risk Assessment Methodology

### Risk Scoring

**Likelihood:**
- **Low (1):** Unlikely to occur (< 10% annual probability)
- **Medium (2):** Possible (10-50% annual probability)
- **High (3):** Likely (> 50% annual probability)

**Impact:**
- **Low (1):** Minimal impact (< $10k loss, < 1 hour downtime, no customer impact)
- **Medium (2):** Moderate impact ($10k-$100k loss, 1-4 hour downtime, limited customer impact)
- **High (3):** Severe impact (> $100k loss, > 4 hour downtime, major customer impact, regulatory fine, reputational damage)

**Risk Score = Likelihood × Impact**

| Score | Risk Level | Response |
|-------|------------|----------|
| 1-2   | Low        | Accept or mitigate opportunistically |
| 3-4   | Medium     | Mitigate within 90 days |
| 6     | High       | Mitigate within 30 days or escalate for acceptance |
| 9     | Critical   | Mitigate immediately (< 7 days) or executive acceptance required |

### Risk Assessment Triggers

Conduct risk assessment when:
- Starting new project or initiative (design phase)
- Adopting new technology or vendor
- Regulatory or compliance changes
- Security incident (post-incident review)
- Annually (comprehensive program review)

## Risk Treatment Options

### 1. Mitigate (Reduce)

Implement controls to reduce likelihood or impact.

**Examples:**
- Deploy WAF to reduce likelihood of web attacks
- Implement backups to reduce impact of ransomware
- Add MFA to reduce likelihood of account compromise

**When to use:** Most common approach for Medium/High risks

### 2. Accept (Retain)

Acknowledge risk and proceed without additional controls.

**Requirements:**
- Document risk in risk register
- Obtain approval from appropriate level (see Risk Decision Authority)
- Set review date (quarterly for High risks, annually for Medium/Low)

**When to use:** Low risks, or when mitigation cost exceeds impact

### 3. Avoid (Eliminate)

Change approach to eliminate the risk entirely.

**Examples:**
- Don't collect PII if not needed (avoid GDPR risk)
- Don't build feature if security risk too high
- Don't use vendor with inadequate security posture

**When to use:** Critical risks that can't be adequately mitigated

### 4. Transfer (Share)

Shift risk to third party (insurance, outsourcing).

**Examples:**
- Cyber insurance for data breach response costs
- Use managed security services instead of building in-house
- Contractual indemnification from vendors

**When to use:** Financial risks, specialized capabilities

## Risk Decision Authority

| Risk Level | Decision Authority | Approval Required |
|------------|-------------------|-------------------|
| Low | Security Team | Document in risk register |
| Medium | Security Team + Engineering/Business Lead | Email or Slack approval |
| High | CTO or Executive Team | Written approval, quarterly review |
| Critical | CEO or Board | Formal approval, monthly review |

## Risk Register

### What to Track

- **Risk ID:** Unique identifier (RISK-001)
- **Description:** What is the risk?
- **Category:** Technical, Process, People, Third-Party, Compliance
- **Likelihood and Impact:** Scoring and justification
- **Risk Score:** Calculated score
- **Owner:** Who is responsible for managing this risk?
- **Status:** Open, Accepted, Mitigated, Closed
- **Treatment Plan:** What controls are being implemented?
- **Target Date:** When will mitigation be complete?
- **Review Date:** When to reassess

### Risk Register Review

- **Monthly:** New risks and status updates
- **Quarterly:** Full review of all open risks, reassess scores
- **Annually:** Comprehensive review, sunset closed risks

## Risk Scenarios

### Examples of Assessed Risks

**RISK-001: AWS Account Compromise**
- **Description:** Attacker gains access to production AWS account via compromised credentials
- **Likelihood:** Low (MFA enabled, limited access)
- **Impact:** High (access to customer data, potential data breach)
- **Score:** 3 (Low × High)
- **Mitigation:** MFA enforced, CloudTrail monitoring, quarterly access reviews
- **Status:** Mitigated

**RISK-002: Unpatched Critical Vulnerability**
- **Description:** Critical vulnerability in application dependency not patched within SLA
- **Likelihood:** Medium (delays in patching process)
- **Impact:** Medium (potential RCE, but requires authenticated access)
- **Score:** 4 (Medium × Medium)
- **Mitigation:** Improve patch management process, automated dependency updates
- **Status:** In Progress

**RISK-003: Third-Party Data Breach**
- **Description:** Vendor with access to customer data suffers data breach
- **Likelihood:** Low (vendors SOC 2 certified, DPAs in place)
- **Impact:** High (customer data exposed, GDPR notification required)
- **Score:** 3 (Low × High)
- **Mitigation:** Vendor risk assessments, annual reviews, contractual breach notification
- **Status:** Accepted (residual risk after controls)

## Integration with Development

### Security Design Review

All new features/projects assessed for security risks before development starts.

**Process:**
1. Engineering submits design document
2. Security team reviews for risks (authentication, data access, third-party integrations)
3. Risk assessment performed (likelihood and impact)
4. Mitigation controls identified and added to requirements
5. Approval to proceed or request design changes

### Threat Modeling

For high-risk systems (authentication, payment processing, data processing):
- Identify assets and trust boundaries
- Enumerate threats (STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Assess likelihood and impact
- Identify mitigations

## Compliance Risk Management

### Regulatory Risks

- **GDPR non-compliance:** Fines up to 4% of revenue, reputational damage
- **SOC 2 audit failures:** Customer trust erosion, deal delays
- **Contractual security obligations:** Customer SLA breaches, financial penalties

### Mitigation Approach

- Maintain compliance program with continuous monitoring
- Map controls to regulatory requirements
- Regular internal audits and gap assessments
- Legal review of new processing activities

## Emerging Risks

Monitor and assess emerging threats:
- AI/ML security (adversarial attacks, data poisoning)
- Supply chain attacks (SolarWinds-style compromises)
- Cloud misconfigurations (as infrastructure scales)
- Insider threats (as company grows)

## Risk Communication

### Internal Communication

- **Security team:** Daily risk discussions, weekly risk triage
- **Engineering leadership:** Monthly risk dashboard
- **Executive team:** Quarterly risk report (top 5 risks, trends, mitigation progress)
- **Board:** Annual comprehensive risk review

### External Communication

- **Customers:** Security posture shared via website, SOC 2 report
- **Prospects:** Security questionnaires during sales process
- **Regulators:** Breach notifications if required (GDPR 72 hours)

## Metrics and Reporting

### Risk Metrics

- Number of open risks by severity
- Aging of risks (how long open)
- Risk remediation velocity (time to close)
- Risk acceptance rate (% of risks accepted vs. mitigated)

### Trend Analysis

- Are risks increasing or decreasing over time?
- Are we remediating faster than new risks emerge?
- Which categories have most risks (Technical, Process, Third-Party)?

## Review and Updates

This strategy reviewed annually and updated based on:
- Changes in business model or technology
- Major incidents or near-misses
- Regulatory changes
- Industry threat landscape evolution

## Related Documents

- Charter: information-security-program-charter.md
- Control: GOV-02 (Risk Assessment)
- Processes: incident-response-process.md, vendor-risk-assessment-process.md

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [GOV-02: Risk Assessment](../custom/gov-02.md) ^[Risk management framework: methodology (likelihood × impact scoring), risk appetite (moderate), treatment options (mitigate/accept/avoid/transfer), decision authority, risk register]
- [VEN-01: Third-Party Risk Assessment](../custom/ven-01.md) ^[Risk scenario: third-party data breach, vendor risk assessments as mitigation]
- [OPS-03: Incident Response](../custom/ops-03.md) ^[Risk assessment triggered by security incidents in post-incident review]

---

<!-- Backlinks auto-generated below -->
## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*

