---
type: standard
id: standard-github-security
title: GitHub Security Standard
owner: engineering-team
last_reviewed: 2025-01-09
review_cadence: quarterly
applies_to: [engineers]
---

# GitHub Security Standard

Baseline security requirements for GitHub organizations and repositories.

## Scope

All repositories in the organization's GitHub organization(s).

## Requirements

### Organization Settings

- Require 2FA for all organization members
- Restrict repository creation to admins
- Enable Dependency Graph and Dependabot alerts
- Enable Secret Scanning (GitHub Advanced Security)
- Default repository permission: Read (not Write)

### Repository Protection

- Require branch protection on `main`/`master`:
  - Require pull request reviews (minimum 1 approval)
  - Require status checks to pass
  - Require conversation resolution before merge
  - No force pushes or deletions
- Protected branches cannot be bypassed by admins
- Enable "Require signed commits" for sensitive repos

### Access Control

- Use GitHub Teams for access management (not individual invites)
- Follow least privilege: Read by default, Write when needed, Admin sparingly
- External collaborators must be approved by security team
- Quarterly access reviews of organization members

### Secrets Management

- No secrets in code (enforced by pre-commit hooks and secret scanning)
- Use GitHub Actions secrets for CI/CD credentials
- Rotate secrets when team members leave
- Use environment protection rules for production deployments

### CI/CD Security

- GitHub Actions:
  - Pin actions to SHA (not tags)
  - No secrets in PR builds from forks
  - Use OIDC for cloud provider authentication (not long-lived keys)
  - Require workflow approval for first-time contributors
- Third-party integrations require security review

### Audit and Monitoring

- Enable audit log streaming to SIEM
- Alert on sensitive actions: member added, permissions changed, secrets accessed
- Review security advisories weekly

## References

- Related controls: ACC-01, ACC-02, INF-01, OPS-01
- GitHub Security Best Practices: https://docs.github.com/en/code-security

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Identity & Authentication](../controls/iam/identity-authentication.md) ^[Require 2FA for all GitHub organization members, SSO integration for authentication]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[2FA mandatory for all organization members, no exceptions]
- [Single Sign-On](../controls/iam/single-sign-on.md) ^[SSO integration with organizational identity provider]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[GitHub Teams for access management, Read by default, Write when needed, Admin sparingly]
- [Access Reviews](../controls/iam/access-reviews.md) ^[Quarterly access reviews of organization members and external collaborators]
- [Secrets Management](../controls/iam/secrets-management.md) ^[No secrets in code enforced by pre-commit hooks and secret scanning, GitHub Actions secrets for CI/CD]
- [Change Management](../controls/operational-security/change-management.md) ^[Branch protection on main/master, require PR reviews (min 1 approval), require status checks, no force pushes]
- [Automated Code Analysis](../controls/security-engineering/automated-code-analysis.md) ^[Dependency Graph and Dependabot alerts, secret scanning enabled]
- [Secure Code Review](../controls/security-engineering/secure-code-review.md) ^[Pull request reviews required before merge, conversation resolution required]
- [Cloud Vulnerability Detection](../controls/vulnerability-management/cloud-vulnerability-detection.md) ^[Security advisories reviewed weekly, Dependabot alerts for dependency vulnerabilities]
- [SaaS Hardening](../controls/configuration-management/saas-hardening.md) ^[Repository creation restricted to admins, default repository permission Read, protected branches cannot be bypassed]

---

<!-- Backlinks auto-generated below -->
