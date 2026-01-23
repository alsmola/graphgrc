---
type: process
title: Access Provisioning Process
owner: it-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [it-team, hiring-manager, hr]
---

# Access Provisioning Process

Step-by-step process for granting user access to company systems and applications.

## Roles and Responsibilities

- **HR:** Initiates provisioning request when employee starts or changes roles
- **Hiring Manager:** Specifies required access based on role
- **IT Team:** Provisions accounts and access
- **Security Team:** Reviews and approves privileged access requests

## Prerequisites

- Employee record created in HRIS
- Role and department defined
- Manager assigned

## Process Steps

### Step 1: Request Initiation

HR creates provisioning ticket in IT system on employee start date or role change.

**Ticket includes:**
- Employee name, email, department, role
- Start date or role change effective date
- Manager name
- Standard access template for role (if exists)

**Owner:** HR
**Duration:** Day before start date

### Step 2: Access Determination

Manager reviews standard access template and adds/removes systems based on specific needs.

**Standard access typically includes:**
- Email (Google Workspace)
- Slack
- GitHub (for engineers)
- AWS SSO (for engineers/infrastructure team)
- Specific SaaS tools for role

**Owner:** Hiring Manager
**Duration:** < 4 hours

### Step 3: Account Creation

IT team provisions accounts via automated tools (SCIM) or manual creation.

**Actions:**
- Create SSO account in identity provider (Okta, Google Workspace)
- Assign to appropriate groups for RBAC
- Provision SaaS application access via SCIM or API
- Send welcome email with setup instructions

**Owner:** IT Team
**Duration:** < 2 hours

### Step 4: Elevated Access (if needed)

For admin/privileged access, security team reviews request.

**Review criteria:**
- Business justification
- Least privilege principle
- Temporary vs permanent access
- Alternatives to elevated access

**Approval required from:** Security team lead
**Owner:** Security Team
**Duration:** < 24 hours

### Step 5: Verification

IT team verifies provisioning completed successfully.

**Checks:**
- User can log in via SSO
- MFA enrollment completed
- Access to required systems confirmed
- No errors in provisioning logs

**Owner:** IT Team
**Duration:** < 1 hour

### Step 6: User Onboarding

New employee completes account setup on first day.

**Tasks:**
- Enroll MFA (authenticator app)
- Accept security policy acknowledgment
- Complete security awareness training (within 7 days)

**Owner:** New Employee
**Duration:** Day 1

## Validation and Evidence

- Provisioning ticket with timestamps and approvals
- Audit logs from identity provider showing account creation
- MFA enrollment confirmation
- Security training completion record

## Exception Handling

- **Urgent access (same-day hire):** Manager can request expedited provisioning, security review happens retroactively
- **Contractor/vendor access:** Follow vendor access process (separate procedure)

## References

- Related controls: ACC-01, ACC-02, PEO-01
- Related standards: saas-iam-standard.md
- Related process: access-deprovisioning-process.md (offboarding)

---

<!-- Backlinks auto-generated below -->
