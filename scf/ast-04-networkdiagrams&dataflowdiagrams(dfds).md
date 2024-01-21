# AST-04 - Network Diagrams & Data Flow Diagrams (DFDs)
Mechanisms exist to maintain network architecture diagrams that: 
 - Contain sufficient detail to assess the security of the network's architecture;
 - Reflect the current architecture of the network environment; and
 - Document all sensitive/regulated data flows.
## Mapped framework controls
### SOC 2
- [CC2.1](../soc2/cc21.md)
### GDPR
- [Art 30.1](../gdpr/art301.md)
- [Art 30.2](../gdpr/art302.md)
- [Art 30.3](../gdpr/art303.md)
- [Art 30.4](../gdpr/art304.md)
- [Art 30.5](../gdpr/art305.md)
## Control questions
Does the organization maintain network architecture diagrams that: 
 - Contain sufficient detail to assess the security of the network's architecture;
 - Reflect the current architecture of the network environment; and
 - Document all sensitive/regulated data flows?
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to maintain network |
|                            | architecture diagrams that:    |
|                            |  - Contain sufficient detail   |
|                            | to assess the security of      |
|                            | the network's architecture;    |
|                            |  - Reflect the current         |
|                            | architecture of the network    |
|                            | environment; and  - Document   |
|                            | all sensitive/regulated data   |
|                            | flows.                         |
| Performed internally       | Asset Management (AST)         |
|                            | efforts are ad hoc and         |
|                            | inconsistent. CMM Level        |
|                            | 1 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist: •	Asset      |
|                            | management is informally       |
|                            | assigned as an additional duty |
|                            | to existing IT/cybersecurity   |
|                            | personnel. •	Asset inventories  |
|                            | are performed in an ad hoc     |
|                            | manner. •	Software licensing    |
|                            | is tracked as part of IT       |
|                            | asset inventories. •	Data       |
|                            | process owners maintain        |
|                            | limited network diagrams       |
|                            | to document the flow of        |
|                            | sensitive/regulated data       |
|                            | that is specific to their      |
|                            | initiative. •	IT personnel work |
|                            | with data/process owners to    |
|                            | help ensure secure practices   |
|                            | are implemented throughout the |
|                            | System Development Lifecycle   |
|                            | (SDLC) for all high-value      |
|                            | projects. •	 on at least an     |
|                            | annual basis, or after any     |
|                            | major technology or process    |
|                            | change, network diagrams are   |
|                            | updated to reflect the current |
|                            | topology.                      |
| Planned and tracked        | Asset Management (AST) efforts |
|                            | are requirements-driven        |
|                            | and formally governed at a     |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM          |
|                            | Level 2 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most,         |
|                            | the following criteria to      |
|                            | exist: •	Asset management       |
|                            | is decentralized (e.g.,        |
|                            | a localized/regionalized       |
|                            | function) and uses             |
|                            | non-standardized methods to    |
|                            | implement secure and compliant |
|                            | practices. •	IT/cybersecurity   |
|                            | personnel identify             |
|                            | cybersecurity & data privacy   |
|                            | controls that are appropriate  |
|                            | to address applicable          |
|                            | statutory, regulatory and      |
|                            | contractual requirements       |
|                            | for asset management.          |
|                            | •	Administrative processes      |
|                            | and technologies focus on      |
|                            | protecting High Value Assets   |
|                            | (HVAs), including environments |
|                            | where sensitive/regulated data |
|                            | is stored, transmitted and     |
|                            | processed. •	Asset management   |
|                            | is formally assigned as an     |
|                            | additional duty to existing    |
|                            | IT/cybersecurity personnel.    |
|                            | •	Technology assets are         |
|                            | categorized according to data  |
|                            | classification and business    |
|                            | criticality. •	Inventories      |
|                            | cover technology assets        |
|                            | in scope for statutory,        |
|                            | regulatory and/ or contractual |
|                            | compliance, which includes     |
|                            | both physical and virtual      |
|                            | assets. •	Software licensing    |
|                            | is tracked as part of          |
|                            | IT asset inventories.          |
|                            | •	Users are educated on         |
|                            | their responsibilities         |
|                            | to protect technology          |
|                            | assets assigned to them or     |
|                            | under their supervision.       |
|                            | •	IT/cybersecurity personnel    |
|                            | maintain network diagrams      |
|                            | to document the flow           |
|                            | of sensitive/regulated         |
|                            | data across the network.       |
|                            | •	Data/process owners generate  |
|                            | Data Flow Diagrams (DFDs) and  |
|                            | network diagrams to document   |
|                            | the flow of data to create     |
|                            | and maintain a map of systems  |
|                            | where sensitive/regulated      |
|                            | data is stored, transmitted    |
|                            | or processed. •	Data/process    |
|                            | owners document where personal |
|                            | data is stored, transmitted    |
|                            | and/ or processed.             |
| Well defined               | Asset Management (AST)         |
|                            | efforts are standardized       |
|                            | across the organization and    |
|                            | centrally managed, where       |
|                            | technically feasible, to       |
|                            | ensure consistency. CMM        |
|                            | Level 3 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | •	An IT Asset Management        |
|                            | (ITAM) function, or similar    |
|                            | function, governs asset        |
|                            | management to help ensure      |
|                            | compliance with requirements   |
|                            | for asset management. •	An ITAM |
|                            | function, or similar function, |
|                            | maintains an inventory of      |
|                            | IT assets, covering both       |
|                            | physical and virtual assets,   |
|                            | as well as centrally managed   |
|                            | asset ownership assignments.   |
|                            | •	Technology assets and data    |
|                            | are categorized according      |
|                            | to data classification and     |
|                            | business criticality criteria. |
|                            | •	A Cybersecurity Supply Chain  |
|                            | Risk Management (C-SCRM)       |
|                            | function oversees supply       |
|                            | chain risks including the      |
|                            | removal and prevention of      |
|                            | certain technology services    |
|                            | and/ or equipment designated   |
|                            | as supply chain threats by a   |
|                            | statutory or regulatory body.  |
|                            | •	Data/process owners document  |
|                            | where sensitive/regulated      |
|                            | data is stored, transmitted    |
|                            | and processed, generating      |
|                            | Data Flow Diagrams (DFDs)      |
|                            | and network diagrams to        |
|                            | document the flow of data.     |
|                            | •	Stakeholders create network   |
|                            | diagrams that graphically      |
|                            | represent compliance           |
|                            | boundaries (e.g., in-scope vs  |
|                            | out-of-scope). •	Data/process   |
|                            | owners document where personal |
|                            | data is stored, transmitted    |
|                            | and/ or processed.             |
| Quantitatively controllled | Asset Management (AST)         |
|                            | efforts are metrics driven     |
|                            | and provide sufficient         |
|                            | management insight (based on   |
|                            | a quantitative understanding   |
|                            | of process capabilities)       |
|                            | to predict optimal             |
|                            | performance, ensure continued  |
|                            | operations and identify        |
|                            | areas for improvement. -       |
|                            | 	Metrics reporting includes     |
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
|                            | maintain network architecture  |
|                            | diagrams that:   - Contain     |
|                            | sufficient detail to           |
|                            | assess the security of the     |
|                            | network's architecture;        |
|                            |  - Reflect the current         |
|                            | architecture of the network    |
|                            | environment; and  - Document   |
|                            | all sensitive/regulated data   |
|                            | flows.                         |
