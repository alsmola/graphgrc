# CFG-01 - Configuration Management Program
Mechanisms exist to facilitate the implementation of configuration management controls.
## Mapped framework controls
### GDPR
- [Art 32.1](../gdpr/art321.md)
- [Art 32.2](../gdpr/art322.md)
### SOC 2
- [CC7.1](../soc2/cc71.md)
## Control questions
Does the organization facilitate the implementation of configuration management controls?
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to facilitate       |
|                            | the implementation of          |
|                            | configuration management       |
|                            | controls.                      |
| Performed internally       | Configuration Management       |
|                            | (CFG) efforts are ad hoc       |
|                            | and inconsistent. CMM Level    |
|                            | 1 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist: •	IT         |
|                            | personnel use an informal      |
|                            | process to design, build and   |
|                            | maintain secure configurations |
|                            | for test, development, staging |
|                            | and production environments.   |
|                            | •	Secure configurations         |
|                            | are not: o	Standardized         |
|                            | across the organization.       |
|                            | o	Consistently aligned with     |
|                            | industry-recognized standards  |
|                            | for hardening (e.g., DISA      |
|                            | STIGs, CIS Benchmarks or OEM   |
|                            | security guides).              |
| Planned and tracked        | Configuration Management       |
|                            | (CFG) efforts are              |
|                            | requirements-driven and        |
|                            | formally governed at a         |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM          |
|                            | Level 2 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | •	Configuration management      |
|                            | is decentralized (e.g.,        |
|                            | a localized/regionalized       |
|                            | function) and uses             |
|                            | non-standardized methods       |
|                            | to implement secure and        |
|                            | compliant practices.           |
|                            | •	IT/cybersecurity personnel    |
|                            | identify cybersecurity &       |
|                            | data privacy controls that     |
|                            | are appropriate to address     |
|                            | applicable statutory,          |
|                            | regulatory and contractual     |
|                            | requirements for configuration |
|                            | management. •	Technologies      |
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
|                            | cryptographic protections      |
|                            | for sensitive/regulated        |
|                            | data. •	Special baseline        |
|                            | configurations are created     |
|                            | for higher-risk environments   |
|                            | or for systems, applications   |
|                            | and services that store,       |
|                            | process or transmit            |
|                            | sensitive/regulated data.      |
|                            | •	Apart from workstation        |
|                            | and server operating system    |
|                            | baselines, configuration       |
|                            | management is decentralized.   |
|                            | •	Cybersecurity personnel       |
|                            | use a structured process to    |
|                            | design, build and maintain     |
|                            | secure configurations for      |
|                            | test, development, staging     |
|                            | and production environments.   |
|                            | •	Deviations to baseline        |
|                            | configurations are required    |
|                            | to have a risk assessment and  |
|                            | the business process owner     |
|                            | acceptance of the risk(s)      |
|                            | associated with the deviation. |
|                            | •	Unauthorized configuration    |
|                            | changes are investigated to    |
|                            | determine if the unauthorized  |
|                            | configuration is malicious     |
|                            | in nature. •	Logical Access     |
|                            | Control (LAC) is enforced to   |
|                            | prohibit non-administrative    |
|                            | users from being able to       |
|                            | install unauthorized software. |
| Well defined               | Configuration Management       |
|                            | (CFG) efforts are standardized |
|                            | across the organization and    |
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
|                            | business strategy to           |
|                            | determine prioritized and      |
|                            | authoritative guidance         |
|                            | for secure configuration       |
|                            | management practices. •	The     |
|                            | CISO, or similar function,     |
|                            | develops a security-focused    |
|                            | Concept of Operations          |
|                            | (CONOPS) that documents        |
|                            | management, operational and    |
|                            | technical measures to apply    |
|                            | defense-in-depth techniques    |
|                            | across the organization        |
|                            | with regards to secure         |
|                            | configuration management.      |
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
|                            | services and data to ensure    |
|                            | that secure configuration      |
|                            | management are identified      |
|                            | and documented. •	A steering    |
|                            | committee is formally          |
|                            | established to provide         |
|                            | executive oversight of the     |
|                            | cybersecurity & data privacy   |
|                            | program, including secure      |
|                            | configuration management       |
|                            | to provide clear and           |
|                            | authoritative accountability   |
|                            | for secure configuration       |
|                            | management operations. •	The    |
|                            | configuration management       |
|                            | function is formally           |
|                            | assigned with defined roles    |
|                            | and responsibilities. •	An      |
|                            | IT infrastructure team, or     |
|                            | similar function, ensures      |
|                            | that statutory, regulatory and |
|                            | contractual cybersecurity &    |
|                            | data privacy obligations are   |
|                            | addressed to ensure secure     |
|                            | configurations are designed,   |
|                            | built and maintained.          |
|                            | •	Configuration management is   |
|                            | centralized for all operating  |
|                            | systems, applications,         |
|                            | servers and other configurable |
|                            | technologies. •	Technologies    |
|                            | are configured to protect      |
|                            | data with the strength         |
|                            | and integrity commensurate     |
|                            | with the classification        |
|                            | or sensitivity of the          |
|                            | information and conform to     |
|                            | industry-recognized standards  |
|                            | for hardening (e.g., DISA      |
|                            | STIGs, CIS Benchmarks or OEM   |
|                            | security guides), including    |
|                            | test, development, staging     |
|                            | and production environments.   |
|                            | •	Configurations conform to     |
|                            | industry-recognized standards  |
|                            | for hardening (e.g., DISA      |
|                            | STIGs, CIS Benchmarks          |
|                            | or OEM security guides)        |
|                            | for test, development,         |
|                            | staging and production         |
|                            | environments. •	Deviations      |
|                            | to baseline configurations     |
|                            | are required to have a risk    |
|                            | assessment and business        |
|                            | process owner approval of      |
|                            | the risk(s) associated with    |
|                            | the deviation. •	Special        |
|                            | baseline configurations        |
|                            | are created for higher-risk    |
|                            | environments or for systems,   |
|                            | applications and services that |
|                            | store, process or transmit     |
|                            | sensitive/regulated data.      |
|                            | •	An IT Asset Management        |
|                            | (ITAM) function, or similar    |
|                            | function, ensures compliance   |
|                            | with requirements for          |
|                            | asset management. •	Logical     |
|                            | Access Control (LAC) is        |
|                            | used to limit the ability      |
|                            | of non-administrators from     |
|                            | making configuration changes   |
|                            | to systems, applications       |
|                            | and services, including        |
|                            | the of installation of         |
|                            | unauthorized software. •	A      |
|                            | Security Incident Event        |
|                            | Manager (SIEM), or similar     |
|                            | automated tool, monitors       |
|                            | for unauthorized activities,   |
|                            | accounts, connections, devices |
|                            | and software. Unauthorized     |
|                            | configuration changes are      |
|                            | responded to in accordance     |
|                            | with an Incident Response      |
|                            | Plan (IRP) to determine if the |
|                            | unauthorized configuration is  |
|                            | malicious in nature.           |
| Quantitatively controllled | Configuration Management       |
|                            | (CFG) efforts are metrics      |
|                            | driven and provide sufficient  |
|                            | management insight (based on   |
|                            | a quantitative understanding   |
|                            | of process capabilities) to    |
|                            | predict optimal performance,   |
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
| Continuously improving     | Configuration Management (CFG) |
|                            | efforts are “world-class”      |
|                            | capabilities that leverage     |
|                            | predictive analysis (e.g.,     |
|                            | machine learning, AI, etc.).   |
|                            | In addition to CMM Level 4     |
|                            | criteria, CMM Level 5 control  |
|                            | maturity would reasonably      |
|                            | expect all, or at least most,  |
|                            | the following criteria to      |
|                            | exist: - 	Stakeholders make     |
|                            | time-sensitive decisions       |
|                            | to support operational         |
|                            | efficiency, which may          |
|                            | include automated remediation  |
|                            | actions. - 	Based on predictive |
|                            | analysis, process improvements |
|                            | are implemented according      |
|                            | to “continuous improvement”    |
|                            | practices that affect process  |
|                            | changes.                       |
