# GraphGRC Document Structure

This document describes the standardized structure for all GRC documentation and how the backlink generation system works.

## Philosophy: Markdown-Native, GitHub Pages & Obsidian Compatible

All documentation is pure semantic markdown with YAML frontmatter. No custom syntax that breaks GitHub Pages or Obsidian rendering.

**Key principles:**
- Pure markdown with annotation-based links
- Automatic backlink generation for bidirectional navigation
- YAML frontmatter for structured metadata
- Compatible with GitHub Pages, Obsidian, and standard Markdown viewers

## Document Hierarchy and Link Direction

```
┌─────────────────────────────────────────┐
│     Framework Controls (SOC 2, GDPR)    │  ← Backlinks FROM custom controls
│     ## Referenced By (generated)         │
└─────────────────────────────────────────┘
                    ▲
                    │ Custom controls link UP
                    │ (## Framework Mapping)
┌─────────────────────────────────────────┐
│         Custom Controls (ACC-01, etc)    │  ← Backlinks FROM standards/processes
│         ## Framework Mapping (manual)    │
│         ## Referenced By (generated)     │
└─────────────────────────────────────────┘
                    ▲
                    │ Standards/processes link UP
                    │ (## Control Mapping)
┌─────────────────────────────────────────┐
│  Standards/Processes/Policies/Charter    │
│  ## Control Mapping (manual)             │
│  NO Referenced By section                │
└─────────────────────────────────────────┘
```

**Link Philosophy: "Arrows Point UP"**
- Standards/Processes/Policies/Charter → link UP to Custom Controls
- Custom Controls → link UP to Framework Controls
- Backlinks are automatically generated in the opposite direction

## Directory Structure

### `/custom/` - Custom Security Controls (26 controls)

Your organization's security controls mapped to SOC 2 and GDPR. Each control includes:
- YAML frontmatter with metadata
- Cross-references to implementing standards/processes/policies
- Framework mappings to SOC 2, GDPR, etc.
- Implementation guidance, examples, and audit evidence

**Categories:**
- **Access Control (ACC):** 4 controls - Authentication, RBAC, Access Reviews, Privileged Access
- **Data Protection (DAT):** 4 controls - Classification, Encryption, Retention, Privacy/GDPR
- **Endpoint Security (END):** 3 controls - MDM, Protection, Updates
- **Governance (GOV):** 2 controls - Policies, Risk Assessment
- **Infrastructure (INF):** 4 controls - Cloud Config, Network, Logging, Backup
- **Operations (OPS):** 4 controls - Change Mgmt, Vulnerability Mgmt, Incident Response, Business Continuity
- **People (PEO):** 3 controls - Background Checks, Training, Offboarding
- **Vendor (VEN):** 2 controls - Risk Assessment, Contracts/DPAs

### `/standards/` - Technical Security Standards

Technical requirements and best practices (9 standards):
1. AWS Security Standard
2. GitHub Security Standard
3. Data Classification Standard
4. Cryptography Standard
5. Vulnerability Management Standard
6. SaaS IAM Standard
7. Endpoint Security Standard
8. Logging & Monitoring Standard
9. Data Retention Standard

### `/processes/` - Security Processes

Step-by-step operational procedures (9 processes):
1. Access Provisioning Process
2. Access Review Process
3. Incident Response Process
4. Vulnerability Management Process
5. Vendor Risk Assessment Process
6. Change Management Process
7. Data Breach Response Process
8. Security Training Process
9. Backup & Recovery Process

### `/policies/` - Security Policies

Role-based security requirements (3 policies):
1. Baseline Security Policy (applies to all employees)
2. Engineering Security Policy (applies to engineers)
3. Data Access Policy (applies to roles with data access)

### `/charter/` - Strategic Governance

High-level strategic framework (2 documents):
1. Information Security Program Charter
2. Risk Management Strategy

### Generated Framework Docs

- `/soc2/` - SOC 2 control pages (auto-generated)
- `/gdpr/` - GDPR article pages (auto-generated)
- `/iso27001/`, `/iso27002/`, `/nist80053/`, `/scf/` - Other frameworks

## Document Types and Their Structure

### 1. Custom Controls (`custom/*.md`)

Custom controls are the core of the GRC program. They map UP to framework controls and receive backlinks DOWN from standards/processes/policies.

**Required sections:**
- YAML frontmatter (id, title, category, owner, last_reviewed, review_cadence)
- `## Objective` - What the control achieves
- `## Description` - What the control does
- `## Implementation Details` - How it's implemented
- `## Examples` - Real-world examples
- `## Audit Evidence` - What auditors look for
- `## Framework Mapping` - Links UP to framework controls (SOC 2, GDPR, etc.)
- `## Referenced By` - AUTO-GENERATED backlinks from standards/processes/policies

