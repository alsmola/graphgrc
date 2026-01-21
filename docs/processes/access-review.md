---
type: process
title: Access Review
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Access Review

Quarterly review of user access across all systems to validate least privilege principle. Ensures employees have only necessary access, detects orphaned accounts, identifies privilege creep. Implements [Governance](../charter/governance.md#metrics) access control metrics and least privilege principle.

## Scope

**Systems reviewed quarterly**:

- **Cloud infrastructure**: AWS, GCP, Azure IAM roles and permissions (see [Cloud IAM](../controls/iam/cloud-iam.md))
- **SaaS applications**: Google Workspace, GitHub, Jira, Slack, CRM, marketing tools, support systems (see [SaaS IAM](../controls/iam/saas-iam.md))
- **Production databases**: Direct database access, read replicas, query tools
- **Admin consoles**: MDM, SSO, EDR, SIEM, security tools
- **VPN/network access**: If applicable

**Access types reviewed**:

- User accounts (employees, contractors)
- Service accounts and API keys
- Shared accounts (flag for remediation)
- Admin/privileged roles
- Cross-account/cross-tenant access

**Out of scope**: Customer accounts, public-facing services. Those reviewed separately as part of customer access management.

## Roles

**Security Team**: Coordinates review, generates access reports, tracks completion, escalates exceptions, updates access baselines, reports metrics to [Security Committee](../charter/governance.md#communication).

**IT Operations**: Reviews endpoint access, VPN, MDM, SSO configurations. Approves/revokes access per manager decisions.

**Department Managers**: Review and approve access for direct reports. Indicate required access level (read, write, admin). Respond within 5 business days.

**System Owners** (Engineering Leads, Department Heads): Review service accounts, admin access, cross-functional access. Validate business justification for privileged access.

**HR**: Provides employee status (active, contractor, terminated, transferred). Flags recent role changes requiring access adjustment.

## Steps

### 1. Preparation (Week 1)

**Security Team generates access reports** for all in-scope systems:

- Export user lists with roles, permissions, last login, account creation date
- Cross-reference with HR system for current employees
- Flag anomalies: inactive accounts (no login >90 days), terminated employees still with access, unexpected admin accounts
- Group users by department and manager for delegation

**Tools**: SSO admin console, cloud IAM exports, SaaS admin APIs, HR system export

**Output**: Access review workbook with one sheet per system/department, flagged anomalies

### 2. Manager Review (Weeks 2-3)

**Security Team distributes** access review workbook to department managers with instructions:

- Review each direct report's access
- For each account: Approve (current role requires this), Revoke (no longer needed), Modify (change permission level)
- Provide business justification for admin/privileged access
- Complete review within 5 business days

**Managers review** and annotate spreadsheet or review tool:

- ✅ **Approve**: Access appropriate for current role
- ❌ **Revoke**: No longer needed (role change, project ended, over-provisioned)
- ⚠️ **Modify**: Downgrade admin to standard, reduce scope, change from write to read-only

**For ambiguous cases**: Managers contact employee directly to confirm usage. If unused or uncertain, default to revoke (employee can request reinstatement if needed).

**Security Team monitors** completion rate, sends reminders at day 3 and day 5. Escalates incomplete reviews to Department Heads.

### 3. System Owner Review (Week 3)

**System Owners** (Engineering Leads for infrastructure, Department Heads for SaaS) review:

- **Service accounts**: Still in use? Principle of least privilege? Credentials rotated recently per [Secrets Management](../controls/iam/secrets-management.md)?
- **Admin accounts**: Business justification documented? Time-bound or standing access? Can this be JIT access instead?
- **Cross-functional access**: Engineering access to CRM, Sales access to production logs, etc. Still required?

**Output**: Approved service accounts with documented justification, admin access with review date, flagged accounts for revocation

### 4. Remediation (Week 4)

**IT Operations and Security Team** execute access changes:

**Revocations**:

- Remove user from groups, roles, organizations
- Disable accounts (don't delete immediately - retain for audit trail)
- Document reason for removal in access log

**Modifications**:

- Downgrade admin to standard user
- Reduce scope of access (e.g., from all projects to specific project)
- Change from write to read-only

**Exceptions** (approved admin access, cross-functional access):

- Document business justification in exception register
- Set review date (3-6 months for high-privilege access)
- Ensure compensating controls (MFA, monitoring, logging)

**Orphaned accounts** (terminated employees, unknown users):

- Immediately disable
- Investigate recent activity via audit logs
- If suspicious activity, escalate to [Security Incident Response](security-incident-response.md)
- Delete after 30-day retention for recovery

**Output**: All access changes executed and documented

### 5. Validation & Reporting (Week 4-5)

**Security Team validates** remediation completed:

- Spot-check removed users no longer appear in system exports
- Verify admin count decreased or justifications documented
- Check service account inventory updated

**Security Team reports** to [Security Committee](../charter/governance.md#communication):

- Total accounts reviewed across all systems
- Revocations by system (number and percentage)
- Orphaned/terminated accounts found and removed
- Admin account count trend (should be stable or decreasing)
- Completion rate by department (target 100%)
- Exception count and types

**Metrics tracked** per [Governance Metrics](../charter/governance.md#metrics):

- Access review completion: 100% quarterly
- Orphaned account removal time: <5 days from identification
- Admin account percentage: Trend down or stable with documented justification

### 6. Baseline Update

**Security Team updates** access baselines for next quarter:

- Current approved access becomes new baseline
- Document new service accounts with owners
- Update exception register with new review dates
- Archive review workbook for audit evidence

**Continuous improvements**:

- Identify systems with highest revocation rates (indicates over-provisioning)
- Work with IT to improve onboarding/offboarding automation
- Recommend JIT access for high-privilege roles
- Integrate SSO to centralize access management (see [Single Sign-On](../controls/iam/single-sign-on.md))

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Cloud IAM](../controls/iam/cloud-iam.md) ^[Quarterly review of AWS IAM roles and policies, validation of cloud infrastructure access, removal of over-provisioned permissions]
- [SaaS IAM](../controls/iam/saas-iam.md) ^[Quarterly reviews of SaaS application access across Google Workspace, GitHub, Jira, Slack, identification and removal of orphaned accounts]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Review of admin/privileged roles, service accounts, validation of business justification for elevated access]
- [Single Sign-On](../controls/iam/single-sign-on.md) ^[SSO integration centralizes access management and simplifies quarterly reviews across all connected applications]
- [Offboarding](../controls/personnel-security/offboarding.md) ^[Cross-reference quarterly access reports with HR system to identify and remove access for terminated employees]
- [Documentation Review](../controls/compliance/documentation-review.md) ^[Access review workbooks archived as audit evidence, access baselines documented and updated quarterly]
