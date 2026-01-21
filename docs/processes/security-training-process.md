---
type: process
title: Security Training Process
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [security-team, hr, all-employees]
---

# Security Training Process

Process for delivering and tracking security awareness training for all employees.

## Roles and Responsibilities

- **Security Team:** Develops training content, tracks completion
- **HR:** Enforces training requirements during onboarding
- **Managers:** Ensure team members complete training
- **Employees:** Complete required training

## Prerequisites

- Security training platform (e.g., KnowBe4, SANS, custom LMS)
- Training content library
- Tracking system for completion

## Process Steps

### Step 1: New Hire Training

All new employees complete security training during onboarding (within first 7 days).

**Training modules:**
- Security policies overview
- Password and authentication best practices (MFA)
- Phishing and social engineering awareness
- Data classification and handling
- Acceptable use of company resources
- Incident reporting
- Physical security (if applicable)

**Delivery:** Self-paced online training with quiz (80% passing score)

**Owner:** New Employee (completion), HR (tracking)
**Duration:** 45-60 minutes, complete within first week

### Step 2: Annual Refresher Training

All employees complete refresher training annually.

**Training modules (updated yearly):**
- Review of security policies (any changes)
- Latest threat landscape (recent attacks, trends)
- Phishing awareness (updated scenarios)
- Data privacy and GDPR/CCPA requirements
- Secure remote work practices
- New security tools or processes

**Delivery:** Online training with quiz, scheduled in Q1 each year

**Owner:** All Employees
**Duration:** 30 minutes annually

### Step 3: Role-Specific Training

Employees in certain roles receive additional specialized training.

**Engineering team:**
- Secure coding practices (OWASP Top 10)
- Secrets management
- Secure SDLC
- Frequency: Annually, plus on-demand resources

**Infrastructure team:**
- Cloud security best practices (AWS, GCP, Azure)
- Infrastructure as code security
- Frequency: Annually

**Managers:**
- Access review procedures
- Handling security incidents with team members
- Frequency: Annually

**Customer success / Support:**
- Handling customer data securely
- Recognizing social engineering targeting customer accounts
- Frequency: Annually

**Owner:** Respective team members
**Duration:** 1-2 hours annually

### Step 4: Phishing Simulations

Security team conducts simulated phishing campaigns quarterly.

**Campaign details:**
- Realistic phishing emails sent to random selection of employees
- Track click rate and credential entry rate
- Immediate education for employees who click (micro-training)

**Scenarios:**
- Fake password reset emails
- Fake invoice/payment requests
- Fake IT support requests
- Impersonation of executives (CEO fraud)

**Frequency:** Quarterly (4 campaigns per year)

**Owner:** Security Team
**Duration:** Ongoing, quarterly campaigns

### Step 5: Tracking and Reporting

Security team tracks training completion and reports to leadership.

**Metrics tracked:**
- New hire training completion rate (target: 100% within 7 days)
- Annual training completion rate (target: 100% by deadline)
- Phishing simulation click rate (target: <5%)
- Repeat clickers (individuals who fail multiple simulations)

**Reporting:**
- Monthly: Completion dashboard
- Quarterly: Training metrics to leadership
- Annually: Comprehensive training report

**Owner:** Security Team
**Duration:** Ongoing

### Step 6: Remedial Training

Employees who fail phishing simulations or violate security policies receive additional training.

**Triggers for remedial training:**
- Click on 2+ phishing simulations in a year
- Enter credentials on phishing simulation
- Security policy violation
- Involvement in security incident due to user error

**Remedial training:**
- One-on-one session with security team member (30 min)
- Targeted training on specific weakness (phishing, data handling, etc.)
- Manager notified of pattern (if repeated failures)

**Owner:** Security Team
**Duration:** As needed

### Step 7: Content Updates

Security team updates training content annually or as needed.

**Update triggers:**
- New security policies or tools
- Significant security incidents (internal or industry-wide)
- Regulatory changes (GDPR, CCPA, etc.)
- Feedback from employees on training clarity

**Process:**
- Review training content in Q4
- Update modules with new content
- Record updated versions
- Deploy updated training in Q1

**Owner:** Security Team
**Duration:** Annual review in Q4

## Validation and Evidence

- Training platform completion reports (new hire, annual, role-specific)
- Training acknowledgment records (signed policies)
- Phishing simulation results
- Remedial training records
- Annual training summary report

## Enforcement

- New hire training: Required before system access granted (IT access blocked until complete)
- Annual training: Email reminders at 2 weeks, 1 week, 3 days before deadline
- Non-compliance escalation: Manager reminder → VP reminder → HR intervention

## References

- Related controls: PEO-02, GOV-01
- Related policies: 
- SANS Security Awareness Training: https://www.sans.org/security-awareness-training/

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [PEO-02: Security Training](../custom/peo-02.md) ^[7-step training program: new hire, annual refresher, role-specific, phishing simulations, tracking, remedial, content updates]
- [GOV-01: Security Policies](../custom/gov-01.md) ^[Training includes security policies overview, acceptable use, data classification, incident reporting]
- [Security Training](../controls/personnel-security/security-training.md) ^[7-step training program: new hire (within 7 days), annual refresher (Q1), role-specific (engineers, infrastructure, managers), quarterly phishing simulations, completion tracking, remedial training for failures, annual content updates]

---

<!-- Backlinks auto-generated below -->
