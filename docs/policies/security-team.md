---
type: policy
title: Security Team Policy
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
applies_to: security-team
---

# Security Team Policy

Security requirements and responsibilities for security team members.

## Extends

All requirements from Employee Security Policy plus Engineer Security Policy plus:

## Security Operations

- Monitor security alerts and respond within SLA
- Triage vulnerabilities and assign remediation owners
- Conduct security reviews for high-risk changes
- Perform incident response and root cause analysis
- Maintain security documentation (policies, standards, runbooks)

## Risk Management

- Assess risks for new projects and vendors
- Maintain risk register
- Escalate high/critical risks to leadership
- Track risk remediation progress
- Report on security metrics

## Compliance

- Maintain SOC 2 compliance controls
- Prepare for external audits
- Respond to customer security questionnaires
- Track compliance obligations (GDPR, contractual)
- Conduct internal audits

## Privileged Access

- Access production for security investigations only
- Document reason for production access
- Use separate security admin accounts
- All production access logged and reviewed
- No standing production access (just-in-time only)

## Confidential Information

- Protect security incident details (need-to-know basis)
- Do not disclose vulnerabilities publicly before remediation
- Handle audit findings confidentially
- Coordinate disclosure with Legal/PR

## Tools and Access

- Access to security tools (SIEM, vulnerability scanners, EDR consoles)
- Admin access to identity providers
- Cloud security admin access
- Endpoint management console access

## Continuous Learning

- Stay current on threat landscape
- Participate in security conferences
- Share knowledge with team
- Contribute to security community

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Monitor security alerts and respond within SLA, perform incident response and root cause analysis]
- [Vulnerability Management Process](../controls/vulnerability-management/vulnerability-management-process.md) ^[Triage vulnerabilities and assign remediation owners, track remediation progress]
- [Security Reviews](../controls/security-assurance/security-reviews.md) ^[Conduct security reviews for high-risk changes, assess risks for new projects and vendors]
- [Organizational Risk Assessment](../controls/risk-management/organizational-risk-assessment.md) ^[Maintain risk register, escalate high/critical risks to leadership, track remediation progress, report on security metrics]
- [Vendor Risk Management](../controls/risk-management/vendor-risk-management.md) ^[Assess risks for new vendors, respond to customer security questionnaires]
- [External Audits](../controls/compliance/external-audits.md) ^[Maintain SOC 2 compliance controls, prepare for external audits]
- [Internal Audits](../controls/compliance/internal-audits.md) ^[Conduct internal audits, track compliance obligations (GDPR, contractual)]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Maintain security documentation (policies, standards, runbooks)]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Access production for security investigations only, document reason, use separate admin accounts, no standing production access (JIT only)]
- [SIEM](../controls/monitoring/siem.md) ^[Access to SIEM, vulnerability scanners, EDR consoles for security monitoring]
- [Cloud IAM](../controls/iam/cloud-iam.md) ^[Cloud security admin access for investigations and security configuration]
- [Security Awareness Training](../controls/security-training/security-awareness-training.md) ^[Stay current on threat landscape, participate in conferences, share knowledge, contribute to security community]
- [Insider Threat Mitigation](../controls/personnel-security/insider-threat-mitigation.md) ^[Security team monitors SIEM/UEBA for anomalous activity, coordinates with HR on terminations, enforces least privilege and separation of duties]
