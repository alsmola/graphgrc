# SEA-01.1 - Centralized Management of Cybersecurity & Data Privacy Controls
Mechanisms exist to centrally-manage the organization-wide management and implementation of cybersecurity & data privacy controls and related processes.
## Mapped framework controls
### SOC 2
- [CC5.1](../soc2/cc51.md)
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
Does the organization centrally-manage the organization-wide management and implementation of cybersecurity & data privacy controls and related processes?
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to centrally-manage |
|                            | the organization-wide          |
|                            | management and implementation  |
|                            | of cybersecurity & data        |
|                            | privacy controls and related   |
|                            | processes.                     |
| Performed internally       | SP-CMM1 is N/A, since          |
|                            | a structured process is        |
|                            | required to centrally-manage   |
|                            | the organization-wide          |
|                            | management and implementation  |
|                            | of cybersecurity & data        |
|                            | privacy controls and related   |
|                            | processes.                     |
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
|                            | to centrally-manage the        |
|                            | organization-wide management   |
|                            | and implementation of          |
|                            | cybersecurity & data           |
|                            | privacy controls and related   |
|                            | processes.                     |
