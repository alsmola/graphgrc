# INF-03: Logging & Monitoring
**Category: **Infrastructure Security
  
## Objective
Enable security incident detection and investigation through comprehensive logging.
  
## Description
Security events and system activities are logged centrally. Logs are monitored for anomalies and security incidents. Logs are retained and protected from tampering.
  
## Implementation Guidance
**Centralized Logging**: All AWS CloudTrail, VPC Flow Logs, application logs sent to CloudWatch Logs. Immutable storage in S3.
  
**Security Monitoring**: AWS GuardDuty for threat detection. CloudWatch alarms for critical events (root account usage, unauthorized API calls).
  
**Alerting**: PagerDuty integration for security alerts. P0/P1 alerts page on-call engineer 24/7.
  
**Log Retention**: Security logs retained 7 years. Application logs 90 days. Logs encrypted and access-controlled.
  
  
## Examples of Good Implementation
- CloudTrail logs every AWS API call across all regions to immutable S3 bucket
- Failed authentication attempts trigger alert after 5 failures in 5 minutes
- GuardDuty detected and alerted on compromised EC2 instance (bitcoin mining)
- Security team can search all logs in CloudWatch Insights for investigation
  
## Audit Evidence
- CloudTrail configuration showing all regions enabled
- CloudWatch alarm definitions
- PagerDuty integration and alert history
- Log retention policy and S3 lifecycle configuration
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [CC7.2](../soc2/cc72.md)
- [CC7.3](../soc2/cc73.md)
  