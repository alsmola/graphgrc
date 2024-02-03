# BCD-12.1 - Transaction Recovery
Mechanisms exist to utilize specialized backup mechanisms that will allow transaction recovery for transaction-based applications and services in accordance with Recovery Point Objectives (RPOs).
## Mapped framework controls
### SOC 2
- [A1.2](../soc2/a12.md)
## Control questions
Does the organization utilize specialized backup mechanisms that will allow transaction recovery for transaction-based applications and services in accordance with Recovery Point Objectives (RPOs)?
## Control maturity
|       MATURITY LEVEL       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not performed              | There is no evidence of a capability to utilize specialized backup mechanisms that will allow transaction recovery for transaction-based applications and services in accordance with Recovery Point Objectives (RPOs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Performed internally       | SP-CMM1 is N/A, since a structured process is required to utilize specialized backup mechanisms that will allow transaction recovery for transaction-based applications and services in accordance with Recovery Point Objectives (RPOs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Planned and tracked        | Business Continuity & Disaster Recovery (BCD) efforts are requirements-driven and formally governed at a local/regional level, but are not consistent across the organization. CMM Level 2 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- Business Continuity / Disaster Recovery (BC/DR) management is decentralized (e.g., a localized/regionalized function) and uses non-standardized methods to implement secure and compliant practices.<br>- IT/cybersecurity personnel identify cybersecurity & data privacy controls that are appropriate to address applicable statutory, regulatory and contractual requirements for BC/DR management.<br>- BC/DR roles are formally assigned as an additional duty to existing IT/cybersecurity personnel.<br>- Recovery Time Objectives (RTOs) identify business-critical systems and services, which are given priority of service in alternate processing and storage sites.<br>- IT personnel develop Disaster Recovery Plans (DRP) to recover business-critical systems and services.<br>- Data/process owners conduct a Business Impact Analysis (BIA) at least annually, or after any major technology or process change, to identify assets critical to the business in need of protection, as well as single points of failure.<br>- IT/cybersecurity personnel work with business stakeholders to develop Business Continuity Plans (BCPs) to ensure business functions are sustainable both during and after an incident within Recovery Time Objectives (RTOs).<br>- IT personnel use a backup methodology (e.g., grandfather, father & s on rotation) to store backups in a secondary location, separate from the primary storage site.<br>- IT personnel configure business-critical systems to transfer backup data to the alternate storage site at a rate that is capable of meeting Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs). |
| Well defined               | Business Continuity & Disaster Recovery (BCD) efforts are standardized across the organization and centrally managed, where technically feasible, to ensure consistency. CMM Level 3 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- A formal Business Continuity & Disaster Recovery (BC/DR) program exists with defined roles and responsibilities to restore functionality in the event of a catastrophe, emergency, or significant disruptive incident that is handled in accordance with the Continuity of Operations Plan (COOP).<br>- BC/DR personnel work with business stakeholders to identify business-critical systems, services, internal teams and third-party service providers.<br>- Application/system/process owners conduct a Business Impact Analysis (BIA) at least annually, or after any major technology or process change, to identify assets critical to the business in need of protection, as well as single points of failure.<br>- Recovery Time Objectives (RTOs) are defined.<br>- Recovery Point Objectives (RPOs) are defined.<br>- Controls are assigned to sensitive/regulated assets to comply with specific BC/DR requirements to facilitate recovery operations in accordance with RTOs and RPOs.<br>- IT personnel work with business stakeholders to develop Disaster Recovery Plans (DRP) to recover business-critical systems and services within RPOs.<br>- Business stakeholders work with IT personnel to develop Business Continuity Plans (BCPs) to ensure business functions are sustainable both during and after an incident within RTOs.<br>- The data backup function is formally assigned with defined roles and responsibilities.<br>- Recoveries are performed into an isolated, non-production environment.                                                                                                                                                     |
| Quantitatively controllled | Business Continuity & Disaster Recovery (BCD) efforts are metrics driven and provide sufficient management insight (based on a quantitative understanding of process capabilities) to predict optimal performance, ensure continued operations and identify areas for improvement. In addition to CMM Level 3 criteria, CMM Level 4 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- 	Metrics reporting includes quantitative analysis of Key Performance Indicators (KPIs).<br>- 	Metrics reporting includes quantitative analysis of Key Risk Indicators (KRIs).<br>- 	Scope of metrics, KPIs and KRIs covers organization-wide cybersecurity & data privacy controls, including functions performed by third-parties.<br>- 	Organizational leadership maintains a formal process to objectively review and respond to metrics, KPIs and KRIs (e.g., monthly or quarterly review).<br>- 	Based on metrics analysis, process improvement recommendations are submitted for review and are handled in accordance with change control processes.<br>- 	Both business and technical stakeholders are involved in reviewing and approving proposed changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A, since a continuously-improving process is not necessary to utilize specialized backup mechanisms that will allow transaction recovery for transaction-based applications and services in accordance with Recovery Point Objectives (RPOs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |