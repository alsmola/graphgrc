---
type: process
title: Security Design Review
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Security Design Review

Proactive security assessment of new features, architecture changes, and systems before development. Identifies risks early when mitigation is cheapest. Implements [Risk Management Charter](../charter/risk-management.md#risk-identification) proactive assessment strategy.

## Scope

**Requires security design review**:

- New features handling customer data or authentication
- Architecture changes affecting production systems
- New third-party integrations with data sharing
- New data processing activities (GDPR relevance)
- Infrastructure changes affecting network boundaries or access controls
- Changes to cryptographic implementations
- New external APIs or services

**Does not require review** (engineering judgment sufficient):

- Bug fixes with no architectural impact
- UI/UX changes with no data handling changes
- Performance optimizations maintaining existing security posture
- Internal tooling with no production data access

When in doubt, request review. [Security Team](../policies/security-team.md) will triage and may fast-track low-risk changes.

## Roles

**Engineering Lead/Tech Lead**: Initiates review by submitting design document. Owns implementation of security requirements. Escalates timeline conflicts to Engineering Leadership.

**Security Team**: Facilitates review, performs threat modeling for high-risk systems, documents risks in risk register, provides security guidance. Reviews within 3 business days for standard changes, 5 days for complex changes.

**Product Owner**: Participates in review when security requirements impact feature scope or timeline. Approves trade-offs between security and business requirements.

**Privacy/Legal** (if applicable): Reviews data processing activities for GDPR compliance, contractual obligations, regulatory requirements.

## Steps

### 1. Submit Design Document

**Engineering submits** via design review template covering:

- **What**: Feature/change description, user stories, success criteria
- **Why**: Business justification, customer impact
- **How**: Architecture diagram, data flows, components involved
- **Data**: What data is processed, stored, transmitted? Classification (public, internal, confidential, restricted)?
- **Access**: Who/what systems access this data? Authentication/authorization approach?
- **Dependencies**: Third-party services, APIs, libraries, infrastructure changes
- **Risks**: Known concerns or trade-offs

Submit at least 5 business days before planned development start to allow time for risk mitigation planning.

### 2. Initial Triage (24 hours)

**Security Team** reviews submission and categorizes:

**Low risk** (no formal review needed):

- No customer data involved
- No authentication/authorization changes
- No new external integrations
- Standard patterns already approved

Security Team provides quick feedback via comment, marks approved.

**Standard risk** (3-day review):

- Customer data processing with standard controls
- Typical third-party integrations
- Infrastructure changes following existing patterns

**High risk** (5-day review + threat modeling):

- New authentication mechanisms
- Cryptographic implementations
- Cross-security-boundary data flows
- Novel architectures or technologies
- Privileged access implementations

### 3. Security Review

**Security Team analyzes** design for:

**Confidentiality risks**:

- Data exposure via API, logs, error messages, debugging tools
- Insufficient access controls or authorization bypass potential
- Unencrypted data in transit or at rest (see [Encryption in Transit](../controls/cryptography/encryption-in-transit.md), [Encryption at Rest](../controls/cryptography/encryption-at-rest.md))
- Secrets in code or configuration (see [Secrets Management](../controls/iam/secrets-management.md))

**Integrity risks**:

- Input validation gaps enabling injection attacks
- Insufficient authentication or session management
- CSRF, replay attacks, or tampering vulnerabilities
- Insecure dependencies or supply chain risks

**Availability risks**:

- Resource exhaustion or DoS potential
- Single points of failure
- Insufficient monitoring or alerting
- Missing backup/recovery mechanisms

**Compliance risks**:

- GDPR violations (data minimization, consent, retention)
- SOC 2 control gaps
- Contractual security obligations

**Output**: Security findings document with risk scores per [Risk Scoring Methodology](organizational-risk-assessment.md#risk-scoring-methodology).

**For high-risk designs, Security Team facilitates** collaborative threat modeling session (60-90 min) with Engineering using STRIDE methodology:

- **S**poofing: Can attacker impersonate legitimate user/system?
- **T**ampering: Can attacker modify data in transit or at rest?
- **R**epudiation: Can attacker deny actions or hide activity?
- **I**nformation Disclosure: Can attacker access unauthorized data?
- **D**enial of Service: Can attacker disrupt availability?
- **E**levation of Privilege: Can attacker gain unauthorized access?

**Output**: Threat model document with attack vectors, likelihood/impact assessment, mitigation strategies. Added to risk register.

### 5. Risk Acceptance & Mitigation Planning

**Security Team documents** each finding with:

- Risk description and affected components
- Likelihood and impact score
- Recommended mitigation (code change, configuration, compensating control)
- Risk acceptance option (if mitigation impractical)

**Engineering Lead reviews** findings and chooses treatment per [Risk Management](../charter/risk-management.md#risk-treatment):

- **Mitigate**: Implement recommended security control. Most common for Medium+ risks.
- **Accept**: Document in risk register, obtain approval per [Decision Authority](../charter/risk-management.md#decision-authority). Used when mitigation cost exceeds risk or timeline critical.
- **Avoid**: Change design to eliminate risk. Used when risk exceeds appetite.

**For accepted risks**: Security Team escalates per severity. High/Critical require CTO approval before proceeding.

### 6. Implementation & Validation

**Engineering implements** approved design with security requirements. Security-relevant changes flagged for [Security Code Review](security-code-review.md) during PR review.

**Security Team validates** implementation post-deployment:

- Configuration review (IAM policies, network rules, encryption settings)
- Spot-check against design review findings
- Verify monitoring/alerting configured
- Update risk register (close mitigated risks, track accepted risks)

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Security Reviews](../controls/security-assurance/security-reviews.md) ^[Security design review process before development: threat modeling, architecture review, security requirements, risk acceptance]
- [Organizational Risk Assessment](../controls/risk-management/organizational-risk-assessment.md) ^[Design review identifies risks for risk register, threat model drives risk assessment]
- [Secure Coding Standards](../controls/security-engineering/secure-coding-standards.md) ^[Design review establishes security requirements that inform coding standards]
- [Data Classification](../controls/data-management/data-classification.md) ^[Design review identifies data types and required classification levels]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[Design review determines encryption requirements based on data classification]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[Design review specifies TLS requirements for data transmission]
