# SEA-15 - Distributed Processing & Storage
Mechanisms exist to distribute processing and storage across multiple physical locations. 
## Mapped framework controls
### GDPR
- [Art 26.1](../gdpr/art261.md)
- [Art 26.2](../gdpr/art262.md)
- [Art 26.3](../gdpr/art263.md)
- [Art 28.10](../gdpr/art2810.md)
- [Art 28.1](../gdpr/art281.md)
- [Art 28.2](../gdpr/art282.md)
- [Art 28.3](../gdpr/art283.md)
- [Art 28.4](../gdpr/art284.md)
- [Art 28.5](../gdpr/art285.md)
- [Art 28.6](../gdpr/art286.md)
- [Art 28.9](../gdpr/art289.md)
- [Art 29](../gdpr/art29.md)
- [Art 44](../gdpr/art44.md)
- [Art 45.1](../gdpr/art451.md)
- [Art 45.2](../gdpr/art452.md)
- [Art 46.1](../gdpr/art461.md)
- [Art 46.2](../gdpr/art462.md)
- [Art 46.3](../gdpr/art463.md)
- [Art 47.1](../gdpr/art471.md)
- [Art 47.2](../gdpr/art472.md)
- [Art 48](../gdpr/art48.md)
- [Art 49.1](../gdpr/art491.md)
- [Art 49.2](../gdpr/art492.md)
- [Art 49.6](../gdpr/art496.md)
- [Art 6.1](../gdpr/art61.md)
## Control questions
Does the organization distribute processing and storage across multiple physical locations? 
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to distribute       |
|                            | processing and storage across  |
|                            | multiple physical locations.   |
| Performed internally       | Secure Engineering &           |
|                            | Architecture (SEA) efforts are |
|                            | ad hoc and inconsistent. CMM   |
|                            | Level 1 control maturity would |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist:<br>- IT     |
|                            | personnel use an informal      |
|                            | process to design, build and   |
|                            | maintain secure solutions.     |
|                            | <br>- IT /cyber engineering    |
|                            | governance is decentralized,   |
|                            | with the responsibility for    |
|                            | implementing and testing       |
|                            | cybersecurity & data privacy   |
|                            | controls being assigned to     |
|                            | the business process owner(s), |
|                            | including the definition       |
|                            | and enforcement of roles and   |
|                            | responsibilities.              |
| Planned and tracked        | Secure Engineering &           |
|                            | Architecture (SEA) efforts     |
|                            | are requirements-driven        |
|                            | and formally governed at a     |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM Level    |
|                            | 2 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist:<br>-        |
|                            | Architecture/engineering       |
|                            | management is                  |
|                            | decentralized (e.g., a         |
|                            | localized/regionalized         |
|                            | function) and uses             |
|                            | non-standardized methods       |
|                            | to implement secure and        |
|                            | compliant practices.<br>-      |
|                            | A Change Advisory Board        |
|                            | (CAB), or similar function,    |
|                            | exists to govern changes to    |
|                            | systems, applications and      |
|                            | services, ensuring their       |
|                            | stability, reliability         |
|                            | and predictability. <br>-      |
|                            | Administrative processes       |
|                            | and technologies focus on      |
|                            | protecting High Value Assets   |
|                            | (HVAs), including environments |
|                            | where sensitive/regulated      |
|                            | data is stored, transmitted    |
|                            | and processed.<br>-            |
|                            | IT/cybersecurity personnel     |
|                            | identify cybersecurity         |
|                            | & data privacy controls        |
|                            | to address applicable          |
|                            | statutory, regulatory and      |
|                            | contractual requirements       |
|                            | for architecture/engineering   |
|                            | management. <br>- IT           |
|                            | personnel implement secure     |
|                            | engineering practices to       |
|                            | protect the confidentiality,   |
|                            | integrity, availability and    |
|                            | safety of the organization’s   |
|                            | technology assets, data and    |
|                            | network(s).<br>- Technologies  |
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
|                            | criteria to exist:<br>-        |
|                            | IT/cybersecurity architects,   |
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
|                            | STIGs, CIS Benchmarks or       |
|                            | OEM security guides).<br>-     |
|                            | IT/cybersecurity engineers,    |
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
|                            | assets, individuals, other     |
|                            | organizations. <br>- A         |
|                            | Validated Architecture         |
|                            | Design Review (VADR), or       |
|                            | similar process, is used       |
|                            | to evaluate design criteria    |
|                            | for secure practices and       |
|                            | conformance with requirements  |
|                            | for applicable statutory,      |
|                            | regulatory and contractual     |
|                            | controls to determine if the   |
|                            | system/application/service     |
|                            | is designed, built and         |
|                            | operated in a secure           |
|                            | and resilient manner.          |
|                            | <br>- A Change Advisory        |
|                            | Board (CAB), or similar        |
|                            | function, governs changes      |
|                            | to systems, applications       |
|                            | and services to ensure their   |
|                            | stability, reliability and     |
|                            | predictability. <br>- A formal |
|                            | Change Management (CM) program |
|                            | helps to ensure that no        |
|                            | unauthorized changes are made, |
|                            | all changes are documented,    |
|                            | services are not disrupted     |
|                            | and resources are used         |
|                            | efficiently.<br>- An Identity  |
|                            | & Access Management (IAM)      |
|                            | function, or similar function, |
|                            | enables the implementation     |
|                            | of identification and access   |
|                            | management controls for        |
|                            | “least privileges” practices,  |
|                            | allowing for the management    |
|                            | of user, group and system      |
|                            | accounts, including privileged |
|                            | accounts.<br>- An IT Asset     |
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
|                            | all, or at least most,         |
|                            | the following criteria to      |
|                            | exist:<br>- 	Metrics reporting  |
|                            | includes quantitative          |
|                            | analysis of Key Performance    |
|                            | Indicators (KPIs).<br>-        |
|                            | 	Metrics reporting includes     |
|                            | quantitative analysis of Key   |
|                            | Risk Indicators (KRIs).<br>-   |
|                            | 	Scope of metrics, KPIs and     |
|                            | KRIs covers organization-wide  |
|                            | cybersecurity & data           |
|                            | privacy controls, including    |
|                            | functions performed            |
|                            | by third-parties.<br>-         |
|                            | 	Organizational leadership      |
|                            | maintains a formal process to  |
|                            | objectively review and respond |
|                            | to metrics, KPIs and KRIs      |
|                            | (e.g., monthly or quarterly    |
|                            | review).<br>- 	Based on metrics |
|                            | analysis, process improvement  |
|                            | recommendations are submitted  |
|                            | for review and are handled in  |
|                            | accordance with change control |
|                            | processes.<br>- 	Both business  |
|                            | and technical stakeholders     |
|                            | are involved in reviewing and  |
|                            | approving proposed changes.    |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A,   |
|                            | since a continuously-improving |
|                            | process is not necessary       |
|                            | to distribute processing       |
|                            | and storage across multiple    |
|                            | physical locations.            |
