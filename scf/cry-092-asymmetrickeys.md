# CRY-09.2 - Asymmetric Keys
Mechanisms exist to facilitate the production and management of asymmetric cryptographic keys using Federal Information Processing Standards (FIPS)-compliant key management technology and processes that protect the user’s private key. 
## Mapped framework controls
### SOC 2
- [CC6.1](../soc2/cc61.md)
## Control questions
Does the organization facilitate the production and management of asymmetric cryptographic keys using Federal Information Processing Standards (FIPS)-compliant key management technology and processes that protect the user’s private key? 
## Control maturity
|       MATURITY LEVEL       |          DESCRIPTION           |
|----------------------------|--------------------------------|
| Not performed              | There is no evidence of a      |
|                            | capability to facilitate the   |
|                            | production and management of   |
|                            | asymmetric cryptographic keys  |
|                            | using Federal Information      |
|                            | Processing Standards           |
|                            | (FIPS)-compliant key           |
|                            | management technology and      |
|                            | processes that protect the     |
|                            | user’s private key.            |
| Performed internally       | SP-CMM1 is N/A, since a        |
|                            | structured process is required |
|                            | to facilitate the production   |
|                            | and management of asymmetric   |
|                            | cryptographic keys using       |
|                            | Federal Information Processing |
|                            | Standards (FIPS)-compliant     |
|                            | key management technology and  |
|                            | processes that protect the     |
|                            | user’s private key.            |
| Planned and tracked        | Cryptographic Protections      |
|                            | (CRY) efforts are              |
|                            | requirements-driven and        |
|                            | formally governed at a         |
|                            | local/regional level, but      |
|                            | are not consistent across      |
|                            | the organization. CMM          |
|                            | Level 2 control maturity       |
|                            | would reasonably expect        |
|                            | all, or at least most, the     |
|                            | following criteria to exist:   |
|                            | •	Cryptographic management      |
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
|                            | contractual requirements for   |
|                            | cryptographic management.      |
|                            | •	Data classification and       |
|                            | handling criteria govern       |
|                            | requirements to encrypt        |
|                            | sensitive/regulated data       |
|                            | during transmission and        |
|                            | in storage. •	Decentralized     |
|                            | technologies implement         |
|                            | cryptographic mechanisms       |
|                            | on endpoints to control how    |
|                            | sensitive/regulated data is    |
|                            | encrypted during transmission  |
|                            | and in storage. •	Systems,      |
|                            | applications and services that |
|                            | store, process or transmit     |
|                            | sensitive/regulated data       |
|                            | use cryptographic mechanisms   |
|                            | to prevent unauthorized        |
|                            | disclosure of information      |
|                            | as an alternate to physical    |
|                            | safeguards. •	The IT department |
|                            | implements Public Key          |
|                            | Infrastructure (PKI) key       |
|                            | management controls to protect |
|                            | the confidentiality, integrity |
|                            | and availability of keys.      |
|                            | •	The IT department implements  |
|                            | and maintains an internal      |
|                            | PKI infrastructure or obtains  |
|                            | PKI services from a reputable  |
|                            | PKI service provider.  •	The    |
|                            | PKI infrastructure enables     |
|                            | the secure distribution of     |
|                            | symmetric and asymmetric       |
|                            | cryptographic keys using       |
|                            | industry recognized key        |
|                            | management technology          |
|                            | and processes.  •	The PKI       |
|                            | infrastructure ensures the     |
|                            | availability of information    |
|                            | in the event of the loss       |
|                            | of cryptographic keys by       |
|                            | individual users.  •	The        |
|                            | PKI infrastructure enables     |
|                            | the secure distribution of     |
|                            | symmetric and asymmetric       |
|                            | cryptographic keys using       |
|                            | industry recognized key        |
|                            | management technology          |
|                            | and processes.  •	The PKI       |
|                            | management function enables    |
|                            | the implementation of          |
|                            | cryptographic key management   |
|                            | controls to protect the        |
|                            | confidentiality, integrity and |
|                            | availability of keys.          |
| Well defined               | Cryptographic Protections      |
|                            | (CRY) efforts are standardized |
|                            | across the organization and    |
|                            | centrally managed, where       |
|                            | technically feasible, to       |
|                            | ensure consistency. CMM Level  |
|                            | 3 control maturity would       |
|                            | reasonably expect all, or      |
|                            | at least most, the following   |
|                            | criteria to exist: •	Data       |
|                            | classification and handling    |
|                            | criteria govern requirements   |
|                            | to encrypt sensitive/regulated |
|                            | data during transmission and   |
|                            | in storage. •	Centrally-managed |
|                            | technologies implement         |
|                            | cryptographic mechanisms       |
|                            | on endpoints to control how    |
|                            | sensitive/regulated data is    |
|                            | encrypted during transmission  |
|                            | and in storage. •	Systems,      |
|                            | applications and services that |
|                            | store, process or transmit     |
|                            | sensitive/regulated data       |
|                            | use cryptographic mechanisms   |
|                            | to prevent unauthorized        |
|                            | disclosure of information      |
|                            | as an alternate to physical    |
|                            | safeguards. •	The Public        |
|                            | Key Infrastructure (PKI)       |
|                            | management function enables    |
|                            | the implementation of          |
|                            | cryptographic key management   |
|                            | controls to protect the        |
|                            | confidentiality, integrity     |
|                            | and availability of keys. •	The |
|                            | PKI infrastructure enables     |
|                            | the secure distribution of     |
|                            | symmetric and asymmetric       |
|                            | cryptographic keys using       |
|                            | industry recognized key        |
|                            | management technology          |
|                            | and processes.  •	The PKI       |
|                            | infrastructure ensures the     |
|                            | availability of information    |
|                            | in the event of the loss       |
|                            | of cryptographic keys by       |
|                            | individual users.  •	An IT      |
|                            | infrastructure team, or        |
|                            | similar function, enables:     |
|                            | o	The production and management |
|                            | of asymmetric cryptographic    |
|                            | keys using approved key        |
|                            | management technology and      |
|                            | processes that protect the     |
|                            | user’s private key.  o	The      |
|                            | production and management of   |
|                            | symmetric cryptographic keys   |
|                            | using approved key management  |
|                            | technology and processes that  |
|                            | protect the user’s private     |
|                            | key.                           |
| Quantitatively controllled | See SP-CMM3. SP-CMM4           |
|                            | is N/A, since a                |
|                            | quantitatively-controlled      |
|                            | process is not necessary to    |
|                            | facilitate the production      |
|                            | and management of asymmetric   |
|                            | cryptographic keys using       |
|                            | Federal Information Processing |
|                            | Standards (FIPS)-compliant     |
|                            | key management technology and  |
|                            | processes that protect the     |
|                            | user’s private key.            |
| Continuously improving     | See SP-CMM4. SP-CMM5 is N/A,   |
|                            | since a continuously-improving |
|                            | process is not necessary to    |
|                            | facilitate the production      |
|                            | and management of asymmetric   |
|                            | cryptographic keys using       |
|                            | Federal Information Processing |
|                            | Standards (FIPS)-compliant     |
|                            | key management technology and  |
|                            | processes that protect the     |
|                            | user’s private key.            |
