# BCD-06 - Contingency Planning & Updates
Mechanisms exist to keep contingency plans current with business needs, technology changes and feedback from contingency plan testing activities.
## Control questions
Does the organization keep contingency plans current with business needs, technology changes and feedback from contingency plan testing activities?
## Control maturity
### Not performed
There is no evidence of a capability to keep contingency plans current with business needs, technology changes and feedback from contingency plan testing activities.
### Performed internally
Business Continuity & Disaster Recovery (BCD) efforts are ad hoc and inconsistent. CMM Level 1 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	IT personnel work with business stakeholders to identify business-critical systems and services, including internal teams and third-party service providers.
•	IT personnel develop limited Disaster Recovery Plans (DRP) to recover business-critical systems and services.
•	Business stakeholders develop limited Business Continuity Plans (BCPs) to ensure business-critical functions are sustainable both during and after an incident within Recovery Time Objectives (RTOs).
•	Backups are performed ad-hoc and focus on business-critical systems.
•	Limited technologies exist to support near real-time network infrastructure failover (e.g., redundant ISPs, redundant power, etc.).
•	IT personnel work with business stakeholders to identify alternative or compensating controls to address control deficiencies, if the primary means of implementing the security function is unavailable or compromised.
### Planned and tracked
Business Continuity & Disaster Recovery (BCD) efforts are requirements-driven and formally governed at a local/regional level, but are not consistent across the organization. CMM Level 2 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	Business Continuity / Disaster Recovery (BC/DR) management is decentralized (e.g., a localized/regionalized function) and uses non-standardized methods to implement secure and compliant practices.
•	IT/cybersecurity personnel identify cybersecurity & data privacy controls that are appropriate to address applicable statutory, regulatory and contractual requirements for BC/DR management.
•	BC/DR roles are formally assigned as an additional duty to existing IT/cybersecurity personnel.
•	Recovery Time Objectives (RTOs) identify business-critical systems and services, which are given priority of service in alternate processing and storage sites.
•	IT personnel develop Disaster Recovery Plans (DRP) to recover business-critical systems and services.
•	Data/process owners conduct a Business Impact Analysis (BIA) at least annually, or after any major technology or process change, to identify assets critical to the business in need of protection, as well as single points of failure.
•	IT/cybersecurity personnel work with business stakeholders to develop Business Continuity Plans (BCPs) to ensure business functions are sustainable both during and after an incident within Recovery Time Objectives (RTOs).
•	IT personnel use a backup methodology (e.g., grandfather, father & s on rotation) to store backups in a secondary location, separate from the primary storage site.
•	IT personnel configure business-critical systems to transfer backup data to the alternate storage site at a rate that is capable of meeting Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs).
•	 on at least an annual basis, or after any major technology or process change, the data/process owner updates the data mapping documentation.
### Well defined
Business Continuity & Disaster Recovery (BCD) efforts are standardized across the organization and centrally managed, where technically feasible, to ensure consistency. CMM Level 3 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	A formal Business Continuity & Disaster Recovery (BC/DR) program exists with defined roles and responsibilities to restore functionality in the event of a catastrophe, emergency, or significant disruptive incident that is handled in accordance with the Continuity of Operations Plan (COOP).
•	BC/DR personnel work with business stakeholders to identify business-critical systems, services, internal teams and third-party service providers.
•	Application/system/process owners conduct a Business Impact Analysis (BIA) at least annually, or after any major technology or process change, to identify assets critical to the business in need of protection, as well as single points of failure.
•	Recovery Time Objectives (RTOs) are defined.
•	Recovery Point Objectives (RPOs) are defined.
•	Controls are assigned to sensitive/regulated assets to comply with specific BC/DR requirements to facilitate recovery operations in accordance with RTOs and RPOs.
•	IT personnel work with business stakeholders to develop Disaster Recovery Plans (DRP) to recover business-critical systems and services within RPOs.
•	Business stakeholders work with IT personnel to develop Business Continuity Plans (BCPs) to ensure business functions are sustainable both during and after an incident within RTOs.
•	The data backup function is formally assigned with defined roles and responsibilities.
•	 on at least an annual basis, or after any major technology or process change, the data/process owner updates the data mapping documentation.
### Quantitatively controllled
Business Continuity & Disaster Recovery (BCD) efforts are metrics driven and provide sufficient management insight (based on a quantitative understanding of process capabilities) to predict optimal performance, ensure continued operations and identify areas for improvement. In addition to CMM Level 3 criteria, CMM Level 4 control maturity would reasonably expect all, or at least most, the following criteria to exist:
- 	Metrics reporting includes quantitative analysis of Key Performance Indicators (KPIs).
- 	Metrics reporting includes quantitative analysis of Key Risk Indicators (KRIs).
- 	Scope of metrics, KPIs and KRIs covers organization-wide cybersecurity & data privacy controls, including functions performed by third-parties.
- 	Organizational leadership maintains a formal process to objectively review and respond to metrics, KPIs and KRIs (e.g., monthly or quarterly review).
- 	Based on metrics analysis, process improvement recommendations are submitted for review and are handled in accordance with change control processes.
- 	Both business and technical stakeholders are involved in reviewing and approving proposed changes.
### Continuously improving
See SP-CMM4. SP-CMM5 is N/A, since a continuously-improving process is not necessary to keep contingency plans current with business needs, technology changes and feedback from contingency plan testing activities.
## Mapped framework controls
### SOC 2
- [CC7.5](../soc2/cc75.md)