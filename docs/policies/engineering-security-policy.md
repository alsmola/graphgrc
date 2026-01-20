---
type: policy
title: Engineering Security Policy
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: engineers
---

# Engineering Security Policy

Security requirements specific to software engineers and developers.

## Purpose

This policy establishes secure development practices to prevent security vulnerabilities in code and infrastructure. Applies in addition to the baseline-security-policy.md.

## Scope

Applies to all engineers, including software engineers, SREs, DevOps engineers, and contractors writing code or managing infrastructure.

## Secure Coding

### Requirements

- Follow secure coding practices for your language/framework (OWASP guidelines)
- Validate and sanitize all user inputs (prevent injection attacks)
- Use parameterized queries for database access (no string concatenation in SQL)
- Implement proper authentication and authorization checks
- Handle errors securely (no sensitive information in error messages)
- Use secure defaults (deny by default, opt-in to permissions)
- Keep dependencies up to date (address Dependabot/Snyk alerts within SLA)

### Responsibilities

- Review OWASP Top 10 vulnerabilities annually
- Use linting tools and security scanners in your IDE
- Write security tests for critical functionality (auth, authz, data access)
- Consider security implications during code review
- Attend annual secure coding training

## Secrets Management

### Requirements

- **Never commit secrets to Git** (API keys, passwords, tokens, private keys)
- Use environment variables or secrets management service (AWS Secrets Manager, Parameter Store)
- Rotate secrets when team members leave or credentials compromised
- Use short-lived credentials where possible (IAM roles, OAuth tokens)
- Scope secrets to minimum required permissions (least privilege)

### Responsibilities

- Use pre-commit hooks to prevent secret commits (detect-secrets, gitleaks)
- If you accidentally commit a secret: Revoke it immediately, rotate, notify security team
- Never share secrets in Slack, email, or ticketing systems
- Use `git-secrets` or `trufflehog` to scan repositories

## Access Control

### Requirements

- Follow least privilege principle for AWS IAM roles and policies
- Use IAM roles, not IAM users with long-lived access keys
- No wildcard (*) permissions in production
- Request access only for systems you actively work on
- Use separate AWS accounts for dev/staging/production

### Responsibilities

- Review IAM policies before creating or modifying
- Remove unused IAM roles and policies
- Use temporary credentials (AWS STS AssumeRole)
- Avoid overly permissive policies (least privilege)

## Code Review

### Requirements

- All code changes require peer review before merge (minimum 1 approval)
- Security-sensitive changes require security team review (auth, crypto, data access)
- Review for security issues during code review (injection, XSS, auth bypass, secrets)
- Automated security scans must pass before merge (SAST, secret scanning, dependency check)

### Responsibilities

- Review code carefully, not just "rubber stamp" approval
- Ask questions if you don't understand security implications
- Suggest security improvements during review
- Block merges if security issues identified (use "Request Changes")

## Development Environments

### Requirements

- Use separate AWS accounts/projects for dev, staging, production
- Do not use production data in development (use synthetic data or anonymized backups)
- Production access restricted (read-only for most engineers, write access for on-call/SRE only)
- No production database queries from local laptop (use bastion/jump host)

### Responsibilities

- Test in dev/staging before deploying to production
- Do not bypass controls to "move fast" (shortcuts lead to incidents)
- Request production access only when on-call or troubleshooting incident

## Dependency Management

### Requirements

- Review dependencies before adding to project (check reputation, maintenance, license)
- Keep dependencies up to date (automated updates via Dependabot/Renovate)
- Address Critical/High severity vulnerabilities within SLA (see vulnerability-management-standard.md)
- Pin direct dependencies to specific versions (lockfiles: package-lock.json, go.sum, requirements.txt)

### Responsibilities

- Review and merge Dependabot PRs promptly
- Investigate and document risk exceptions for vulnerabilities that can't be immediately patched
- Avoid using abandoned or unmaintained dependencies
- Prefer well-known, actively maintained libraries over obscure packages

## Infrastructure as Code

### Requirements

- All infrastructure defined as code (Terraform, CloudFormation, etc.)
- Infrastructure changes reviewed and approved before deployment
- Use security scanning for IaC (tfsec, checkov, cfn_nag)
- No manual infrastructure changes in production (use CI/CD)
- Store IaC in version control (Git)

### Responsibilities

- Follow security best practices in IaC (encryption, least privilege, network isolation)
- Review Terraform plans before applying
- Use modules and reusable templates for consistency
- Document infrastructure architecture

## Testing

### Requirements

- Write unit tests for critical functionality (especially auth, data access)
- Automated tests run in CI/CD pipeline before merge
- Security tests cover common vulnerabilities (OWASP Top 10)
- Do not disable security checks to make tests pass

### Responsibilities

- Achieve reasonable test coverage (aim for 70%+ on critical paths)
- Test error handling and edge cases (not just happy path)
- Test with malicious inputs (fuzzing, boundary testing)
- Update tests when fixing security issues (regression tests)