**Structure:**
```markdown
---
id: ACC-01
title: Identity & Authentication
category: Access Control
owner: it-team
last_reviewed: 2025-01-09
review_cadence: quarterly
---

# ACC-01: Identity & Authentication

## Objective
[What this control achieves]

## Description
[What this control does]

## Implementation Details
[How it's implemented]

## Examples
[Real-world examples]

## Audit Evidence
[What auditors look for]

---

## Framework Mapping

<!-- This section is used to generate backlinks from framework controls to this custom control. Do not remove. -->

### SOC 2
- [CC6.1](../soc2/cc61.md) - Description of how this control satisfies CC6.1
- [CC6.2](../soc2/cc62.md) - Description of how this control satisfies CC6.2

### GDPR
- [Article 32](../gdpr/art32.md) - Description of how this control satisfies Article 32

---

<!-- Backlinks auto-generated below -->
## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*
```

### 2. Standards (`standards/*.md`)

Standards define technical requirements and link DOWN to custom controls they satisfy.

**Required sections:**
- YAML frontmatter
- Main content (requirements, scope, etc.)
- `## Control Mapping` - Links DOWN to custom controls

**NO "Referenced By" section** - standards only link TO controls, not receive backlinks.

**Structure:**
```markdown
---
type: standard
title: AWS Security Standard
owner: infrastructure-team
last_reviewed: 2025-01-09
review_cadence: quarterly
---

# AWS Security Standard

[Content describing the standard]

---

## Control Mapping

<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->
<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->

- [ACC-01: Identity & Authentication](../custom/acc-01.md) ^[IAM Identity Center for cloud access]
- [INF-01: Cloud Security Configuration](../custom/inf-01.md) ^[VPC and Security Group requirements]
```

### 3. Processes (`processes/*.md`)

Processes define workflows and link DOWN to custom controls they implement.

Same structure as standards - has `## Control Mapping`, NO `## Referenced By`.

### 4. Policies (`policies/*.md`)

Policies define rules and link DOWN to custom controls they reference.

Same structure as standards - has `## Control Mapping`, NO `## Referenced By`.

### 5. Charter (`charter/*.md`)

Charter documents define program governance and link DOWN to relevant controls.

Same structure as standards - has `## Control Mapping`, NO `## Referenced By`.

### 6. Framework Controls (`soc2/*.md`, `gdpr/*.md`, etc.)

Framework controls receive backlinks FROM custom controls.

**Only has:**
- Main content (framework-specific control description)
- `## Referenced By` - AUTO-GENERATED backlinks from custom controls

**NO manual Control Mapping section** - these are referenced BY custom controls, not the other way around.

## Annotation Syntax

We use two link formats for different contexts:

### Format 1: Caret Annotation (Standards → Controls)

Used when standards/processes/policies link to custom controls:

```markdown
- [ACC-01: Identity & Authentication](../custom/acc-01.md) ^[IAM Identity Center for cloud access]
- [INF-01: Cloud Security Configuration](../custom/inf-01.md) ^[VPC and Security Group requirements]
```

**Pattern:** `[Link Text](path.md) ^[annotation explaining the relationship]`

### Format 2: Dash Separation (Controls → Frameworks)

Used when custom controls link to framework controls:

```markdown
### SOC 2
- [CC6.1](../soc2/cc61.md) - Strong authentication implements logical access controls
- [CC6.2](../soc2/cc62.md) - SSO with MFA ensures users are authorized before access

### GDPR
- [Article 32](../gdpr/art32.md) - MFA is a technical measure for security of processing
```

**Pattern:** `- [Control ID](path.md) - explanation of how this satisfies the requirement`

**Why Two Formats?**
- Both are pure markdown (no custom syntax)
- Both render correctly in GitHub Pages and Obsidian
- Caret format `^[...]` uses markdown footnote-style syntax
- Dash format is semantic and readable as a list with descriptions
- Easy to parse programmatically for backlink generation

## YAML Frontmatter Structure

### Control Frontmatter

```yaml
---
id: ACC-01
title: Identity & Authentication
category: Access Control
owner: it-team
last_reviewed: 2025-01-09
review_cadence: quarterly
---
```

**Required fields:** id, title, category, owner, last_reviewed, review_cadence

### Standard/Process/Policy/Charter Frontmatter

```yaml
---
type: standard  # or process, policy, charter
title: AWS Security Standard
owner: infrastructure-team
last_reviewed: 2025-01-09
review_cadence: quarterly
---
```

**Required fields:** type, title, owner, last_reviewed, review_cadence

## Link Format Details

