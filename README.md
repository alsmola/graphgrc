# GraphGRC

**AI-generated security controls with automated compliance traceability**

GraphGRC provides 76 custom security controls with direct mappings to compliance frameworks (SOC 2, GDPR, ISO 27001, NIST 800-53). Each control includes detailed implementation guidance, evidence requirements, and bidirectional links showing which standards/policies/processes implement it.

## Published Documentation

Browse the live documentation at **[engseclabs.github.io/graphgrc/](https://engseclabs.github.io/graphgrc/)**

## What's Included

### Complete GRC Documentation (1,136 files)

| Category | Count | Description |
|----------|-------|-------------|
| **Controls** | 76 | Detailed security controls organized by 25 families (IAM, cryptography, incident response, etc.) |
| **Standards** | 10 | Technical security standards (AWS security, cryptography, data classification, etc.) |
| **Policies** | 6 | Role-specific security policies (employee, engineer, HR, IT, product, security team) |
| **Processes** | 23 | Operational procedures (incident response, audits, access reviews, etc.) |
| **Charter** | 4 | Governance and risk management foundation |
| **Frameworks** | 1,004 | Generated framework mappings (SCF, SOC 2, GDPR, ISO 27001/27002, NIST 800-53) |

### Control Families

**76 controls** across 25 families covering comprehensive security domains:

- **Asset Management** - Cloud, endpoint, and SaaS inventory
- **Availability** - Monitoring, capacity planning, disaster recovery
- **Compliance** - Contract management, audits, GRC function
- **Configuration Management** - Cloud, endpoint, and SaaS hardening
- **Cryptography** - Encryption, key management, code signing
- **Data Management** - Data inventory, retention, classification
- **Data Privacy** - Customer and employee personal data protection
- **IAM** - Cloud IAM, MFA, SSO, password management, secrets
- **Incident Response** - Security incidents, data breaches, exercises
- **Monitoring** - Endpoint, infrastructure, and SIEM
- **Network Security** - Cloud and endpoint network protection
- **Personnel Security** - Lifecycle, insider threats, rules of behavior
- **Physical Protection** - Office security
- **Risk Management** - Organizational risk assessment, vendor risk
- **Security Assurance** - Penetration testing, bug bounty, security reviews
- **Security Engineering** - Code analysis, secure coding, code review
- **Security Training** - Awareness, incident response, secure coding training
- **Threat Detection** - Cloud, endpoint, and SaaS threat detection
- **Vulnerability Management** - Detection and remediation processes

## Architecture

GraphGRC provides a **custom control framework** with direct mappings to compliance frameworks:

```
┌──────────────────────────────────────────────┐
│         Custom Security Controls (76)        │
│   IAM, Cryptography, Data Privacy, etc.      │
│                                              │
│  Each control defines:                       │
│  - Objective & Implementation                │
│  - Framework Mappings (SOC 2, GDPR, etc.)   │
│  - Evidence requirements                     │
└──────────────┬────────────┬──────────────────┘
               │            │
       ┌───────┘            └────────┐
       ▼                              ▼
┌─────────────────┐          ┌──────────────────┐
│   Frameworks    │          │  Implementation  │
│  SOC 2, GDPR,   │◄────────►│   Documents      │
│  ISO, NIST      │          │                  │
│                 │          │ - Standards (10) │
│ "Referenced By" │          │ - Policies (6)   │
│   backlinks     │          │ - Processes (23) │
└─────────────────┘          │ - Charter (4)    │
                             │                  │
                             │ "Implemented By" │
                             │    backlinks     │
                             └──────────────────┘
```

**Key features:**
- **AI-Generated Controls:** 76 custom security controls with detailed implementation guidance
- **Direct Framework Mapping:** Each control explicitly maps to SOC 2, GDPR, ISO 27001, NIST 800-53 requirements
- **Bidirectional Traceability:** Auto-generated backlinks showing:
  - **Controls → Frameworks:** Which compliance requirements each control satisfies
  - **Controls → Implementation:** Which standards/policies/processes implement each control
  - **Frameworks → Controls:** Which controls satisfy each framework requirement
- **Information Dense:** Specific, concrete controls (e.g., "Cloud IAM", "MFA") instead of vague umbrella terms
- **Automated Maintenance:** Scripts automatically regenerate backlinks and validate documentation structure

## Quick Start

### Regenerate Backlinks

After modifying control mappings in standards, policies, or processes:

```bash
# Rebuild the backlink generator
cd src/cmd/generate-backlinks && go build -o ../../../bin/generate-backlinks .

# Generate backlinks
cd ../../..
./bin/generate-backlinks -root=docs -verbose
```

### Validate Links

Check for broken links in documentation:

```bash
# Build validator
cd src/cmd/validate-links && go build -o ../../../bin/validate-links .

# Run validation
cd ../../..
./bin/validate-links docs/
```

## Project Structure

```
graphgrc/
├── bin/                           # Compiled binaries
│   ├── generate-backlinks        # Backlink generator
│   ├── validate-links            # Link validator
│   └── fix-links                 # Link fixer
│
├── src/
│   ├── cmd/                      # Go tools
│   │   ├── generate-backlinks/  # Backlink generation tool
│   │   ├── validate-links/      # Link validation tool
│   │   └── fix-links/           # Link fixing tool
│   └── scripts/                  # Python automation scripts
│       ├── consolidate-*.py     # Control consolidation scripts
│       ├── remove-*.py          # Control removal scripts
│       └── move-*.py            # Control reorganization scripts
│
├── docs/                         # Documentation (hand-crafted + auto-generated backlinks)
│   ├── charter/                 # Governance & risk management (4 docs)
│   ├── controls/                # Security controls (76 custom controls)
│   ├── frameworks/              # Framework requirement pages (SOC 2, GDPR, ISO, NIST)
│   ├── policies/                # Role-specific policies (6 policies)
│   ├── processes/               # Operational processes (23 processes)
│   ├── standards/               # Technical standards (10 standards)
│   └── index.md                 # Documentation home
│
└── README.md                     # This file
```

## Customization

### Adding New Controls

1. Create new markdown file in appropriate `docs/controls/{family}/` directory
2. Use existing controls as templates (include frontmatter, Framework Mapping, Implemented By sections)
3. Add framework mappings in the "Framework Mapping" section
4. Reference the control from relevant standards/policies/processes via "Control Mapping" sections
5. Regenerate backlinks: `./bin/generate-backlinks -root=docs -verbose`

### Modifying Framework Mappings

Framework mappings are defined in each control's "Framework Mapping" section:

```markdown
## Framework Mapping

### SOC 2
- [CC6.1](../../frameworks/soc2/cc61.md) ^[How this control satisfies CC6.1]
- [CC6.2](../../frameworks/soc2/cc62.md) ^[How this control satisfies CC6.2]

### GDPR
- [Article 32](../../frameworks/gdpr/art32.md) ^[How this control satisfies Article 32]
```

After modifying, regenerate backlinks to update framework "Referenced By" sections.

## Documentation Quality

All documentation includes:

- **Frontmatter metadata:** Type, title, owner, review dates, IDs
- **Consistent structure:** Standardized headings and sections
- **Comprehensive cross-references:** 200+ links between controls, standards, policies, and processes
- **Auto-generated backlinks:** 114+ "Referenced By" sections showing document relationships
- **Evidence guidance:** Specific audit evidence examples
- **Implementation details:** Practical guidance with real tools (AWS KMS, Okta, CrowdStrike, etc.)

**Quality metrics:**
- ✅ 100% controls filled (0 templates)
- ✅ 100% controls have framework mappings (76/76)
- ✅ **100% controls have implementation backlinks (76/76)**
- ✅ 100% standards have control mappings (10/10)
- ✅ All standards have unique IDs
- ✅ All control references point to correct locations
- ✅ Bidirectional links auto-generated and maintained
- ✅ Consistent frontmatter across all document types

**Interlinking structure:**
- **Controls → Frameworks:** Each control links to framework requirements it satisfies (SOC 2, GDPR, ISO, NIST)
- **Frameworks → Controls:** "Referenced By" sections show which controls satisfy each requirement
- **Standards/Policies/Processes → Controls:** "Control Mapping" sections with annotated links (551 total)
- **Controls → Implementation Docs:** "Implemented By" sections auto-generated from Control Mappings

## Development

### Prerequisites

- Go 1.21+ (for backlink generator and link validation tools)
- Python 3.x (for automation scripts)

### Workflow

```bash
# 1. Modify controls, standards, policies, or processes
vim docs/controls/iam/cloud-iam.md

# 2. Rebuild backlink generator (if code changed)
cd src/cmd/generate-backlinks && go build -o ../../../bin/generate-backlinks .

# 3. Regenerate backlinks
cd ../../..
./bin/generate-backlinks -root=docs -verbose

# 4. Validate links
./bin/validate-links docs/
```

## Customizing for Your Organization

This provides a **reference implementation** with 76 AI-generated controls. To adapt:

1. **Review Control Content** - Validate implementations match your actual practices
2. **Update Tool References** - Change AWS/Okta/etc. to your specific tools
3. **Adjust SLAs** - Update remediation timeframes (e.g., Critical: 7 days → your SLA)
4. **Modify Framework Mappings** - Add/remove framework links based on your compliance needs
5. **Customize Evidence** - Tailor evidence examples to your audit processes
6. **Add/Remove Controls** - Create new controls or remove ones you don't need

## Use Cases

- **SOC 2 Preparation:** Map your controls to SOC 2 Trust Service Criteria
- **Multi-Framework Compliance:** Demonstrate how one control satisfies multiple frameworks
- **Control Documentation:** Generate comprehensive control documentation with evidence
- **Gap Analysis:** Identify controls needed for specific frameworks
- **Audit Support:** Provide auditors with detailed control descriptions and mappings

## Organization Profile

The default configuration assumes:
- **Cloud:** AWS-native SaaS application
- **Team Size:** ~100 people
- **Endpoints:** macOS laptops managed via MDM (Jamf)
- **Infrastructure:** No physical datacenters, cloud-native architecture
- **Security Practices:** WebAuthn MFA, full disk encryption, SSO (Okta/Google Workspace)

Customize [control content](docs/controls/) to match your environment.

## License

MIT

## Documentation

- **[CLAUDE.md](CLAUDE.md)** - Comprehensive AI assistant guide for working on the codebase
- Project summaries available in root directory for historical context

## Links

- **Published Site:** https://engseclabs.github.io/graphgrc/
- **Repository:** https://github.com/engseclabs/graphgrc/
- **SCF Official:** https://securecontrolsframework.com/

---

**Status:** Production-ready, audit-ready documentation with 100% complete controls
