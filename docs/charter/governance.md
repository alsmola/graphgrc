---
type: charter
title: Governance
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
audience: leadership
---

# Governance

Strategic framework for the organization's information security program. Defines ownership, principles, scope, and metrics for protecting organizational and customer assets.

## Ownership

**Executive Sponsor** (CTO/CEO): Program approval, resource allocation, risk acceptance authority. Reviews high/critical risks monthly.

**Security Team**: Policy development, [risk assessments](../processes/organizational-risk-assessment.md), control monitoring, [incident response](../processes/security-incident-response.md), [compliance management](../processes/external-audit.md). See [Security Team Policy](../policies/security-team.md).

**Engineering Leadership** (SVP Engineering): Implements security controls, [secure development practices](../processes/security-code-review.md), vulnerability remediation. See [Engineer Policy](../policies/engineer.md).

**IT Operations**: [Endpoint security](../policies/it-administrator.md), [access management](../processes/access-review.md), system hardening.

**HR**: Personnel security, security training, [data privacy](../processes/personal-data-request.md). See [HR Administrator Policy](../policies/hr-administrator.md).

**All Employees**: Follow [security policies](../policies/employee.md), complete training, report incidents.

## Communication

**Security Committee** (Quarterly): Executive Sponsor, Security Team, Engineering Leadership, IT Ops, HR. Reviews risk posture, metrics, compliance status, major initiatives.

**Incident Response Team** (On-demand): Security Team lead, Engineering on-call, IT Ops, Legal/PR. Activated per [Security Incident Response](../processes/security-incident-response.md).

**Risk Review** (Monthly): Security Team, Engineering Leadership. Discuss open risks, remediation progress, new assessments. Documented in risk register.

**All-Hands Updates** (Quarterly): Security Team presents metrics, major changes, security awareness topics.

## Security Principles

**Risk-Based**: Focus resources on highest risks (likelihood × impact). See [Risk Management Charter](risk-management.md) for methodology.

**Defense in Depth**: Multiple overlapping controls, no single point of failure, assume breach mentality.

**Least Privilege**: Minimum access necessary, regular [access reviews](../processes/access-review.md), time-bound permissions.

**Security by Design**: [Security design reviews](../processes/security-design-review.md) before development, secure defaults, [threat modeling](risk-management.md) for high-risk systems.

**Transparency**: Clear ownership, blameless incident culture, visible security posture, documented decisions.

## Scope

**Systems**: All cloud infrastructure, SaaS applications, endpoints, networks, development environments.

**Data**: Customer data, employee data, business data, source code. All classifications and locations.

**People**: Employees, contractors, vendors, partners. All roles and locations.

**Processes**: Development, operations, sales, support, HR. Security integrated throughout.

## Metrics

**Vulnerability Management**:

- MTTR by severity: Critical <7d, High <30d, Medium <90d
- Open Critical/High vulnerabilities: Target 0/5

**Access & Identity**:

- [Access review](../processes/access-review.md) completion: 100% quarterly
- MFA adoption: 100% for production systems

**Security Awareness**:

- Training completion: 100% annually
- Phishing simulation click rate: <5%

**Incident Response**:

- [Incident](../processes/security-incident-response.md) detection time: <1 hour for critical
- Mean time to containment: <4 hours for critical

**Compliance**:

- [SOC 2](../processes/external-audit.md) audit findings: 0 exceptions
- [Internal audit](../processes/internal-audit.md) completion: 100% quarterly
- Control effectiveness: >95%

**Risk Management**:

- Open high/critical risks: Trend down
- Risk remediation SLA compliance: >90%
- See [Risk Management Charter](risk-management.md) for scoring methodology

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Security Policies](../controls/governance/security-policies.md) ^[Establishes governance framework with clear ownership, principles (risk-based, defense in depth, least privilege), and scope]
- [Risk Assessment](../controls/governance/risk-assessment.md) ^[Risk-based approach with focus on highest risks (likelihood × impact), monthly risk reviews, documented risk register]
- [Organizational Risk Assessment](../controls/risk-management/organizational-risk-assessment.md) ^[Risk review process with Security Committee quarterly, monthly risk reviews with Engineering Leadership]
- [Vendor Risk Management](../controls/risk-management/vendor-risk-management.md) ^[Vendor security assessment process, third-party risk management framework]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Incident Response Team structure, detection time <1 hour for critical, containment <4 hours for critical]
- [Incident Response Exercises](../controls/incident-response/incident-response-exercises.md) ^[Blameless incident culture, security awareness through incident learnings]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA adoption target of 100% for production systems]
- [Security Awareness Training](../controls/security-training/security-awareness-training.md) ^[Training completion 100% annually, phishing simulation click rate <5%]
- [External Audits](../controls/compliance/external-audits.md) ^[SOC 2 audit findings target 0 exceptions, control effectiveness >95%]
- [Internal Audits](../controls/compliance/internal-audits.md) ^[Internal audit completion 100% quarterly]
