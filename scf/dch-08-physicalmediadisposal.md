# DCH-08 - Physical Media Disposal
Mechanisms exist to securely dispose of media when it is no longer required, using formal procedures. 
## Mapped framework controls
### SOC 2
- [CC6.5](../soc2/cc65.md)
## Control questions
Does the organization securely dispose of media when it is no longer required, using formal procedures? 
## Control maturity
|       MATURITY LEVEL       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not performed              | There is no evidence of a capability to securely dispose of media when it is no longer required, using formal procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Performed internally       | SP-CMM1 is N/A, since a structured process is required to securely dispose of media when it is no longer required, using formal procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Planned and tracked        | Data Classification & Handling (DCH) efforts are requirements-driven and formally governed at a local/regional level, but are not consistent across the organization. CMM Level 2 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- Data management is decentralized (e.g., a localized/regionalized function) and uses non-standardized methods to implement secure and compliant practices.<br>- IT/cybersecurity personnel identify cybersecurity & data privacy controls that are appropriate to address applicable statutory, regulatory and contractual requirements for data management.<br>- Data protection controls are primarily administrative and preventative in nature (e.g., policies & standards) to classify, protect and dispose of systems and data, including storage media.<br>- A data classification process exists to identify categories of data and specific protection requirements.<br>- A data retention process exists and is a manual process to govern.<br>- Data/process owners:<br>o	Document where sensitive/regulated data is stored, transmitted and processed to identify data repositories and data flows.<br>o	Create and maintain Data Flow Diagrams (DFDs) and network diagrams.<br>o	Are expected to take the initiative to work with Data Protection Officers (DPOs) to ensure applicable statutory, regulatory and contractual obligations are properly addressed, including the storage, transmission and processing of sensitive/regulated data<br>- A manual data retention process exists.<br>- Content filtering blocks users from performing ad hoc file transfers through unapproved file transfer services (e.g., Box, Dropbox, Google Drive, etc.).<br>- Mobile Device Management (MDM) software is used to restrict and protect the data that resides on mobile devices.<br>- Physical controls, administrative processes and technologies focus on protecting High Value Assets (HVAs), including environments where sensitive/regulated data is stored, transmitted and processed.<br>- Administrative means (e.g., policies and standards) dictate:<br>o	Geolocation requirements for sensitive/regulated data types, including the transfer of data to third-countries or international organizations.<br>o	Requirements for minimizing data collection to what is necessary for business purposes.<br>o	Requirements for limiting the use of sensitive/regulated data in testing, training and research. |
| Well defined               | Data Classification & Handling (DCH) efforts are standardized across the organization and centrally managed, where technically feasible, to ensure consistency. CMM Level 3 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- A Governance, Risk & Compliance (GRC) function, or similar function, assists users in making information sharing decisions to ensure data is appropriately protected, regardless of where or how it is stored, processed and/ or transmitted.<br>- A data classification process exists to identify categories of data and specific protection requirements.<br>- A data retention process exists to protect archived data in accordance with applicable statutory, regulatory and contractual obligations. <br>- Data/process owners:<br>o	Are expected to take the initiative to work with Data Protection Officers (DPOs) to ensure applicable statutory, regulatory and contractual obligations are properly addressed, including the storage, transmission and processing of sensitive/regulated data.<br>o	Maintain decentralized inventory logs of all sensitive/regulated media and update sensitive/regulated media inventories at least annually. <br>o	Create and maintain Data Flow Diagrams (DFDs) and network diagrams.<br>o	Document where sensitive/regulated data is stored, transmitted and processed in order to document data repositories and data flows.<br>- Devices are escrowed in storage for a period of time before being wiped and reissued, in case data on the devices are needed for investigations or business purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Quantitatively controllled | Data Classification & Handling (DCH) efforts are metrics driven and provide sufficient management insight (based on a quantitative understanding of process capabilities) to predict optimal performance, ensure continued operations and identify areas for improvement. In addition to CMM Level 3 criteria, CMM Level 4 control maturity would reasonably expect all, or at least most, the following criteria to exist:<br>- 	Metrics reporting includes quantitative analysis of Key Performance Indicators (KPIs).<br>- 	Metrics reporting includes quantitative analysis of Key Risk Indicators (KRIs).<br>- 	Scope of metrics, KPIs and KRIs covers organization-wide cybersecurity & data privacy controls, including functions performed by third-parties.<br>- 	Organizational leadership maintains a formal process to objectively review and respond to metrics, KPIs and KRIs (e.g., monthly or quarterly review).<br>- 	Based on metrics analysis, process improvement recommendations are submitted for review and are handled in accordance with change control processes.<br>- 	Both business and technical stakeholders are involved in reviewing and approving proposed changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A, since a continuously-improving process is not necessary to securely dispose of media when it is no longer required, using formal procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |