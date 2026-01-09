# OPS-02: Vulnerability Management
  
**Category: **Operational Security
  
## Objective
Identify and remediate security vulnerabilities before exploitation.
  
## Description
Systems are regularly scanned for vulnerabilities. Critical vulnerabilities are patched within 30 days. Penetration testing is conducted annually. Vulnerability management process is documented.
  
## Implementation Guidance
**Vulnerability Scanning**: AWS Inspector scans EC2 instances and containers for vulnerabilities. Dependency scanning in GitHub for application code.
  
**Patching SLA**: Critical vulnerabilities patched within 7 days. High within 30 days. Medium within 90 days.
  
**Penetration Testing**: Annual external penetration test by qualified third party. Findings remediated based on severity.
  
**Bug Bounty**: Public bug bounty program for security researchers. Valid findings remediated and researcher rewarded.
  
  
## Examples of Good Implementation
- AWS Inspector scans all production EC2 instances weekly
- Dependabot creates PRs for vulnerable npm packages, merged within 5 days
- 2024 annual penetration test found 2 medium findings, both remediated within 30 days
- Bug bounty program paid out 3 researchers in 2024 for valid security findings
  
## Audit Evidence
- Vulnerability scan results
- Vulnerability remediation timeline
- Annual penetration test report
- Bug bounty program results
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC7.1](../soc2/cc71.md)
  