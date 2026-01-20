---
type: policy
title: Baseline Security Policy
owner: security-team
last_reviewed: 2025-01-09
review_cadence: annual
applies_to: all-employees
---

# Baseline Security Policy

Baseline security requirements that apply to all employees, contractors, and vendors with access to company systems.

## Purpose

This policy establishes minimum security practices for all personnel to protect company and customer data, maintain system availability, and comply with regulatory requirements.

## Scope

Applies to all employees, contractors, temporary staff, and third parties with access to company systems, data, or facilities.

## Account Security

### Requirements

- Use unique, strong passwords for all accounts (12+ characters, mix of character types)
- Enable Multi-Factor Authentication (MFA) on all company accounts
- Never share passwords or MFA devices with others
- Do not reuse company passwords for personal accounts
- Store passwords in approved password manager only (no spreadsheets, notes, browser storage)

### Responsibilities

- Protect your credentials as if they were your house keys
- Report lost or compromised credentials to IT/Security immediately
- Change passwords immediately if compromise suspected
- Use company-provided password manager (1Password, LastPass, etc.)

## Data Handling

### Requirements

- Classify data appropriately (see data-classification-standard.md)
- **Confidential data:** Do not store on local laptop, use cloud storage only
- **Restricted data:** Access only when required for job duties, never copy to personal devices
- Do not share customer data externally without authorization
- Do not send Confidential/Restricted data via email or Slack without encryption
- Report data breaches or suspected unauthorized access immediately

### Responsibilities

- Understand data classification levels and handle data accordingly
- Minimize data collection and storage (only collect what you need)
- Delete data when no longer needed (follow retention policies)
- Encrypt sensitive data when storing or transmitting

## Device Security

### Requirements

- Use company-issued device or approved BYOD device enrolled in MDM
- Enable FileVault disk encryption on macOS devices
- Keep operating system and software up to date (install security patches within 7 days)
- Enable screen lock after 5 minutes of inactivity
- Do not jailbreak or root devices
- Install company-required security software (EDR agent, antivirus)
- Report lost or stolen devices immediately

### Responsibilities

