# INF-02: Network Security
**Category: **Infrastructure Security
  
## Objective
Protect network perimeter and internal network traffic.
  
## Description
Network boundaries are protected with firewalls and network segmentation. Remote access requires VPN or zero-trust architecture. Network traffic is monitored.
  
## Implementation Guidance
**Cloud Firewalls**: AWS Security Groups and NACLs protect resources. AWS Network Firewall for advanced threat protection.
  
**Zero Trust**: Applications behind AWS Application Load Balancer with WAF. No direct internet access to application servers.
  
**Remote Access**: No VPN - all remote access via SSO to cloud applications. Engineers access AWS Console via SSO only.
  
**Traffic Monitoring**: VPC Flow Logs enabled. AWS GuardDuty for threat detection. Unusual traffic patterns trigger alerts.
  
  
## Examples of Good Implementation
- All application servers in private subnets with no public IP addresses
- AWS WAF protects APIs from common attacks (SQL injection, XSS)
- VPC Flow Logs sent to CloudWatch, analyzed for anomalies
- GuardDuty alerts on suspicious network activity (port scanning, crypto mining)
  
## Audit Evidence
- Network diagram showing segmentation
- VPC Flow Logs configuration
- AWS GuardDuty findings report
- WAF rules and blocked request metrics
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC6.6](../soc2/cc66.md)
- [CC6.7](../soc2/cc67.md)
  