# NET-12.2 - End-User Messaging Technologies
Mechanisms exist to prohibit the transmission of unprotected sensitive/regulated data by end-user messaging technologies. 
## Control questions
Does the organization prohibit the transmission of unprotected sensitive/regulated data by end-user messaging technologies? 
## Control maturity
### Not performed
There is no evidence of a capability to prohibit the transmission of unprotected sensitive/regulated data by end-user messaging technologies. 
### Performed internally
Network Security (NET) efforts are ad hoc and inconsistent. CMM Level 1 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	IT personnel use an informal process to design, build and maintain secure networks for test, development, staging and production environments, including the implementation of appropriate cybersecurity & data privacy controls.
•	Administrative processes are used to configure boundary devices (e.g., firewalls, routers, etc.) to deny network traffic by default and allow network traffic by exception (e.g., deny all, permit by exception). 
•	Network monitoring is primarily reactive in nature.
### Planned and tracked
Network Security (NET) efforts are requirements-driven and formally governed at a local/regional level, but are not consistent across the organization. CMM Level 2 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	Network security management is decentralized (e.g., a localized/regionalized function) and uses non-standardized methods to implement secure and compliant practices.
•	IT/cybersecurity personnel identify cybersecurity & data privacy controls that are appropriate to address applicable statutory, regulatory and contractual requirements for network security management.
•	IT personnel define secure networking practices to protect the confidentiality, integrity, availability and safety of the organization’s technology assets, data and network(s).
•	Administrative processes and technologies focus on protecting High Value Assets (HVAs), including environments where sensitive/regulated data is stored, transmitted and processed.
•	Administrative processes are used to configure boundary devices (e.g., firewalls, routers, etc.) to deny network traffic by default and allow network traffic by exception (e.g., deny all, permit by exception). 
•	Network segmentation exists to implement separate network addresses (e.g., different subnets) to connect systems in different security domains (e.g., sensitive/regulated data environments).
### Well defined
Network Security (NET) efforts are standardized across the organization and centrally managed, where technically feasible, to ensure consistency. CMM Level 3 control maturity would reasonably expect all, or at least most, the following criteria to exist:
•	A Technology Infrastructure team, or similar function, defines centrally-managed network security controls for implementation across the enterprise.
•	IT/cybersecurity architects work with the Technology Infrastructure team to implement a “layered defense” network architecture that provides a defense-in-depth approach for redundancy and risk reduction for network-based security controls, including wired and wireless networking.
•	Administrative processes and technologies configure boundary devices (e.g., firewalls, routers, etc.) to deny network traffic by default and allow network traffic by exception (e.g., deny all, permit by exception).
•	Technologies automate the Access Control Lists (ACLs) and similar rulesets review process to identify security issues and/ or misconfigurations. 
•	Network segmentation exists to implement separate network addresses (e.g., different subnets) to connect systems in different security domains (e.g., sensitive/regulated data environments).
### Quantitatively controllled
See SP-CMM3. SP-CMM4 is N/A, since a quantitatively-controlled process is not necessary to prohibit the transmission of unprotected sensitive/regulated data by end-user messaging technologies. 
### Continuously improving
See SP-CMM4. SP-CMM5 is N/A, since a continuously-improving process is not necessary to prohibit the transmission of unprotected sensitive/regulated data by end-user messaging technologies. 
## Mapped framework controls
### SOC 2
- [CC6.71](../soc2/cc671.md)