### Manual Links (Forward Links)

- **Custom controls → Framework controls:** Use dash-separated format in `## Framework Mapping`
  ```markdown
  - [CC6.1](../soc2/cc61.md) - How this control satisfies CC6.1
  ```

- **Standards/Processes/Policies → Custom controls:** Use annotation format in `## Control Mapping`
  ```markdown
  - [ACC-01: Identity & Authentication](../custom/acc-01.md) ^[Specific requirement from this standard]
  ```

### Auto-Generated Links (Backlinks)

Generated by `make generate-backlinks` in `## Referenced By` sections. These are read-only and should not be edited manually.

## Backlink Generation System

The `make generate-backlinks` command automatically generates backlink sections showing what references what.

### Example Link Graph

```
ACC-01 (Custom Control)
  ├─> aws-security-standard.md ^[IAM Identity Center]
  ├─> saas-iam-standard.md ^[SSO and MFA]
  ├─> access-provisioning-process.md ^[MFA enrollment]
  ├─> soc2/cc6-1.md - [Strong authentication]
  └─> gdpr/article-32.md - [Technical measures]

aws-security-standard.md
  <─ ACC-01 ^[IAM Identity Center]
  <─ ACC-04 ^[Root account MFA]
  <─ INF-01 ^[Security Groups]
```

### Generated Backlink Section Example

In `custom/acc-01.md`, the generator appends:

```markdown
---

<!-- Backlinks auto-generated below -->
## Referenced By

*This section is automatically generated by `make generate-backlinks`. Do not edit manually.*

**Standards:**
- [AWS Security Standard](../standards/aws-security-standard.md) ^[IAM Identity Center for cloud access]

**Processes:**
- [Access Provisioning Process](../processes/access-provisioning-process.md) ^[MFA enrollment during account creation]
```

## Makefile Targets

### Core Commands

- `make help` - Show all available commands with descriptions
- `make validate-structure` - Validate all files have required sections
- `make clean-backlinks` - Remove all generated backlinks
- `make generate-backlinks` - Generate backlinks from forward links
- `make regenerate-backlinks` - Clean and regenerate all backlinks

### Framework Generation

- `make download-frameworks` - Download external framework data (SCF Excel, SOC2 JSON, GDPR markdown)
- `make generate-frameworks` - Generate framework control pages from downloaded data

### Validation

- `make validate` - Validate all markdown files (frontmatter, links, annotations, required fields)

### Full Workflow

```bash
make generate  # Run all generation commands in order
```

## Workflow

### Daily Development

1. Add forward links manually in `## Framework Mapping` (custom controls) or `## Control Mapping` (standards/processes/policies)
2. Run `make generate-backlinks`
3. Backlinks are automatically generated in `## Referenced By` sections
4. Run `make validate-structure` to ensure all files are properly structured

### Adding New Documents

1. Create markdown file with proper YAML frontmatter
2. Add required sections (`## Control Mapping` or `## Framework Mapping`)
3. Add manual links with annotations
4. Run `make regenerate-backlinks` to generate all backlinks
5. Verify with `make validate-structure`

## Framework Mapping Coverage

### SOC 2 Coverage

All major Trust Services Criteria are mapped:
- **CC1 (Control Environment):** CC1.1, CC1.2, CC1.4
- **CC2 (Communication):** CC2.1, CC2.2
- **CC3 (Risk Assessment):** CC3.1, CC3.2, CC3.4
- **CC6 (Logical Access):** CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC6.8
- **CC7 (System Operations):** CC7.1, CC7.2, CC7.3, CC7.4, CC7.5
- **CC8 (Change Management):** CC8.1
- **CC9 (Risk Mitigation):** CC9.1, CC9.2
- **A1 (Availability):** A1.1, A1.2, A1.3

### GDPR Coverage

Key GDPR articles are mapped:
- **Article 5:** Principles of data processing
- **Article 6:** Legal basis for processing
- **Article 15:** Right of access
- **Article 17:** Right to erasure
- **Article 20:** Right to data portability
- **Article 24:** Responsibility of the controller
- **Article 28:** Data Processing Agreements
- **Article 30:** Records of processing activities
- **Article 32:** Security of processing (most frequently mapped)
- **Article 33:** Breach notification to authority
- **Article 34:** Breach notification to data subjects

## Tool Compatibility

### Obsidian

- **YAML frontmatter:** Parsed and displayed in properties panel
- **Markdown links:** Work natively with `[[wikilinks]]` or `[text](path)`
- **Annotations:** `^[text]` renders as footnotes
- **Backlinks:** Obsidian auto-detects links, plus we generate explicit "Referenced By" sections
- **Graph view:** Visualizes the entire link graph automatically

