---
type: standard
id: standard-logging-monitoring
title: Logging and Monitoring Standard
owner: infrastructure-team
last_reviewed: 2025-01-09
review_cadence: quarterly
applies_to: [engineers, infrastructure-team]
---

# Logging and Monitoring Standard

Requirements for security logging, monitoring, and alerting.

## Scope

All production systems, applications, infrastructure, and SaaS applications.

## Log Requirements

### What to Log

**Application logs:**
- Authentication events (login, logout, failed attempts)
- Authorization decisions (access granted/denied)
- Data access (read/write Confidential data)
- Configuration changes
- Error conditions and exceptions

**Infrastructure logs:**
- AWS CloudTrail (API calls)
- VPC Flow Logs (network traffic)
- Load balancer access logs
- DNS query logs
- Firewall/WAF logs

**SaaS audit logs:**
- User provisioning/deprovisioning
- Permission changes
- Admin actions
- Data export/download events

### What NOT to Log

- Passwords, API keys, secrets, tokens
- Full credit card numbers, SSNs
- Customer PII unless necessary for audit (hash/redact)

### Log Format

- Structured logging (JSON preferred)
- Required fields: timestamp (UTC), user/actor, action, resource, result (success/failure), source IP
- Include request/correlation ID for distributed tracing

## Log Storage

### Centralization

- All logs forwarded to centralized logging system (AWS CloudWatch, Datadog, Splunk)
- Real-time or near-real-time ingestion (< 5 minute delay)
- Separate log storage from source systems (immutability)

### Retention

- Security logs: 1 year minimum (2 years for SOC 2)
- Audit logs (access to Confidential data): 2 years
- Infrastructure logs: 90 days
- Application logs (non-security): 30 days

### Protection

- Logs encrypted at rest and in transit
- Access to logs restricted to security team, SRE, and authorized engineers
- Log tampering detection (integrity checking)

## Monitoring and Alerting

### Critical Security Events (Page immediately)

- Root account login (AWS)
- MFA disabled on privileged account
- Security group allows 0.0.0.0/0 on sensitive ports (RDP, SSH)
- IAM policy changes affecting production
- GuardDuty High/Critical findings
- Multiple failed authentication attempts (brute force)
- Unauthorized data access or export

### Important Security Events (Alert in Slack)

- New user provisioned with admin privileges
- CloudTrail disabled
- S3 bucket made public
- Certificate expiring in < 30 days
- Vulnerability scanner findings (Critical/High)

### Monitoring Coverage

- Infrastructure availability (uptime)
- Application performance (latency, errors)
- Security metrics (failed logins, policy violations)
- Compliance metrics (encryption enabled, patches applied)

## Log Analysis

- Weekly review of security logs by security team
- Automated anomaly detection where possible
- Quarterly log review for compliance audit preparation

## References

- Related controls: INF-03, OPS-03
- Related process: incident-response-process.md
- OWASP Logging Cheat Sheet

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to controls using the format: [Control Name](../controls/{family}/{control}.md) ^[annotation] -->

- [Logging & Monitoring](../controls/infrastructure-security/logging-monitoring.md) ^[CloudWatch centralized logging with structured JSON format, 2-year audit log retention per SOC 2, encryption at rest and in transit]
- [Infrastructure Observability](../controls/infrastructure-security/logging-monitoring.md) ^[CloudTrail for API calls, VPC Flow Logs, load balancer logs, DNS query logs, firewall/WAF logs]
- [Endpoint Observability](../controls/monitoring/endpoint-observability.md) ^[Application logs for authentication, authorization, data access, configuration changes]
- [SIEM](../controls/monitoring/siem.md) ^[Real-time log ingestion (<5 min delay), weekly security log review, quarterly compliance audit preparation]
- [Cloud Threat Detection](../controls/threat-detection/cloud-threat-detection.md) ^[GuardDuty High/Critical findings trigger immediate alerts, critical security event monitoring]
- [Security Incident Response](../controls/incident-response/security-incident-response.md) ^[Security event monitoring for detection, centralized logs for forensic investigation]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[Audit logs track privileged authentication and authorization events for access review validation]
- [Privileged Access Management](../controls/iam/privileged-access-management.md) ^[CloudTrail logs all admin API calls, immediate alerts on root account login and IAM policy changes]
- [Cloud Security Configuration (AWS)](../controls/infrastructure-security/cloud-security-configuration-aws.md) ^[CloudTrail enabled in all regions, VPC Flow Logs for network monitoring]
- [Data Retention and Deletion](../controls/data-management/data-retention-and-deletion.md) ^[Security logs retained 1 year minimum, audit logs 2 years, application logs 30 days, infrastructure metrics 90 days]
- [Availability Monitoring](../controls/availability/availability-monitoring.md) ^[CloudWatch monitors infrastructure health metrics, APM tracks application performance, external uptime monitoring checks endpoints, PagerDuty alerts on-call engineers]
- [Capacity Planning](../controls/availability/capacity-planning.md) ^[CloudWatch capacity utilization reports track CPU, memory, storage, network usage trends, alert at 80% thresholds]
- [Insider Threat Mitigation](../controls/personnel-security/insider-threat-mitigation.md) ^[SIEM monitors for anomalous activity including unusual access times, mass downloads, privilege escalation, critical actions logged]

---

<!-- Backlinks auto-generated below -->