- Protect physical access to your device (don't leave unlocked in public)
- Use only approved software (request approval for new tools)
- Lock your screen when leaving your device unattended
- Back up important work to cloud storage (not just local disk)

## Network and Remote Work

### Requirements

- Use company VPN when accessing internal resources from untrusted networks
- Do not access production systems from public WiFi without VPN
- Avoid using public computers for company work
- Use secure WiFi networks when working remotely (WPA2/WPA3 encryption)

### Responsibilities

- Be cautious on public WiFi (assume it's monitored)
- Do not plug unknown USB devices into company laptop
- Use video call backgrounds to avoid exposing sensitive information on screen

## Email and Communication

### Requirements

- Be vigilant for phishing emails (unexpected links, urgent requests, suspicious senders)
- Verify requests for sensitive information or money transfers through secondary channel (call, Slack)
- Do not click links or open attachments from unknown senders
- Report suspected phishing to security team (forward to security@company.com)
- Use company-approved communication tools only (Slack, email, Zoom)

### Responsibilities

- Think before you click (hover over links to verify destination)
- Be suspicious of urgent or unusual requests (CEO fraud, invoice scams)
- Forward phishing attempts to security team for analysis and blocking

## Access to Systems

### Requirements

- Access only systems and data required for your job duties
- Do not share your account credentials or use shared accounts (except approved service accounts)
- Log out or lock sessions when done
- Do not attempt to access systems or data you're not authorized for
- Request access through proper channels (IT ticket)

### Responsibilities

- Respect least privilege principle (don't request more access than you need)
- Notify manager if your role changes and you no longer need certain access
- Report suspicious account activity (unexpected password reset, unrecognized login location)

## Security Incidents

### Requirements

- Report security incidents immediately (don't wait)
- Do not attempt to "fix" a security incident yourself (may destroy evidence)
- Preserve evidence (don't delete logs, emails, or files)
- Follow incident response team instructions

**What to report:**
- Suspected phishing or malware
- Lost or stolen devices or credentials
- Unauthorized access to systems or data
- Suspicious system behavior
- Accidental data exposure (sent to wrong recipient, public S3 bucket)

### Responsibilities

- When in doubt, report it (better safe than sorry)
- Do not discuss incidents publicly (including social media)
- Contact security team: security@company.com or Slack #security-incidents

## Acceptable Use

### Requirements

- Use company systems and data for business purposes only (limited personal use acceptable)
- Do not use company resources for illegal, unethical, or offensive activities
- Do not download or distribute pirated software
- Do not access inappropriate content (adult content, illegal material)
- Respect intellectual property (company and third-party)

### Responsibilities

- Be professional in all communications (email, Slack, GitHub)
- Do not harass, threaten, or discriminate against others online
- Represent the company positively on social media and professional networks

## Third-Party Services

### Requirements

- Use only company-approved SaaS tools and services
- Do not sign up for new SaaS tools without IT/Security approval
- Do not upload Confidential/Restricted data to unapproved services
- Follow vendor security requirements (MFA, access controls)

### Responsibilities

- Request approval before adopting new tools (use IT request process)
- Consider security and privacy when evaluating tools
- Do not use personal accounts for company work (e.g., personal Dropbox)

## Training and Awareness

### Requirements

- Complete security awareness training during onboarding (within 7 days)
- Complete annual security refresher training
- Acknowledge security policies annually
- Participate in security programs (phishing simulations, security events)

### Responsibilities

- Stay informed about security threats and best practices
- Apply training to real-world scenarios
- Ask questions if unsure about security requirements

## Consequences of Non-Compliance

Violations of this policy may result in:
- Verbal or written warning
- Additional training
- Revocation of access privileges
- Termination of employment or contract
- Legal action (if criminal activity)

Severity of consequences depends on intent (accidental vs. malicious), impact, and history of violations.

## Exceptions

Requests for exceptions to this policy must be submitted in writing to security team with business justification. Exceptions require approval from Security Team Lead or CISO. Approved exceptions documented and reviewed annually.

## Acknowledgment

All employees must acknowledge this policy during onboarding and annually. Acknowledgment tracked in HR system.

## Related Documents

- Standards: data-classification-standard.md, saas-iam-standard.md, endpoint-security-standard.md
- Processes: security-training-process.md, incident-response-process.md
- Role-specific policies: engineering-security-policy.md, data-access-policy.md

## References

- SANS Security Policy Templates: https://www.sans.org/information-security-policy/
- NIST SP 800-100: Information Security Handbook

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Identity & Authentication](../controls/iam/identity-authentication.md) ^[Requires MFA on all company accounts, strong passwords (12+ characters), password manager usage]
- [Password Management](../controls/iam/password-management.md) ^[Unique strong passwords, never share credentials, company-provided password manager required]
- [Multi-Factor Authentication](../controls/iam/multi-factor-authentication.md) ^[MFA enabled on all company accounts, protect MFA devices, never share]
- [Data Classification](../controls/data-management/data-classification.md) ^[Understand and follow data classification: Public, Internal, Confidential, Restricted with appropriate handling]
- [Encryption at Rest](../controls/cryptography/encryption-at-rest.md) ^[Confidential data not on local laptop, use encrypted cloud storage only]
- [Encryption in Transit](../controls/cryptography/encryption-in-transit.md) ^[Do not send Confidential/Restricted data via email or Slack without encryption]
- [Device Management (macOS MDM)](../controls/endpoint-security/device-management-macos-mdm.md) ^[Use company-issued device or approved BYOD enrolled in MDM, report lost/stolen devices immediately]
- [Endpoint Protection](../controls/endpoint-security/endpoint-protection.md) ^[Install company-required EDR agent, do not jailbreak devices, firewall enabled]
- [Software Updates](../controls/endpoint-security/software-updates.md) ^[Keep OS and software up to date, install security patches within 7 days]
- [Endpoint Network Security](../controls/network-security/endpoint-network-security.md) ^[Use VPN for internal resources on untrusted networks, no production access from public WiFi without VPN]
- [Security Awareness Training](../controls/security-training/security-awareness-training.md) ^[Complete security awareness training within 7 days of onboarding, annual refresher, policy acknowledgment]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Report security incidents immediately, preserve evidence, follow IR team instructions]
- [Security Policies](../controls/governance/security-policies.md) ^[Establishes baseline security practices for all personnel, annual acknowledgment required]
- [Least Privilege & RBAC](../controls/iam/least-privilege-rbac.md) ^[Access only systems and data required for job duties, request access through proper channels]
- [Rules of Behavior](../controls/personnel-security/rules-of-behavior.md) ^[Establishes acceptable use policy covering account security, data handling, device security, network security, email security, physical security with annual acknowledgment]

---

<!-- Backlinks auto-generated below -->