### GitHub Pages

- **Jekyll:** Renders YAML frontmatter
- **Markdown links:** Work natively
- **Annotations:** Render as footnote references
- **Static site:** No JavaScript required
- **Relative paths:** Work in both local and deployed environments

### Standard Markdown Viewers

- All syntax is standard markdown
- YAML frontmatter is widely supported
- Links work in any markdown renderer
- No custom syntax or preprocessing required

## Usage Guides

### For Auditors

1. Start with [custom/index.md](custom/index.md) to see all controls
2. Click into a control (e.g., ACC-01) to see implementation details
3. Follow annotated links to standards/processes for detailed procedures
4. Review framework mappings with annotations explaining compliance coverage
5. Use backlinks to see what else references this document

### For Engineers

1. Check [standards/](standards/) for technical requirements
2. Check [processes/](processes/) for step-by-step procedures
3. Reference [policies/](policies/) for role-specific obligations
4. Use backlinks to see which controls depend on each standard
5. Run `make validate` to ensure changes don't break documentation

### For Leadership

1. Review [charter/](charter/) for strategic framework
2. Check [custom/index.md](custom/index.md) for control overview
3. Use framework mappings to understand compliance coverage
4. Run `make validate` to ensure all documentation is complete
5. Review backlinks to understand control dependencies

## Benefits

- **Pure markdown:** No custom syntax, works everywhere
- **Context-aware:** Annotations explain why links exist
- **Bidirectional:** Automatic backlinks show dependencies
- **Maintainable:** Manual edits to controls, automatic backlinks
- **Auditable:** Clear evidence trail with annotations
- **Tool-agnostic:** Works in any markdown viewer
- **Version control friendly:** Git diffs are meaningful
- **Semantic:** Structure matches logical relationships
- **Scalable:** Easy to add new controls, standards, or frameworks

## Technical Implementation

### File Organization

```
graphgrc/
├── Makefile                          # Build commands
├── main.go                           # CLI entry point
├── cmd/
│   ├── validate-structure/main.go   # Structure validation
│   └── generate-backlinks/main.go   # Backlink generation
├── internal/
│   ├── parser/
│   │   ├── links.go                 # Parse annotated links
│   │   └── backlinks.go             # Generate backlinks
│   ├── scf.go                       # SCF framework parsing
│   ├── soc2.go                      # SOC2 parsing
│   └── gdpr.go                      # GDPR parsing
├── scripts/
│   ├── standardize-structure.py     # Bulk structure updates
│   └── clean-backlinks.py           # Clean backlink sections
├── custom/                           # Custom controls (manual)
├── standards/                        # Standards (manual)
├── processes/                        # Processes (manual)
├── policies/                         # Policies (manual)
├── charter/                          # Charter (manual)
└── [soc2, gdpr, iso27001, etc.]/    # Generated framework pages
```

### Key Implementation Files

#### `internal/parser/links.go`
- Parses both `^[annotation]` and dash-separated link formats
- Skips `## Referenced By` and `## Framework Mapping` sections to avoid circular references
- Processes `## Control Mapping` sections in standards/processes/policies
- Extracts source file titles from YAML frontmatter
- Returns `AnnotatedLink` structures with source, target, annotation, and line number

#### `cmd/validate-structure/main.go`
- Validates custom controls have `## Framework Mapping` and `## Referenced By`
- Validates standards/processes/policies/charter have `## Control Mapping`
- Validates YAML frontmatter exists and has required fields
- Skips `index.md` files automatically
- Returns detailed validation results with line-by-line issues

#### `scripts/standardize-structure.py`
- Bulk operation to standardize all document structures
- Renames sections consistently across all files
- Fixes formatting (e.g., `**SOC 2:**` → `### SOC 2`)
- Adds missing sections with proper comments

## Troubleshooting

### Links not generating backlinks

1. Check link format - must match `^[annotation]` or dash-separated pattern
2. Verify the target file exists
3. Ensure links are not in `## Referenced By` or `## Framework Mapping` sections
4. Run `make validate-structure` to check for missing sections

### Validation errors

1. Check YAML frontmatter is present and properly formatted
2. Verify required fields are present (id/title, category/type, owner)
3. Ensure `## Framework Mapping` exists in custom controls
4. Ensure `## Control Mapping` exists in standards/processes/policies

### Circular references

1. The parser automatically skips sections that could create circular references
2. Custom controls skip `## Framework Mapping` when parsing
3. All documents skip `## Referenced By` when parsing
4. This prevents infinite loops in backlink generation

---

**This document is maintained as part of the GraphGRC project. When making significant changes to the codebase or documentation structure, please update this file to keep it accurate.**
