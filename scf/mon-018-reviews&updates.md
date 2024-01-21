# MON-01.8 - Reviews & Updates
Mechanisms exist to review event logs on an ongoing basis and escalate incidents in accordance with established timelines and procedures.
## Mapped framework controls
### SOC 2
- [CC7.2](../soc2/cc72.md)
## Control questions
Does the organization review event logs on an ongoing basis and escalate incidents in accordance with established timelines and procedures?
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to review event     |
|                            | logs on an ongoing basis       |
|                            | and escalate incidents in      |
|                            | accordance with established    |
|                            | timelines and procedures.      |
| Performed internally       | Continuous Monitoring (MON)    |
|                            | efforts are ad hoc and         |
|                            | inconsistent. CMM Level        |
|                            | 1 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist: •	Generating |
|                            | event logs and the review of   |
|                            | event logs is narrowly-focused |
|                            | to business-critical           |
|                            | systems and/ or systems that   |
|                            | store, processes and/ or       |
|                            | transmit sensitive/regulated   |
|                            | data. •	Secure baseline         |
|                            | configurations generate        |
|                            | logs that contain sufficient   |
|                            | information to establish       |
|                            | necessary details of activity  |
|                            | and allow for forensics        |
|                            | analysis.                      |
| Planned and tracked        | Continuous Monitoring          |
|                            | (MON) efforts are              |
|                            | requirements-driven and        |
|                            | formally governed at a         |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM          |
|                            | Level 2 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most,         |
|                            | the following criteria         |
|                            | to exist: •	Situational         |
|                            | awareness management is        |
|                            | decentralized (e.g., a         |
|                            | localized/regionalized         |
|                            | function) and uses             |
|                            | non-standardized methods to    |
|                            | implement secure and compliant |
|                            | practices. •	Secure baseline    |
|                            | configurations generate        |
|                            | logs that contain sufficient   |
|                            | information to establish       |
|                            | necessary details of activity  |
|                            | and allow for forensics        |
|                            | analysis. •	IT/cybersecurity    |
|                            | personnel: o	Identify           |
|                            | cybersecurity & data privacy   |
|                            | controls that are appropriate  |
|                            | to address applicable          |
|                            | statutory, regulatory and      |
|                            | contractual requirements       |
|                            | for situational awareness      |
|                            | management. o	Configure alerts  |
|                            | for critical or sensitive data |
|                            | that is stored, transmitted    |
|                            | and processed on assets.       |
|                            | o	Use a structured process      |
|                            | to review and analyze          |
|                            | logs. •	A log aggregator,       |
|                            | or similar automated tool,     |
|                            | provides an event log report   |
|                            | generation capability to aid   |
|                            | in detecting and assessing     |
|                            | anomalous activities on        |
|                            | business-critical systems.     |
| Well defined               | Continuous Monitoring (MON)    |
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
|                            | function: o	Governs asset       |
|                            | management that ensures        |
|                            | compliance with requirements   |
|                            | for asset management.          |
|                            | o	Leverages a Configuration     |
|                            | Management Database (CMDB),    |
|                            | or similar tool, as the        |
|                            | authoritative source of IT     |
|                            | assets. •	A Security Incident   |
|                            | Event Manager (SIEM), or       |
|                            | similar automated tool:        |
|                            | o	Centrally collects logs and   |
|                            | is protected according to      |
|                            | the manufacturer’s security    |
|                            | guidelines to protect the      |
|                            | integrity of the event logs    |
|                            | with cryptographic mechanisms. |
|                            | o	Monitors the organization for |
|                            | Indicators of Compromise (IoC) |
|                            | and provides 24x7x365 near     |
|                            | real-time alerting capability. |
|                            | o	Is configured to alert        |
|                            | incident response personnel    |
|                            | of detected suspicious events  |
|                            | such that incident responders  |
|                            | can look to terminate          |
|                            | suspicious events. •	Both       |
|                            | inbound and outbound network   |
|                            | traffic is monitored for       |
|                            | unauthorized activities to     |
|                            | identify prohibited activities |
|                            | and assist incident handlers   |
|                            | with identifying potentially   |
|                            | compromised systems.           |
| Quantitatively controllled | See SP-CMM3. SP-CMM4           |
|                            | is N/A, since a                |
|                            | quantitatively-controlled      |
|                            | process is not necessary       |
|                            | to review event logs on an     |
|                            | ongoing basis and escalate     |
|                            | incidents in accordance with   |
|                            | established timelines and      |
|                            | procedures.                    |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A,   |
|                            | since a continuously-improving |
|                            | process is not necessary       |
|                            | to review event logs on an     |
|                            | ongoing basis and escalate     |
|                            | incidents in accordance with   |
|                            | established timelines and      |
|                            | procedures.                    |
