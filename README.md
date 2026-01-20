# GraphGRC

**Data-driven GRC documentation with automated framework mappings**

GraphGRC generates comprehensive, interconnected security and compliance documentation by mapping controls across multiple frameworks (SOC 2, GDPR, ISO 27001, NIST 800-53) using the Secure Controls Framework (SCF) as a unified reference model.

## Published Documentation

Browse the live documentation at **[engseclabs.github.io/graphgrc/](https://engseclabs.github.io/graphgrc/)**

## What's Included

### Complete GRC Documentation (1,136 files)

| Category | Count | Description |
|----------|-------|-------------|
| **Controls** | 86 | Detailed security controls organized by family (IAM, cryptography, incident response, etc.) |
| **Standards** | 10 | Technical security standards (AWS security, cryptography, data classification, etc.) |
| **Policies** | 9 | Security policies for different roles and functions |
| **Processes** | 23 | Operational procedures (incident response, audits, access reviews, etc.) |
| **Charter** | 4 | Governance and risk management foundation |
| **Frameworks** | 1,004 | Generated framework mappings (SCF, SOC 2, GDPR, ISO 27001/27002, NIST 800-53) |

### Control Families

**86 controls** covering comprehensive security domains:

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

GraphGRC uses a **hub-and-spoke** architecture with SCF as the central mapping layer:

```
┌─────────────────────────────────────────┐
│          External Data Sources          │
│  (SCF Excel, Framework JSON/Markdown)   │
└────────────────┬────────────────────────┘
                 │ EXTRACT
                 ▼
┌─────────────────────────────────────────┐
│         Transform & Normalize           │
│    (Parse Excel/JSON/MD → Go structs)   │
└────────────────┬────────────────────────┘
                 │ TRANSFORM
                 ▼
┌─────────────────────────────────────────┐
│          SCF Mapping Engine             │
│    (Create bidirectional mappings)      │
└────────────────┬────────────────────────┘
                 │ MAP
                 ▼
┌─────────────────────────────────────────┐
│       Markdown Generation               │
│  (1000+ interconnected .md files)       │
└────────────────┬────────────────────────┘
                 │ GENERATE
                 ▼
┌─────────────────────────────────────────┐
│         GitHub Pages Deploy             │
│      (Static site hosting)              │
└─────────────────────────────────────────┘
```

**Key features:**
- **Semantic:** Framework requirements parsed, structured, and rendered as navigable Markdown
- **Linked:** Bidirectional mappings show how controls satisfy multiple framework requirements
- **Comprehensive:** 86 controls with detailed objectives, implementation guidance, and evidence
- **Automated:** Scripts for link fixing, ID generation, and content standardization

## Quick Start

### Generate Documentation

```bash
# Generate all framework documentation
cd src && make generate

# Or run directly with Go
go run main.go

# Fetch fresh framework data (default uses cached data)
go run main.go -fetch
```

### Makefile Targets

```bash
# Generate framework documentation from cached data
make generate-frameworks

# Download fresh framework data
make download-frameworks

# Regenerate backlinks between documents
make generate-backlinks

# Clean and regenerate everything
make regenerate

# Validate all markdown links
make validate-links

# Watch for changes and auto-regenerate
make watch
```

## Project Structure

```
graphgrc/
├── src/
│   ├── main.go                    # Entry point - orchestrates pipeline
│   ├── internal/                  # Core processing logic
│   │   ├── scf.go                # SCF Excel parsing & mapping engine
│   │   ├── soc2.go               # SOC 2 JSON processing
│   │   ├── gdpr.go               # GDPR Markdown parsing
│   │   ├── iso.go                # ISO 27001/27002 JSON processing
│   │   ├── nist80053.go          # NIST 800-53 OSCAL JSON processing
│   │   └── constants.go          # Standardized heading constants
│   ├── scripts/                   # Automation scripts
│   │   ├── fix-standard-links.py # Fix control reference links
│   │   ├── add-standard-ids.py   # Add IDs to frontmatter
│   │   └── fill-template-controls.py # Generate control content
│   └── Makefile                   # Build automation
│
├── data/                          # Cached framework data
│   ├── scf.xlsx                  # SCF 2023.4 controls (4.6MB)
│   └── *.json                    # Cached framework data (6 files)
│
├── docs/                          # Generated documentation
│   ├── charter/                  # Governance documents (4)
│   ├── controls/                 # Security controls (86)
│   ├── frameworks/               # Framework mappings (1,004)
│   ├── policies/                 # Security policies (9)
│   ├── processes/                # Operational processes (23)
│   └── standards/                # Technical standards (10)
│
└── README.md                      # This file
```

## Customization

### Enabling/Disabling Frameworks

Edit `src/internal/scf.go` and modify the `SupportedFrameworks` map:

```go
var SupportedFrameworks = map[Framework]ControlHeader{
    "SOC 2":       "AICPA TSC 2017 (Controls)",
    "GDPR":        "EMEA EU GDPR",
    "ISO 27001":   "ISO 27001 v2022",
    "ISO 27002":   "ISO 27002 v2022",
    "NIST 800-53": "NIST 800-53 rev5 (moderate)",
    // "ISO 27701":   "ISO 27701 v2019",  // Available but disabled
    // "HIPAA":       "US HIPAA",          // Available but disabled
}
```

### Adding New Frameworks

1. Add framework to `SupportedFrameworks` map in `src/internal/scf.go`
2. Create new processor file `src/internal/newframework.go`
3. Implement parsing, markdown generation, and index creation
4. Add to pipeline in `src/main.go`

See [CLAUDE.md](CLAUDE.md) for detailed development guide.

### Updating SCF Version

1. Download new SCF Excel file from [securecontrolsframework.com](https://securecontrolsframework.com/)
2. Replace `data/scf.xlsx`
3. Run `make regenerate`

## Link Validation

Validate and fix broken links:

```bash
# Validate all markdown links
make validate-links

# Build link validator
make build-validator

# Run validator directly
./bin/validate-links docs/
```

## Documentation Quality

All documentation includes:

- **Frontmatter metadata:** Type, title, owner, review dates, IDs
- **Consistent structure:** Standardized headings and sections
- **Cross-references:** 114+ backlinks between related documents
- **Evidence guidance:** Specific audit evidence examples
- **Implementation details:** Practical guidance with real tools (AWS KMS, Okta, CrowdStrike, etc.)

**Quality metrics:**
- ✅ 100% controls filled (0 templates)
- ✅ All standards have unique IDs
- ✅ All control references point to correct locations
- ✅ Bidirectional links maintained
- ✅ Consistent frontmatter across all document types

## Data Sources

| Framework | Format | Source |
|-----------|--------|--------|
| SCF | Excel (XLSX) | https://securecontrolsframework.com/ |
| SOC 2 | JSON | Prowler cloud (prowler-cloud/prowler) |
| GDPR | Markdown | EnterpriseReady |
| ISO 27001/27002 | JSON | JupiterOne security-policy-templates |
| NIST 800-53 | JSON (OSCAL) | GSA FedRAMP automation |

## Development

### Prerequisites

- Go 1.21+
- Python 3.x (for automation scripts)
- Make

### Key Dependencies

```go
require (
    github.com/xuri/excelize/v2  // Excel file parsing for SCF
    github.com/go-spectest/markdown  // Markdown generation
)
```

### Running Tests

```bash
# Validate generated documentation
make validate-links

# Regenerate all documentation
make regenerate

# Check for broken links
make validate-links | grep "broken"
```

## Contributing

This project provides a reference implementation for GRC documentation. To adapt for your organization:

1. **Review AI-generated content** - Validate control implementations match your practices
2. **Customize tools** - Update tool references (AWS, Okta, etc.) to match your stack
3. **Adjust SLAs** - Update remediation timeframes to match your standards
4. **Add framework mappings** - Link controls to specific compliance requirements
5. **Update evidence** - Tailor evidence examples to your audit processes

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
- **[DOCUMENTATION_AUDIT_RESULTS.md](DOCUMENTATION_AUDIT_RESULTS.md)** - Detailed audit findings and fixes
- **[DOCUMENTATION_STANDARDIZATION_COMPLETE.md](DOCUMENTATION_STANDARDIZATION_COMPLETE.md)** - Standardization summary

## Links

- **Published Site:** https://engseclabs.github.io/graphgrc/
- **Repository:** https://github.com/engseclabs/graphgrc/
- **SCF Official:** https://securecontrolsframework.com/

---

**Status:** Production-ready, audit-ready documentation with 100% complete controls
