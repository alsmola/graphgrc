---
type: process
title: Change Management Process
owner: engineering-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [engineers, infrastructure-team, security-team]
---

# Change Management Process

Process for managing changes to production systems to maintain security and stability.

## Roles and Responsibilities

- **Engineer:** Proposes and implements changes
- **Reviewer:** Reviews code/infrastructure changes (peer or senior engineer)
- **Infrastructure Team:** Approves infrastructure changes
- **Security Team:** Reviews security-sensitive changes

## Prerequisites

- Version control for all code and infrastructure (Git)
- CI/CD pipeline with automated testing
- Staging environment for pre-production testing

## Process Steps

### Step 1: Change Proposal

Engineer creates pull request or change ticket describing proposed change.

**PR/ticket includes:**
- Description of change and business justification
- Risk assessment (low/medium/high)
- Rollback plan
- Testing performed
- Security considerations (if applicable)

**Owner:** Engineer
**Duration:** Time to write PR description

### Step 2: Automated Testing

CI/CD pipeline runs automated tests on proposed change.

**Tests:**
- Unit tests
- Integration tests
- Security scanning (SAST, dependency check, secret scanning)
- Infrastructure validation (Terraform plan, CloudFormation validation)

**Gate:** All tests must pass before merge

**Owner:** Automated CI/CD
**Duration:** 5-15 minutes

### Step 3: Peer Review

One or more engineers review the change.

**Review criteria:**
- Code quality and maintainability
- Security best practices (input validation, authentication, etc.)
- Performance implications
- Test coverage adequate
- Documentation updated

**Approval required:** Minimum 1 approval for standard changes, 2 for high-risk

**Owner:** Peer Reviewer
**Duration:** Hours to days (depending on change size)

### Step 4: Security Review (if needed)

Security team reviews security-sensitive changes.

**Triggers for security review:**
- Authentication or authorization logic
- Cryptographic implementations
- Data access or privacy-related changes
- Third-party integrations
- Infrastructure changes affecting production security controls

**Owner:** Security Team
**Duration:** 1-2 business days

### Step 5: Staging Deployment

Change deployed to staging environment for validation.

**Validation:**
- Functional testing
- Performance testing
- Security testing (if needed)
- Verify no breaking changes

**Owner:** Engineer, QA (if applicable)
**Duration:** Hours to days

### Step 6: Production Deployment

Change deployed to production via CI/CD pipeline or manual deployment.

**Deployment requirements:**
- Merge to main branch triggers automated deployment (for low-risk changes)
- Manual deployment for high-risk changes (database migrations, infrastructure)
- Deploy during business hours (unless emergency)
- Engineer available for monitoring during rollout

**Deployment methods:**
- Blue/green deployment (zero downtime)
- Rolling deployment (gradual rollout)
- Feature flags (toggle new functionality)

**Owner:** Engineer, Infrastructure Team
**Duration:** Minutes to hours

### Step 7: Post-Deployment Verification

Engineer verifies change successful and monitors for issues.

**Verification:**
- Check application logs for errors
- Monitor metrics (error rate, latency, resource usage)
- Verify functionality in production
- User acceptance testing (if applicable)

**Monitoring period:** 30 minutes minimum

**Owner:** Engineer
**Duration:** 30 minutes - 2 hours

### Step 8: Rollback (if needed)

If issues detected, rollback to previous version.

**Rollback triggers:**
- Application errors or crashes
- Performance degradation
- Security issue introduced
- Failed verification testing

**Rollback methods:**
- Revert Git commit and redeploy
- Roll back to previous Docker image
- Toggle feature flag off
- Restore from backup (database)

**Owner:** Engineer, Infrastructure Team
**Duration:** 5-15 minutes

## Emergency Changes

For critical security patches or production outages, expedited process allowed:

1. Create PR with "EMERGENCY" label
2. Post to #engineering Slack channel
3. Minimal review (1 approval, can be post-deployment)
4. Deploy immediately
5. Retrospective within 24 hours to review process

## Change Categories

**Standard changes:** Low-risk, pre-approved patterns (dependency updates, bug fixes)
- 1 reviewer approval
- Automated deployment

**Normal changes:** Most code and infrastructure changes
- 1-2 reviewer approvals
- Security review if needed
- Standard deployment process

**High-risk changes:** Database schema changes, major architecture changes
- 2 reviewer approvals + tech lead
- Security review required
- Manual deployment
- Extra monitoring

## Validation and Evidence

- Git commit history with review approvals
- CI/CD pipeline logs
- Deployment logs
- Post-deployment verification notes
- Rollback events (if any)

## References

- Related controls: OPS-01
- Related standards: github-security-standard.md, aws-security-standard.md

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [OPS-01: Change Management](../custom/ops-01.md) ^[8-step process: proposal, automated testing, peer review, security review, staging deployment, production deployment, verification, rollback]

---

<!-- Backlinks auto-generated below -->
