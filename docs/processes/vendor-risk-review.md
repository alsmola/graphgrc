---
type: process
title: Vendor Risk Review
owner: security-team
last_reviewed: 2025-01-14
review_cadence: annual
---

# Vendor Risk Review

Security and privacy assessment of third-party vendors before contract signature and annually thereafter. Validates vendor controls match organizational risk tolerance. Implements third-party risk management per [Risk Management Charter](../charter/risk-management.md#risk-identification).

## Scope

**Requires vendor risk review**:

- **Data processors**: Vendors receiving, storing, or processing customer or employee data (SaaS, cloud providers, analytics, support tools)
- **Infrastructure providers**: Hosting, CDN, DNS, security tools with production access
- **Critical business services**: Payment processors, email providers, identity providers, backup services
- **Integration partners**: API integrations with bidirectional data flow

**Simplified review** (questionnaire only, no deep assessment):

- **Low-risk vendors**: No data access, no production infrastructure (swag, office supplies, general business tools with no sensitive data)
- **Consumer tools**: Individual employee subscriptions with no company data sharing

**Out of scope** (no formal review):

- One-time purchases with no ongoing relationship
- Publicly available services with no account or data (website hosting of public marketing content)

**Risk-based review depth**:

- **High risk** (customer PII, production access, SOC 2 critical vendors): Full questionnaire + certifications + DPA + remediation plan
- **Medium risk** (employee data, non-production systems): Questionnaire + certifications
- **Low risk** (no sensitive data, isolated systems): Brief questionnaire only

## Roles

**Procurement/Requester** (Department Lead): Identifies vendor need, initiates review request, provides business justification, owns vendor relationship, negotiates contract with Legal.

**Security Team**: Conducts risk assessment, reviews vendor security posture, requests remediation for gaps, approves or rejects from security perspective, tracks vendor inventory and annual re-reviews.

**Legal**: Reviews contract terms, negotiates DPA (Data Processing Agreement), ensures liability and breach notification clauses, validates compliance with regulations.

**Privacy/Compliance** (if applicable): Reviews data processing activities for GDPR compliance, validates DPA terms, assesses data transfer mechanisms (SCCs, adequacy decisions).

**Finance**: Approves budget, executes contract signature after security/legal approval.

## Steps

### 1. Vendor Identification & Initial Triage

**Requester submits** vendor review request with:

- Vendor name, website, product/service description
- Business justification (why do we need this?)
- Data types vendor will access/process (customer PII, employee data, business data, none)
- Integration scope (API, SSO, file sharing, manual data transfer)
- Production vs non-production system
- Contract value and term

**Security Team triages** within 2 business days:

- **No review needed**: No data access, non-critical, consumer tool → Approve immediately
- **Simplified review**: Low risk per scope above → 5-day questionnaire review
- **Standard review**: Medium/high risk → 10-day full assessment
- **Escalated review**: Critical vendor (SOC 2 dependency, large customer data processor) → 15-day detailed review + Legal/Privacy involvement

**Security Team sends** vendor security questionnaire appropriate to risk level.

### 2. Vendor Assessment

**Security Team reviews** vendor-provided information:

**Security questionnaire responses**:

- Data handling practices (encryption, retention, deletion, access controls)
- Infrastructure security (cloud provider, network security, monitoring, patching)
- Authentication/authorization (MFA, SSO support, password policies, session management)
- Incident response capabilities (detection, notification SLAs, contact procedures)
- Business continuity (backup, disaster recovery, uptime SLAs)
- Compliance (certifications, audits, privacy frameworks)

**Supporting documentation** (request as applicable):

- **SOC 2 Type II report** (preferred for high-risk vendors): Review report date (must be <12 months old), scope (matches our use case?), exceptions/qualifications
- **ISO 27001 certificate**: Validates ISMS in place
- **Penetration test results**: Recent (within 12 months), conducted by reputable firm, critical findings remediated
- **DPA template**: Data Processing Agreement for GDPR compliance (required for EU data processing)

**Security Team assesses risk**:

- Score using [Risk Scoring Methodology](organizational-risk-assessment.md#risk-scoring-methodology)
- Identify gaps vs organizational security requirements
- Determine if gaps are acceptable, require remediation, or are deal-breakers

### 3. Risk Treatment & Remediation

**For identified gaps**, Security Team determines treatment:

**Accept risk** (document and move forward):

- Gap is low severity
- Compensating controls exist (e.g., vendor lacks encryption, but we encrypt before sending)
- Business criticality outweighs risk (document in risk register with approval)

**Request remediation** (vendor must address before approval):

- Critical gaps (no encryption at rest for customer PII, no MFA for admin access, no incident response plan)
- Security Team provides vendor with remediation requirements and timeline
- Vendor responds with remediation plan or timeline for fixes
- Security Team validates remediation completed

**Reject vendor** (cannot accept risk):

- Vendor risk exceeds organizational appetite per [Risk Management Charter](../charter/risk-management.md#risk-appetite)
- Vendor unwilling to remediate critical gaps
- Better alternative vendors available
- Security Team notifies requester, provides rationale, suggests alternatives if possible

**Add contractual controls** (Legal negotiates):

- Mandatory breach notification timeline (e.g., within 24 hours)
- Right to audit vendor security controls
- Data deletion upon termination
- Liability caps and insurance requirements
- Subprocessor notification and approval rights

### 4. Approval & Contracting

**Security Team approves** vendor from security perspective (or conditional approval pending remediation/contract terms).

**Legal reviews** contract:

- Negotiates DPA for data processors
- Ensures security obligations in MSA (Master Service Agreement)
- Validates breach notification, liability, indemnification clauses

**Finance executes** contract after all approvals obtained.

**Security Team documents** in vendor inventory:

- Vendor name, contact, contract dates, renewal date
- Risk assessment score and date
- Data types processed
- Certifications on file (SOC 2, ISO, pen test)
- Next review date (annually or at renewal)
- Remediation plans and status

### 5. Ongoing Monitoring & Annual Review

**Continuous monitoring**:

- Track vendor security incidents (vendor-reported or public breaches)
- Monitor news for vendor breaches or security issues
- Review vendor security notifications and changelog for material changes

**Annual re-assessment** (or at contract renewal):

- Request updated questionnaire and certifications
- Review any incidents from past year
- Re-score risk using current methodology
- Identify new gaps since last review
- Determine if vendor still meets requirements

**Triggered re-assessment** (immediate):

- Vendor reports security incident or breach
- Vendor changes ownership, infrastructure, or subprocessors
- Material change to our usage (now processing more sensitive data)
- Failed audit findings related to vendor controls

**Offboarding** (contract termination):

- Request data deletion confirmation
- Revoke vendor access (API keys, SSO, file shares)
- Archive vendor assessment for audit trail
- Remove from active vendor inventory (retain in historical records)

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Vendor Risk Management](../controls/risk-management/vendor-risk-management.md) ^[Vendor risk assessment process: questionnaire, evidence review, risk scoring, DPA negotiation, approval, ongoing monitoring]
- [Contract Management](../controls/compliance/contract-management.md) ^[Vendor contracts reviewed for security terms, SLAs, data processing agreements, liability provisions]
- [Customer Personal Data](../controls/data-privacy/customer-personal-data.md) ^[Data Processing Agreements (DPAs) required for vendors processing customer PII per GDPR]
- [Organizational Risk Assessment](../controls/risk-management/organizational-risk-assessment.md) ^[High-risk vendors escalated to organizational risk register]
- [External Audits](../controls/compliance/external-audits.md) ^[Vendor SOC 2/ISO 27001 reports reviewed as part of vendor assessment]
- [SaaS Inventory](../controls/asset-management/saas-inventory.md) ^[Approved vendors added to SaaS inventory for tracking]
- [Third-Party Risk Assessment](../controls/vendor-management/third-party-risk-assessment.md) ^[5-step vendor risk review: identification and triage, security questionnaire and evidence review, risk treatment and remediation, contract approval with security terms, annual re-assessment and ongoing monitoring]
- [Vendor Contracts & DPAs](../controls/vendor-management/vendor-contracts-dpas.md) ^[Legal reviews contracts for security requirements, SLA, audit rights, termination clauses; DPA template executed with vendors processing customer data; contracts stored in central repository with expiration tracking]
