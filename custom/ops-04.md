# OPS-04: Business Continuity
**Category: **Operational Security
  
## Objective
Ensure business operations can continue during disruptions.
  
## Description
Business continuity and disaster recovery plans are documented and tested. Critical systems have defined RTO and RPO. Failover procedures are tested. Alternative processing sites are available.
  
## Implementation Guidance
**BC/DR Plan**: Written plan covering key scenarios (data center outage, natural disaster, cyber attack). Roles and responsibilities defined.
  
**RTO/RPO Targets**: Production database RTO 4 hours, RPO 1 hour. Application servers RTO 2 hours (auto-scaling).
  
**AWS Multi-Region**: Critical services can failover to alternate AWS region. Route53 health checks enable automatic failover.
  
**Annual Testing**: BC/DR plan tested annually via tabletop or live failover exercise. Plan updated based on findings.
  
  
## Examples of Good Implementation
- Production database has multi-AZ deployment with automatic failover
- Route53 configured to failover to us-west-2 if us-east-1 unhealthy
- Annual DR test failed over production to alternate region, verified RTO target met
- Communications plan includes customer notification templates for major outages
  
## Audit Evidence
- Business continuity plan
- RTO/RPO definitions for critical systems
- Annual BC/DR test results
- Multi-region architecture diagram
  
---
  
## Mapped framework controls
### GDPR
- [Art 32](../gdpr/art32.md)
  
### SOC 2
- [A1.1](../soc2/a11.md)
- [A1.2](../soc2/a12.md)
- [A1.3](../soc2/a13.md)
  