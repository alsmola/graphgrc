---
type: process
title: Security Code Review
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Security Code Review

Manual peer review of code changes for security vulnerabilities before merge to production. Complements automated scanning with human judgment on business logic flaws, authentication/authorization issues, and context-specific risks. Implements secure development practices per [Engineer Policy](../policies/engineer.md).

## Scope

**Requires security-focused code review** (in addition to standard peer review):

- Authentication/authorization logic changes
- Cryptographic implementations or key management
- Payment processing or financial transactions
- Data export, import, or migration features
- Admin/privileged functionality
- External API integrations with data sharing
- Database query construction (SQL injection risk)
- File upload/download features
- Code flagged by SAST tools with potential false positives needing validation
- Changes implementing security design review findings (see [Security Design Review](security-design-review.md))

**Standard peer review sufficient** (no dedicated security review):

- Bug fixes in existing security-reviewed code
- UI/frontend changes with no backend logic
- Documentation, tests, configuration (non-security)
- Refactoring maintaining existing security posture

**All code** requires automated security scanning (SAST/dependency scanning) regardless of manual review scope.

## Roles

**Code Author** ([Engineer](../policies/engineer.md)): Writes secure code per coding standards, runs SAST locally, addresses findings before PR, requests security review when in scope, responds to reviewer feedback.

**Peer Reviewer** (Engineer): Reviews all code for correctness and security, flags security concerns for Security Team if uncertain, verifies SAST findings addressed.

**Security Reviewer** ([Security Team](../policies/security-team.md)): Reviews high-risk code changes, provides security-specific feedback, approves or requests changes, educates developers on secure patterns. Reviews within 2 business days.

**Security Tools** (SAST/DAST): Automatically scan code for known vulnerability patterns, dependency vulnerabilities, secrets in code. Block merge on Critical findings.

## Steps

### 1. Author Prepares Code

**Engineer writes code** following secure coding standards:

- Input validation on all user-supplied data
- Parameterized queries for database access (prevent SQL injection)
- Output encoding to prevent XSS
- Authentication/authorization checks before sensitive operations
- No secrets hardcoded in code (use [Secrets Management](../controls/iam/secrets-management.md))
- Proper error handling (don't expose sensitive info in errors)
- Secure dependencies (no known vulnerabilities)

**Author runs local checks**:

- SAST scan passes (or findings documented as false positives)
- Dependency scan shows no Critical/High vulnerabilities
- Unit tests include security test cases (auth bypass attempts, injection attempts)
- Manual verification of security-relevant logic

**Author creates PR** with:

- Clear description of what changed and why
- Security considerations documented
- SAST findings addressed or marked false positive with justification
- Self-assessment: "Requires security review" checkbox if in scope per above

### 2. Automated Security Scanning

**CI/CD pipeline runs** on PR creation:

- **SAST** (static analysis): Scans code for vulnerability patterns (injection, XSS, insecure crypto, hardcoded secrets)
- **Dependency scanning**: Checks libraries for known CVEs
- **Secret scanning**: Detects accidentally committed credentials, API keys, tokens
- **License compliance**: Flags incompatible open source licenses

**Automated gates**:

- **Block merge** on: Critical vulnerabilities, secrets detected, incompatible licenses
- **Warn but allow** on: Medium/Low findings (require reviewer acknowledgment)
- **Pass** on: No findings or all findings marked as accepted risk

**Author addresses findings**:

- Fix true positives (remediate vulnerability)
- Mark false positives with justification (reviewer must validate)
- Document accepted risks (link to risk register for known technical debt)

### 3. Peer Code Review

**Peer reviewer examines code** for:

**Functional correctness**:

- Does code do what it's supposed to?
- Edge cases handled?
- Error conditions handled gracefully?

**Security considerations**:

- Authentication required where needed?
- Authorization checks appropriate (not just authentication)?
- Input validation comprehensive (whitelist approach, not blacklist)?
- Sensitive data logged or exposed in errors?
- Race conditions or concurrent access issues?

**Reviewer provides feedback**:

- **Request changes**: Security issues found, must be fixed before merge
- **Comment**: Suggestions or questions, not blocking
- **Approve**: Code looks good, including security aspects

**If uncertain about security**, peer reviewer requests Security Team review by adding "security-review" label or @mentioning security team.

### 4. Security Team Review (High-Risk Changes)

**Security reviewer deep-dives** on security-sensitive code:

**Authentication/Authorization review**:

- Is authentication enforced at the right layer (API, not just UI)?
- Authorization checks on every sensitive resource access?
- Session management secure (timeout, secure cookies, CSRF protection)?
- Role checks properly implemented (not bypassable)?

**Data handling review**:

- Sensitive data encrypted in transit (see [Encryption in Transit](../controls/cryptography/encryption-in-transit.md))?
- Sensitive data encrypted at rest where required (see [Encryption at Rest](../controls/cryptography/encryption-at-rest.md))?
- Data access logged for audit trail?
- PII handling compliant with privacy requirements?

**Injection prevention**:

- SQL queries use parameterized statements (not string concatenation)?
- User input validated before processing (whitelist preferred)?
- Output encoded for context (HTML, JSON, SQL, etc.)?
- Command execution properly escaped or avoided?

**Cryptography review**:

- Using approved algorithms (AES-256, RSA-2048+, SHA-256+)?
- No custom crypto implementations?
- Keys managed properly (see [Key Management](../controls/cryptography/key-management.md))?
- Random number generation cryptographically secure?

**Security reviewer provides feedback**:

- **Approve**: Security looks good, merge when ready
- **Request changes**: Security issues must be fixed
- **Comment**: Suggestions for improvement, educational feedback

**Follow-up**: If changes requested, author addresses and re-requests review. Security Team re-reviews within 1 business day.

### 5. Merge & Monitor

**After all approvals**, code merged to main/production branch.

**Post-merge validation**:

- Deployment succeeds
- Automated tests pass in production environment
- Security-relevant configuration verified (encryption enabled, auth enforced)
- Monitoring/alerting configured for new endpoints or features

**If security issues discovered post-merge**:

- Assess severity using [Risk Scoring](organizational-risk-assessment.md#risk-scoring-methodology)
- **Critical/High**: Immediate hotfix or rollback, treat as security incident
- **Medium/Low**: Document in risk register, schedule fix in next sprint

**Security Team tracks metrics** per [Governance Metrics](../charter/governance.md#metrics):

- Security review turnaround time (target <2 business days)
- Findings by severity (track reduction over time as engineers learn)
- Re-review rate (indicates code quality improving or declining)
- Post-merge security issues (should trend toward zero)

---

## Control Mapping

---

## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*