## Deployment Security

### Requirements

- Deploy through CI/CD pipeline (no manual deployments to production)
- Use signed container images (Docker Content Trust)
- Verify checksums/signatures for downloaded binaries
- Rollback plan required for high-risk changes

### Responsibilities

- Monitor deployments for errors and anomalies
- Use blue/green or canary deployments for risk mitigation
- Test rollback procedures periodically

## Incident Response

### Requirements

- Engineers on-call must be familiar with incident response process
- Participate in incident response when paged (security incidents)
- Preserve evidence during incident (don't delete logs or modify systems without approval)

### Responsibilities

- Report security issues immediately (don't try to fix silently)
- Participate in post-incident reviews (blameless culture)
- Implement preventive controls after incidents

## Third-Party Integrations

### Requirements

- New integrations require security review (especially with access to customer data)
- Use OAuth instead of API keys where possible (scoped, revocable)
- Follow principle of least privilege for integration permissions
- Document all third-party integrations (what data is shared, why)

### Responsibilities

- Review third-party security posture (SOC 2, security documentation)
- Limit data shared with third parties to minimum necessary
- Monitor third-party access logs for anomalies

## Personal Projects and Open Source

### Requirements

- Do not commit company code to personal repositories
- Do not use company resources (AWS credits, licenses) for personal projects
- Get approval before open-sourcing company code
- Ensure open source contributions don't expose company IP or vulnerabilities

### Responsibilities

- Be mindful of what you commit to public repositories
- Do not copy-paste code from company repositories to Stack Overflow or GitHub issues
- Use personal email for personal GitHub activity (not @company.com email)

## Exceptions

Exceptions to this policy require written approval from Security Team Lead with business justification. Approved exceptions documented and reviewed quarterly.

## Training

- Complete annual secure coding training (OWASP, language-specific training)
- Attend security talks and workshops (internal or external)
- Review security incidents and lessons learned

## Related Documents

- Standards: aws-security-standard.md, github-security-standard.md, cryptography-standard.md
- Processes: change-management-process.md, vulnerability-management-process.md
- General policy: baseline-security-policy.md

## References

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- CWE Top 25 Most Dangerous Software Weaknesses: https://cwe.mitre.org/top25/

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Secure Coding Standards](../controls/security-engineering/secure-coding-standards.md) ^[Follow OWASP guidelines, validate inputs, parameterized queries, secure defaults, handle errors securely]
- [Secure Code Review](../controls/security-engineering/secure-code-review.md) ^[All code requires peer review (min 1 approval), security review for sensitive changes, review for injection/XSS/auth bypass]
- [Automated Code Analysis](../controls/security-engineering/automated-code-analysis.md) ^[SAST, secret scanning, dependency checks must pass before merge, use linting tools and security scanners in IDE]
- [Secrets Management](../controls/iam/secrets-management.md) ^[Never commit secrets to Git, use AWS Secrets Manager, rotate secrets on team member departure, use pre-commit hooks]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[IAM roles with least privilege, no wildcard permissions in production, temporary credentials via STS AssumeRole]
- [Cloud IAM](../controls/iam/cloud-iam.md) ^[Use IAM roles not IAM users, separate accounts for dev/staging/production, review policies before creating]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Production access restricted, read-only for most engineers, write access for on-call/SRE only, no direct DB queries from laptop]
- [Change Management](../controls/operational-security/change-management.md) ^[All code changes require peer review, automated tests in CI/CD, infrastructure changes reviewed before deployment]
- [Vulnerability Management Process](../controls/vulnerability-management/vulnerability-management-process.md) ^[Address Critical/High severity vulnerabilities within SLA, review dependencies before adding, keep dependencies up to date]
- [Cloud Vulnerability Detection](../controls/vulnerability-management/cloud-vulnerability-detection.md) ^[Automated dependency scanning with Dependabot/Snyk, container image scanning, IaC security scanning with tfsec/checkov]
- [Cloud Security Configuration (AWS)](../controls/infrastructure-security/cloud-security-configuration-aws.md) ^[All infrastructure as code (Terraform/CloudFormation), no manual production changes, use CI/CD for deployments]
- [Cloud Hardening](../controls/configuration-management/cloud-hardening.md) ^[Security best practices in IaC, review Terraform plans before applying, use modules for consistency]
- [Code Signing](../controls/cryptography/code-signing.md) ^[Use signed container images (Docker Content Trust), verify checksums/signatures for downloaded binaries]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Engineers on-call familiar with IR process, preserve evidence during incidents, participate in post-incident reviews]
- [Secure Coding Training](../controls/security-training/secure-coding-training.md) ^[Annual secure coding training (OWASP, language-specific), attend security talks, review incidents and lessons learned]

---

<!-- Backlinks auto-generated below -->
