---
type: process
title: Vendor Risk Assessment Process
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
participants: [security-team, procurement, legal, department-requesting-vendor]
---

# Vendor Risk Assessment Process

Process for assessing security and privacy risks of third-party vendors and SaaS applications.

## Roles and Responsibilities

- **Requesting Department:** Identifies need for vendor, provides business context
- **Security Team:** Conducts risk assessment, approves or rejects vendor
- **Legal:** Reviews contracts, negotiates DPA/security terms
- **Procurement:** Manages purchasing and vendor relationship

## Prerequisites

- Vendor inventory system (track all vendors)
- Security assessment questionnaire template
- Approved vendor list (low-risk pre-approved vendors)

## Process Steps

### Step 1: Vendor Request Initiated

Department submits request to onboard new vendor or SaaS tool.

**Request includes:**
- Vendor name and description
- Business justification and use case
- Data types to be shared (Public, Internal, Confidential, Restricted)
- Number of users
- Budget/cost
- Alternatives considered

**Owner:** Requesting Department
**Duration:** 1 day

### Step 2: Initial Risk Screening

Security team determines assessment level based on data sensitivity.

**Risk tiers:**
- **Low risk:** No Confidential/Restricted data, minimal integration (e.g., marketing tools, public communication) → Expedited approval
- **Medium risk:** Confidential data (customer PII, business data) → Standard assessment
- **High risk:** Restricted data (payment, health, credentials) or critical system → Comprehensive assessment

**Owner:** Security Team
**Duration:** 1-2 business days

### Step 3: Security Questionnaire (Medium/High risk)

Security team sends questionnaire to vendor or reviews vendor's published security documentation.

**Assessment areas:**
- Certifications (SOC 2, ISO 27001, GDPR compliance)
- Data location and residency
- Encryption (at rest and in transit)
- Access controls and authentication (SSO, MFA)
- Data retention and deletion practices
- Incident response and breach notification
- Subprocessors and data sharing
- Business continuity and availability SLA

**Sources:**
- Vendor security questionnaire response
- SOC 2 Type II report
- Vendor Trust Center / security documentation
- Online research (breach history, reputation)

**Owner:** Security Team
**Duration:** 1-2 weeks (waiting on vendor response)

### Step 4: Risk Analysis

Security team evaluates vendor responses and assigns risk rating.

**Risk factors:**
- Data sensitivity
- Security posture (certifications, controls)
- Vendor maturity and reputation
- Contractual protections
- Alternatives available

**Risk rating:** Low, Medium, High, Critical

**Actions:**
- Low/Medium: Proceed to contracting
- High: Require additional controls or contract terms
- Critical: Recommend alternative vendor or compensating controls

**Owner:** Security Team
**Duration:** 2-3 business days

### Step 5: Legal Review and Contracting

Legal reviews contract and negotiates security/privacy terms.

**Required contract terms (Medium/High risk):**
- Data Processing Agreement (DPA) for GDPR compliance
- Security requirements (encryption, access controls)
- Audit rights (right to review SOC 2 report)
- Breach notification (within 24-48 hours)
- Data deletion upon termination
- Subprocessor disclosure and approval
- Indemnification and liability

**Owner:** Legal, Procurement
**Duration:** 1-4 weeks (negotiation timeline)

### Step 6: Technical Integration Review

For integrations accessing company systems, engineering/security teams review technical implementation.

**Review areas:**
- API authentication (OAuth, API keys with rotation)
- Least privilege access (read-only vs. write)
- Data minimization (only share necessary data)
- Logging and monitoring of vendor access

**Owner:** Security Team, Engineering Team
**Duration:** 3-5 business days

### Step 7: Approval and Onboarding

Security team provides final approval, vendor added to approved vendor list.

**Onboarding actions:**
- Add to vendor inventory
- Document risk rating and any exceptions/compensating controls
- Set annual review date
- Share vendor security requirements with vendor contact

**Owner:** Security Team, Procurement
**Duration:** 1 business day

### Step 8: Ongoing Monitoring

Vendors reviewed annually or upon changes.

**Re-assessment triggers:**
- Annual review date
- Vendor security incident/breach
- Change in data shared (new data types or increased volume)
- Contract renewal
- Vendor acquisition or major organizational change

**Owner:** Security Team
**Duration:** Quarterly monitoring, annual deep dive

## Expedited Approval (Low Risk)

Pre-approved vendor categories that skip full assessment:
- No data sharing (informational tools)
- Public data only (marketing, social media)
- Well-known low-risk vendors (e.g., Zoom for video calls)

Approved by security team lead without full questionnaire.

## Validation and Evidence

- Vendor risk assessment with questionnaire responses
- SOC 2 reports (stored securely)
- Contract with security/DPA terms
- Approval decision documented
- Vendor inventory with risk ratings
- Annual review records

## References

- Related controls: VEN-01, VEN-02, DAT-04
- SaaS Security Checklist: https://www.sqreen.com/checklists/saas-cto-security-checklist

## Control Mapping

- [Third-Party Risk Assessment](../controls/vendor-management/third-party-risk-assessment.md) ^[8-step vendor assessment process: request initiation, risk screening, security questionnaire with SOC 2/ISO review, risk analysis, legal review with DPA negotiation, technical integration review, approval and onboarding, annual ongoing monitoring]
- [Vendor Contracts & DPAs](../controls/vendor-management/vendor-contracts-dpas.md) ^[Legal review in Step 5 negotiates DPAs, security terms, breach notification SLAs, data deletion clauses, audit rights; contract repository tracks all executed agreements with renewal dates]
