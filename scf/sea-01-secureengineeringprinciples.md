# SEA-01 - Secure Engineering Principles
Mechanisms exist to facilitate the implementation of industry-recognized cybersecurity & data privacy practices in the specification, design, development, implementation and modification of systems and services.
## Mapped framework controls
### SOC 2
- [CC2.2](../soc2/cc22.md)
- [CC3.2](../soc2/cc32.md)
- [CC5.1](../soc2/cc51.md)
- [CC5.2](../soc2/cc52.md)
### GDPR
- [Art 24.1](../gdpr/art241.md)
- [Art 24.2](../gdpr/art242.md)
- [Art 24.3](../gdpr/art243.md)
- [Art 25.1](../gdpr/art251.md)
- [Art 25.2](../gdpr/art252.md)
- [Art 25.3](../gdpr/art253.md)
- [Art 32.1](../gdpr/art321.md)
- [Art 32.2](../gdpr/art322.md)
- [Art 40.2](../gdpr/art402.md)
- [Art 5.2](../gdpr/art52.md)
## Control questions
Does the organization facilitate the implementation of industry-recognized cybersecurity & data privacy practices in the specification, design, development, implementation and modification of systems and services?
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to facilitate       |
|                            | the implementation of          |
|                            | industry-recognized            |
|                            | cybersecurity & data           |
|                            | privacy practices in the       |
|                            | specification, design,         |
|                            | development, implementation    |
|                            | and modification of systems    |
|                            | and services.                  |
| Performed internally       | Secure Engineering &           |
|                            | Architecture (SEA) efforts     |
|                            | are ad hoc and inconsistent.   |
|                            | CMM Level 1 control maturity   |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | •	IT personnel use an informal  |
|                            | process to design, build and   |
|                            | maintain secure solutions.     |
|                            |  •	IT /cyber engineering        |
|                            | governance is decentralized,   |
|                            | with the responsibility for    |
|                            | implementing and testing       |
|                            | cybersecurity & data privacy   |
|                            | controls being assigned        |
|                            | to the business process        |
|                            | owner(s), including the        |
|                            | definition and enforcement of  |
|                            | roles and responsibilities.    |
|                            | •	Configurations mostly         |
|                            | conform to industry-recognized |
|                            | standards for hardening (e.g., |
|                            | DISA STIGs, CIS Benchmarks or  |
|                            | OEM security guides).          |
| Planned and tracked        | Secure Engineering &           |
|                            | Architecture (SEA) efforts     |
|                            | are requirements-driven        |
|                            | and formally governed at a     |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM          |
|                            | Level 2 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | •	Architecture/engineering      |
|                            | management is                  |
|                            | decentralized (e.g., a         |
|                            | localized/regionalized         |
|                            | function) and uses             |
|                            | non-standardized methods       |
|                            | to implement secure and        |
|                            | compliant practices. •	A        |
|                            | Change Advisory Board          |
|                            | (CAB), or similar function,    |
|                            | exists to govern changes to    |
|                            | systems, applications and      |
|                            | services, ensuring their       |
|                            | stability, reliability         |
|                            | and predictability.            |
|                            | •	Administrative processes      |
|                            | and technologies focus on      |
|                            | protecting High Value Assets   |
|                            | (HVAs), including environments |
|                            | where sensitive/regulated data |
|                            | is stored, transmitted and     |
|                            | processed. •	IT/cybersecurity   |
|                            | personnel identify             |
|                            | cybersecurity & data privacy   |
|                            | controls to address applicable |
|                            | statutory, regulatory and      |
|                            | contractual requirements       |
|                            | for architecture/engineering   |
|                            | management.  •	IT personnel     |
|                            | implement secure engineering   |
|                            | practices to protect the       |
|                            | confidentiality, integrity,    |
|                            | availability and safety        |
|                            | of the organization’s          |
|                            | technology assets, data and    |
|                            | network(s). •	Technologies      |
|                            | are configured to protect      |
|                            | data with the strength         |
|                            | and integrity commensurate     |
|                            | with the classification or     |
|                            | sensitivity of the information |
|                            | and mostly conform to          |
|                            | industry-recognized standards  |
|                            | for hardening (e.g., DISA      |
|                            | STIGs, CIS Benchmarks or OEM   |
|                            | security guides), including    |
|                            | cryptographic protections for  |
|                            | sensitive/regulated data.      |
| Well defined               | Secure Engineering &           |
|                            | Architecture (SEA) efforts     |
|                            | are standardized across        |
|                            | the organization and           |
|                            | centrally managed, where       |
|                            | technically feasible, to       |
|                            | ensure consistency. CMM Level  |
|                            | 3 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist: •	The Chief  |
|                            | Information Security Officer   |
|                            | (CISO), or similar function,   |
|                            | analyzes the organization’s    |
|                            | business strategy to determine |
|                            | prioritized and authoritative  |
|                            | guidance for secure            |
|                            | engineering practices. •	The    |
|                            | CISO, or similar function,     |
|                            | develops a security-focused    |
|                            | Concept of Operations          |
|                            | (CONOPS) that documents        |
|                            | management, operational and    |
|                            | technical measures to apply    |
|                            | defense-in-depth techniques    |
|                            | across the enterprise          |
|                            | for secure engineering.        |
|                            | •	A Governance, Risk &          |
|                            | Compliance (GRC) function,     |
|                            | or similar function, provides  |
|                            | governance oversight for the   |
|                            | implementation of applicable   |
|                            | statutory, regulatory and      |
|                            | contractual cybersecurity      |
|                            | & data privacy controls to     |
|                            | protect the confidentiality,   |
|                            | integrity, availability and    |
|                            | safety of the organization’s   |
|                            | applications, systems,         |
|                            | services and data with         |
|                            | regards to secure engineering. |
|                            | •	A steering committee is       |
|                            | formally established to        |
|                            | provide executive oversight    |
|                            | of the cybersecurity & data    |
|                            | privacy program, including     |
|                            | secure engineering.            |
|                            | •	IT/cybersecurity architects,  |
|                            | or a similar function,         |
|                            | enable the implementation      |
|                            | a “layered defense” network    |
|                            | architecture that enables a    |
|                            | resilient defense-in-depth     |
|                            | approach through the use       |
|                            | of industry-recognized         |
|                            | cybersecurity & data           |
|                            | privacy practices in the       |
|                            | specification, design,         |
|                            | development, implementation    |
|                            | and modification of systems    |
|                            | and services (e.g., DISA       |
|                            | STIGs, CIS Benchmarks          |
|                            | or OEM security guides).       |
|                            | •	IT/cybersecurity engineers,   |
|                            | or a similar function,         |
|                            | operationalize enterprise      |
|                            | architecture, aligned with     |
|                            | industry-recognized leading    |
|                            | practices, with consideration  |
|                            | for cybersecurity & data       |
|                            | privacy principles, including  |
|                            | resiliency expectations,       |
|                            | that addresses risk to         |
|                            | organizational operations,     |
|                            | assets, individuals,           |
|                            | other organizations.  •	A       |
|                            | Validated Architecture         |
|                            | Design Review (VADR), or       |
|                            | similar process, is used       |
|                            | to evaluate design criteria    |
|                            | for secure practices and       |
|                            | conformance with requirements  |
|                            | for applicable statutory,      |
|                            | regulatory and contractual     |
|                            | controls to determine if the   |
|                            | system/application/service is  |
|                            | designed, built and operated   |
|                            | in a secure and resilient      |
|                            | manner.  •	A Change Advisory    |
|                            | Board (CAB), or similar        |
|                            | function, governs changes      |
|                            | to systems, applications       |
|                            | and services to ensure their   |
|                            | stability, reliability and     |
|                            | predictability.  •	A formal     |
|                            | Change Management (CM)         |
|                            | program helps to ensure        |
|                            | that no unauthorized changes   |
|                            | are made, all changes are      |
|                            | documented, services are not   |
|                            | disrupted and resources are    |
|                            | used efficiently. •	An Identity |
|                            | & Access Management (IAM)      |
|                            | function, or similar function, |
|                            | enables the implementation     |
|                            | of identification and access   |
|                            | management controls for        |
|                            | “least privileges” practices,  |
|                            | allowing for the management    |
|                            | of user, group and system      |
|                            | accounts, including privileged |
|                            | accounts. •	An IT Asset         |
|                            | Management (ITAM) function, or |
|                            | similar function, categorizes  |
|                            | assets according to the data   |
|                            | the asset stores, transmits    |
|                            | and/ or processes and applies  |
|                            | the appropriate technology     |
|                            | controls to protect the asset  |
|                            | and data.                      |
| Quantitatively controllled | Secure Engineering &           |
|                            | Architecture (SEA) efforts     |
|                            | are metrics driven and provide |
|                            | sufficient management insight  |
|                            | (based on a quantitative       |
|                            | understanding of process       |
|                            | capabilities) to predict       |
|                            | optimal performance,           |
|                            | ensure continued operations    |
|                            | and identify areas for         |
|                            | improvement. In addition to    |
|                            | CMM Level 3 criteria, CMM      |
|                            | Level 4 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | - 	Metrics reporting includes   |
|                            | quantitative analysis of Key   |
|                            | Performance Indicators (KPIs). |
|                            | - 	Metrics reporting includes   |
|                            | quantitative analysis of Key   |
|                            | Risk Indicators (KRIs). -      |
|                            | 	Scope of metrics, KPIs and     |
|                            | KRIs covers organization-wide  |
|                            | cybersecurity & data privacy   |
|                            | controls, including functions  |
|                            | performed by third-parties.    |
|                            | - 	Organizational leadership    |
|                            | maintains a formal process to  |
|                            | objectively review and respond |
|                            | to metrics, KPIs and KRIs      |
|                            | (e.g., monthly or quarterly    |
|                            | review). - 	Based on metrics    |
|                            | analysis, process improvement  |
|                            | recommendations are submitted  |
|                            | for review and are handled in  |
|                            | accordance with change control |
|                            | processes. - 	Both business     |
|                            | and technical stakeholders     |
|                            | are involved in reviewing and  |
|                            | approving proposed changes.    |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A,   |
|                            | since a continuously-improving |
|                            | process is not necessary to    |
|                            | facilitate the implementation  |
|                            | of industry-recognized         |
|                            | cybersecurity & data           |
|                            | privacy practices in the       |
|                            | specification, design,         |
|                            | development, implementation    |
|                            | and modification of systems    |
|                            | and services.                  |
