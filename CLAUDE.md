# CLAUDE.md - AI Engineering Guide for GraphGRC

> This file provides comprehensive context for AI assistants (Claude, ChatGPT, etc.) working on the GraphGRC codebase. It enables effective collaboration without repeated explanations.

## Project Overview

**GraphGRC** is a Go-based documentation generator that creates interconnected Markdown documentation for GRC (Governance, Risk, and Compliance) programs. It maps controls across multiple compliance frameworks using the Secure Controls Framework (SCF) as a unified reference model.

- **Language:** Go 1.21
- **Repository:** https://github.com/engseclabs/graphgrc/
- **Published Site:** https://engseclabs.github.io/graphgrc/
- **License:** MIT

### What Problem Does This Solve?

Organizations implementing security programs must comply with multiple frameworks simultaneously (SOC 2, ISO 27001, GDPR, NIST 800-53). Each framework has hundreds of controls with significant overlap. GraphGRC:

1. **Maps relationships** between similar controls across frameworks
2. **Creates navigable documentation** showing how one security control can satisfy multiple framework requirements
3. **Reduces complexity** by using SCF as a single unified control set that maps to all frameworks

## Architecture

### Design Pattern: Hub-and-Spoke ETL Pipeline

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

### Hub-and-Spoke Model

- **Hub:** SCF (576 controls in 30 families)
- **Spokes:** SOC 2, GDPR, ISO 27001, ISO 27002, NIST 800-53
- **Linking:** Bidirectional - frameworks → SCF → frameworks

### Data Flow

1. **Extract:** Download framework data from external URLs (or use cached JSON)
2. **Transform:** Parse diverse formats (Excel, JSON, Markdown) into normalized Go structures
3. **Map:** Create cross-references using SCF as the mapping layer
4. **Generate:** Produce 1000+ Markdown files with bidirectional hyperlinks
5. **Deploy:** Publish via GitHub Actions to GitHub Pages

## Codebase Structure

```
graphgrc/
├── main.go                        # Entry point - orchestrates entire pipeline
├── go.mod                         # Go module definition
├── go.sum                         # Dependency checksums
│
├── internal/                      # Core processing logic
│   ├── scf.go                    # SCF Excel parsing & core mapping engine (326 LOC)
│   ├── soc2.go                   # SOC 2 JSON processing (159 LOC)
│   ├── gdpr.go                   # GDPR Markdown parsing (178 LOC)
│   ├── iso.go                    # ISO 27001/27002 JSON processing (157 LOC)
│   ├── nist80053.go              # NIST 800-53 OSCAL JSON processing (305 LOC)
│   └── file.go                   # Filename sanitization utilities (12 LOC)
│
├── scf.xlsx                       # SCF 2023.4 controls (4.6MB Excel file)
├── *.json                         # Cached framework data (6 files)
│
├── scf/                           # Generated SCF docs (576 files)
│   └── index.md                  # SCF control family index
├── soc2/                          # Generated SOC 2 docs (59 files)
├── gdpr/                          # Generated GDPR docs (55 files)
├── iso27001/                      # Generated ISO 27001 docs (10 files)
├── iso27002/                      # Generated ISO 27002 docs (7 files)
├── nist80053/                     # Generated NIST 800-53 docs (326 files)
│
├── .github/workflows/             # CI/CD
│   └── publish.yml               # GitHub Pages deployment
│
├── README.md                      # User documentation
└── CLAUDE.md                      # This file - AI engineering guide
```

**Total Generated Output:** 1,033 Markdown files, ~44MB

## Key Technologies & Dependencies

### Core Dependencies

```go
require (
    github.com/xuri/excelize/v2  // Excel file parsing for SCF
    github.com/go-spectest/markdown  // Markdown generation (forked version)
)
```

### External Data Sources

| Framework | Format | Source |
|-----------|--------|--------|
| SCF | Excel (XLSX) | https://securecontrolsframework.com/ |
| SOC 2 | JSON | Prowler cloud (prowler-cloud/prowler) |
| GDPR | Markdown | EnterpriseReady |
| ISO 27001/27002 | JSON | JupiterOne security-policy-templates |
| NIST 800-53 | JSON (OSCAL) | GSA FedRAMP automation |

## Core Data Structures

### Type System

```go
// Framework identifier (e.g., "SOC 2", "GDPR", "ISO 27001")
type Framework string

// Column header from framework Excel/JSON (e.g., "Control ID", "Description")
type ControlHeader string

// String value for a control field
type ControlValue string

// Control ID (e.g., "IAC-01", "CC6.1", "Article 5")
type ControlID string

// Flexible control representation - map of headers to values
type Control map[ControlHeader]ControlValue

// Core mapping structure: SCF Control ID → Frameworks → Framework Control IDs
// Example: "IAC-01" → { "SOC 2" → ["CC6.1", "CC6.2"], "ISO 27001" → ["A.9.2.1"] }
type SCFControlMappings map[ControlID]map[Framework][]ControlID
```

### Example Mapping

```go
scfControlMappings := map[string]map[string][]string{
    "IAC-01": {
        "SOC 2":     []string{"CC6.1", "CC6.2"},
        "ISO 27001": []string{"A.9.2.1"},
        "NIST 800-53": []string{"IA-2"},
    },
}
```

This structure enables bidirectional lookups:
- Given SCF control → find all related framework controls
- Given framework control → find related SCF control (via reverse lookup)

## Critical Configuration

### Supported Frameworks Map

**Location:** `internal/scf.go` lines 62-70

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

**How to Use:**
- The **key** is the framework name used throughout the codebase
- The **value** is the exact column header in `scf.xlsx` that contains the framework's control mappings
- To enable a framework: uncomment or add a line
- To disable a framework: comment out the line

### Caching Flag

**Location:** `main.go` line 12

```go
getFile := false  // true = download fresh data, false = use cached JSON
```

Set to `false` during development to use cached JSON files for faster iteration.

## Module-by-Module Guide

### main.go (Entry Point)

**Purpose:** Orchestrates the entire generation pipeline sequentially.

**Flow:**
1. Process SCF (hub) → Generate mappings
2. Process SOC 2 → Link to SCF
3. Process GDPR → Link to SCF
4. Process ISO 27001 → Link to SCF
5. Process ISO 27002 → Link to SCF
6. Process NIST 800-53 → Link to SCF

**Key Variables:**
- `latestScfLink` - URL to SCF Excel file
- `getFile` - Download fresh data vs use cache
- `scfControlMappings` - The core mapping structure passed to all generators

### internal/scf.go (Core Mapping Engine)

**Purpose:** The brain of the operation. Handles SCF parsing and creates all cross-framework mappings.

**Key Functions:**

#### `ReturnSCFControls(url string, getFile bool) ([]Control, error)`
- Downloads/reads SCF Excel file
- Parses all rows into Control structs
- Returns 576 controls with all their metadata

#### `GetComplianceControlMappings(scfControls []Control) SCFControlMappings`
- Iterates through all SCF controls
- For each enabled framework in `SupportedFrameworks`:
  - Extracts framework control IDs from the SCF Excel column
  - Builds the mapping: SCF ID → Framework → [Control IDs]
- Returns the complete bidirectional mapping structure

#### `GenerateSCFMarkdown(control Control, scfID ControlID, mappings map[Framework][]ControlID)`
- Creates individual SCF control page (e.g., `scf/iac-01-user-identification.md`)
- Includes control description, objective, guidance
- Adds "Mapped Framework Controls" section with links to related framework controls
- Example: IAC-01 page links to SOC 2 CC6.1, ISO 27001 A.9.2.1, etc.

#### `GenerateSCFIndex(mappings SCFControlMappings, controls []Control)`
- Creates `scf/index.md` organized by control families
- Groups controls: AST (Asset Management), BCD (Business Continuity), IAC (Identity), etc.
- 30 families total

**Important Constants:**
- `SCFControlID` - Header for SCF control IDs
- `SCFControlFamilyTitle` - Header for family names
- Control family codes: AST, BCD, CPL, CRY, DCH, END, GOV, HRS, IAC, IAM, IAO, etc.

### internal/soc2.go (SOC 2 Processor)

**Purpose:** Parse SOC 2 controls from Prowler JSON format and generate linked documentation.

**Key Functions:**

#### `GetSOC2Controls(url string, getFile bool) (SOC2Framework, error)`
- Downloads JSON from Prowler cloud
- Parses into SOC2Framework struct with Requirements array
- Each requirement has: ID, Description, Attributes (trust service criteria)

#### `GenerateSOC2Markdown(req Requirement, scfMappings SCFControlMappings)`
- Creates individual SOC 2 control page (e.g., `soc2/cc6.1.md`)
- Parses multi-section descriptions (headers like "Description:", "Criteria:")
- **Reverse mapping:** Searches scfMappings to find which SCF controls map to this SOC 2 control
- Adds "Related SCF Controls" section with links back to SCF

#### `GenerateSOC2Index(framework SOC2Framework)`
- Creates `soc2/index.md` with all SOC 2 controls listed

**Data Structure:**
```go
type SOC2Framework struct {
    Framework    string
    Requirements []Requirement
}
type Requirement struct {
    Id          string
    Description string
    Attributes  []Attribute
}
```

### internal/gdpr.go (GDPR Processor)

**Purpose:** Parse GDPR articles from Markdown source and generate linked documentation.

**Key Functions:**

#### `GetGDPRControls(url string, getFile bool) ([]GDPRArticle, error)`
- Downloads Markdown from EnterpriseReady
- Parses hierarchical structure: Articles contain sub-articles
- Example: Article 5 has sub-articles 5.1(a), 5.1(b), etc.

#### `GenerateGDPRMarkdown(article GDPRArticle, scfMappings SCFControlMappings)`
- Creates article page (e.g., `gdpr/article-5.md`)
- Includes all sub-articles with anchor links
- **Reverse mapping:** Links back to related SCF controls

#### `GenerateGDPRIndex(articles []GDPRArticle)`
- Creates `gdpr/index.md` with article listing

**Data Structure:**
```go
type GDPRArticle struct {
    Title         string
    ControlNumber string
    ControlTitle  string
    Text          string
    SubArticles   []GDPRArticle  // Recursive for hierarchical structure
}
```

### internal/iso.go (ISO 27001/27002 Processor)

**Purpose:** Parse ISO controls from JupiterOne JSON and generate linked documentation.

**Key Functions:**

#### `GetISOControls(framework Framework, url string, getFile bool) (ISOFramework, error)`
- Downloads JSON from JupiterOne
- Parses domains (organizational categories)
- Handles both ISO 27001 (requirements) and ISO 27002 (controls)

#### `GenerateISOMarkdown(framework Framework, domain ISODomain, scfMappings SCFControlMappings)`
- Creates domain page (e.g., `iso27001/a.5-organizational-controls.md`)
- Lists all controls in the domain
- **Reverse mapping:** Links to related SCF controls

#### `FCIDToAnnex(fcid string) string`
- Converts Framework Control ID to Annex reference
- Example: "iso-27001_a.5.1" → "Annex A.5.1"

**Data Structure:**
```go
type ISOFramework struct {
    Domains []ISODomain
}
type ISODomain struct {
    Title    string
    Ref      string
    Controls []ISOControl
}
type ISOControl struct {
    Ref         string
    Title       string
    Description string
}
```

### internal/nist80053.go (NIST 800-53 Processor)

**Purpose:** Parse NIST 800-53 controls from FedRAMP OSCAL JSON and generate linked documentation.

**Key Functions:**

#### `GetNIST80053Controls(url string, getFile bool) (NIST80053, error)`
- Downloads OSCAL-formatted JSON from GSA FedRAMP
- Parses control families (AC, AT, AU, CA, etc.)
- Handles hierarchical controls (e.g., AC-1, AC-1(1), AC-1(2) are parent and sub-controls)

#### `GenerateNIST80053Markdown(control NISTControl, scfMappings SCFControlMappings)`
- Creates control page (e.g., `nist80053/ac-1.md`)
- Includes control statement, guidance, parameters
- Lists sub-controls (enhancements)
- **Reverse mapping:** Links to related SCF controls

#### `GenerateNIST80053Index(framework NIST80053)`
- Creates `nist80053/index.md` organized by control families

**Data Structure (OSCAL-based):**
```go
type NIST80053 struct {
    Families []NISTFamily
}
type NISTFamily struct {
    Title    string
    Controls []NISTControl
}
type NISTControl struct {
    ID        string
    Title     string
    Parts     []NISTPart     // Statements, guidance
    Controls  []NISTControl  // Sub-controls (recursive)
    Params    []NISTParam    // Configurable parameters
}
```

### internal/file.go (Utilities)

**Purpose:** Filename sanitization for filesystem compatibility.

#### `safeFileName(s string) string`
- Converts to lowercase
- Removes special characters
- Replaces spaces with hyphens
- Ensures valid filesystem names across platforms

## SCF Control Families (30 Total)

| Code | Family Name |
|------|-------------|
| AST | Asset Management |
| BCD | Business Continuity & Disaster Recovery |
| CPL | Compliance |
| CRY | Cryptography |
| DCH | Data Classification & Handling |
| END | Endpoint Security |
| GOV | Governance |
| HRS | Human Resources Security |
| IAC | Identification & Authentication |
| IAM | Identity & Access Management |
| IAO | Incident Response, Continuity of Operations Planning & Disaster Recovery |
| MDM | Mobile Device Management |
| NET | Network Security |
| PRI | Privacy |
| RSK | Risk Management |
| SDA | Secure Engineering & Architecture |
| SEA | Security Assessment |
| STA | Secure Systems Administration |
| TDA | Technology Development & Acquisition |
| THR | Threat Management |
| TPS | Third-Party Management |
| TPM | Training, Awareness & Education |
| VPM | Vulnerability & Patch Management |
| WEB | Web Security |
| ... | (and 6 others) |

## Common Tasks & How-To

### Regenerate All Documentation

```bash
go run main.go
```

This will:
1. Read SCF Excel file (or download if missing)
2. Download/read cached framework data
3. Generate 1000+ Markdown files in framework directories
4. Create index files for each framework

### Add a New Framework

**Steps:**

1. **Update `SupportedFrameworks` map** in `internal/scf.go`:
   ```go
   var SupportedFrameworks = map[Framework]ControlHeader{
       "SOC 2":     "AICPA TSC 2017 (Controls)",
       "HIPAA":     "US HIPAA",  // <-- Add this line
   }
   ```

2. **Create new processor file** `internal/hipaa.go`:
   ```go
   package internal

   func GetHIPAAControls(url string, getFile bool) (HIPAAFramework, error) {
       // Download and parse HIPAA data
   }

   func GenerateHIPAAMarkdown(control HIPAAControl, scfMappings SCFControlMappings) {
       // Generate HIPAA control pages with SCF links
   }

   func GenerateHIPAAIndex(framework HIPAAFramework) {
       // Generate hipaa/index.md
   }
   ```

3. **Add to `main.go` pipeline**:
   ```go
   hipaaLink := "https://example.com/hipaa.json"
   hipaaFramework, err := internal.GetHIPAAControls(hipaaLink, getFile)
   if err != nil {
       log.Fatal(err)
   }
   for _, control := range hipaaFramework.Controls {
       internal.GenerateHIPAAMarkdown(control, scfControlMappings)
   }
   internal.GenerateHIPAAIndex(hipaaFramework)
   ```

4. **Run:** `go run main.go`

### Update SCF to Newer Version

1. Download new SCF Excel file from https://securecontrolsframework.com/
2. Replace `scf.xlsx` in repository root
3. Update version references in documentation
4. Run `go run main.go` to regenerate all documentation

### Enable/Disable Frameworks

Edit `SupportedFrameworks` map in `internal/scf.go`:
- **Disable:** Comment out the line
- **Enable:** Uncomment the line

Example:
```go
var SupportedFrameworks = map[Framework]ControlHeader{
    "SOC 2":     "AICPA TSC 2017 (Controls)",
    // "GDPR":      "EMEA EU GDPR",  // Disabled
    "ISO 27001": "ISO 27001 v2022",
}
```

### Use Cached Data (Faster Development)

Set `getFile = false` in `main.go` line 12:
```go
getFile := false  // Use cached *.json files instead of downloading
```

### Debug Mapping Issues

1. **Check SCF Excel file** - Verify the framework column header matches `SupportedFrameworks` value exactly
2. **Print mappings** - Add debug logging in `GetComplianceControlMappings()`:
   ```go
   fmt.Printf("SCF %s maps to %s: %v\n", scfID, framework, controlIDs)
   ```
3. **Verify control ID parsing** - Check that framework control IDs are correctly extracted from SCF cells

## Design Patterns & Best Practices

### 1. Caching Strategy

**Purpose:** Reduce external API calls during development.

**Implementation:**
- All framework data can be cached as JSON files
- `getFile` parameter controls download vs cache
- SCF Excel file is manual (not auto-downloaded)

**Trade-offs:**
- Faster iteration when `getFile = false`
- Must manually update cache to get latest framework data

### 2. Type Safety with Flexibility

**Pattern:** Use typed constants for structure, maps for flexibility.

```go
type Framework string        // Typed for safety
type Control map[ControlHeader]ControlValue  // Map for flexibility
```

**Rationale:**
- Different frameworks have different fields
- Maps allow adding new fields without struct changes
- Type aliases provide compile-time safety

### 3. Bidirectional Linking

**Pattern:** Create mappings in both directions.

**Implementation:**
1. Forward: `scf.go` generates SCF pages with links to framework controls
2. Reverse: Each framework processor searches `scfControlMappings` to find which SCF controls reference it

**Code Example:**
```go
// Forward (scf.go)
for framework, controlIDs := range mappings {
    md.PlainText(fmt.Sprintf("- %s: ", framework))
    for _, id := range controlIDs {
        md.Link(id, fmt.Sprintf("../%s/%s.md", framework, id))
    }
}

// Reverse (soc2.go)
for scfID, frameworkMappings := range scfMappings {
    if soc2IDs, exists := frameworkMappings["SOC 2"]; exists {
        for _, soc2ID := range soc2IDs {
            if soc2ID == currentControlID {
                md.Link(scfID, fmt.Sprintf("../scf/%s.md", scfID))
            }
        }
    }
}
```

### 4. Relative Markdown Links

**Pattern:** Use relative paths for portability.

**Examples:**
- From SCF to SOC 2: `../soc2/cc6.1.md`
- From SOC 2 to SCF: `../scf/iac-01.md`
- Within same framework: `./other-control.md`

**Benefits:**
- Works locally and on GitHub Pages
- No hardcoded URLs
- Easy to move/deploy

### 5. Error Propagation

**Pattern:** Errors bubble up to `main()` for centralized handling.

**Implementation:**
```go
// main.go
soc2Framework, err := internal.GetSOC2Controls(soc2Link, getFile)
if err != nil {
    log.Fatal(err)  // Fail fast with clear error
}
```

**Rationale:**
- Clean failure rather than partial generation
- Easy to identify which stage failed
- No need for complex error recovery

### 6. Declarative Configuration

**Pattern:** Use data structures to declare behavior.

**Example:** `SupportedFrameworks` map declares which frameworks to process.

**Benefits:**
- Easy to add/remove frameworks
- Self-documenting code
- No need to modify multiple locations

## Testing & Validation

### Manual Testing Checklist

After code changes, verify:

- [ ] `go run main.go` completes without errors
- [ ] All framework directories contain expected number of files
- [ ] Generated Markdown files have valid syntax
- [ ] Links work (open in Markdown preview)
- [ ] Index files are properly organized
- [ ] Bidirectional links are correct (SCF → framework and framework → SCF)

### Common Issues

**Problem:** Missing framework controls in SCF mappings
**Cause:** Column header mismatch in `SupportedFrameworks`
**Fix:** Check `scf.xlsx` for exact column name

**Problem:** Broken links in generated Markdown
**Cause:** Filename sanitization or incorrect path construction
**Fix:** Verify `safeFileName()` logic and relative path format

**Problem:** Slow generation
**Cause:** Downloading fresh data every run
**Fix:** Set `getFile = false` to use cached JSON

**Problem:** Empty framework directory
**Cause:** Download failure or JSON parsing error
**Fix:** Check error logs, verify external URL accessibility

## Development Workflow

### Typical Iteration Cycle

1. **Make code changes** in `internal/*.go`
2. **Set caching:** `getFile = false` in `main.go`
3. **Run:** `go run main.go`
4. **Verify output:** Check generated Markdown files
5. **Iterate:** Repeat steps 1-4
6. **Final test:** Set `getFile = true` and run full pipeline
7. **Commit:** Add changes to git (exclude generated .md files if desired)

### Git Workflow

**Generated files:** The `scf/`, `soc2/`, etc. directories contain generated output. You can:
- **Option A:** Commit them (current approach) for GitHub Pages
- **Option B:** Add to `.gitignore` and generate via CI/CD

**Currently:** Generated files ARE committed for GitHub Pages deployment.

## Deployment

### GitHub Pages

**Configuration:**
- Workflow: `.github/workflows/publish.yml`
- Branch: Published from `main` branch
- Directory: Repository root (not `/docs`)

**Process:**
1. Commit generated Markdown files
2. Push to GitHub
3. GitHub Actions builds Jekyll site
4. Site published at https://engseclabs.github.io/graphgrc/

### Local Preview

Use any Markdown viewer or static site generator:

```bash
# Option 1: Python HTTP server
python -m http.server 8000

# Option 2: Jekyll (GitHub Pages locally)
bundle exec jekyll serve
```

## Performance Characteristics

| Metric | Value | Notes |
|--------|-------|-------|
| Total files generated | 1,033 | Includes all frameworks + indexes |
| Total size | ~44 MB | Includes all Markdown files |
| SCF controls | 576 | Core mapping layer |
| SCF control families | 30 | Organizational categories |
| Generation time | ~10-30 seconds | Depends on network, caching |
| Lines of Go code | ~1,137 LOC | Internal package only |

## Future Enhancement Ideas

### Potential Improvements

1. **Add more frameworks:**
   - HIPAA (already in SCF Excel)
   - ISO 27701 (already in SCF Excel)
   - PCI DSS
   - CIS Controls
   - NIST Cybersecurity Framework

2. **Enhanced output formats:**
   - JSON API for programmatic access
   - Interactive web UI with search
   - PDF export of full documentation
   - Graph visualization of control relationships

3. **Improved mapping:**
   - Fuzzy matching for similar controls
   - Confidence scores for mappings
   - Gap analysis (controls in framework not in SCF)

4. **Developer experience:**
   - Unit tests for parsers
   - Integration tests for full pipeline
   - CLI flags for selective framework generation
   - Progress bars for long operations

5. **Data quality:**
   - Validate external URLs before processing
   - Retry logic for downloads
   - Schema validation for JSON inputs
   - Diff checker for SCF updates

## AI Assistant Guidelines

When working on this codebase:

### DO:
- ✅ Read the relevant `internal/*.go` file before suggesting changes
- ✅ Maintain the hub-and-spoke architecture (SCF as hub)
- ✅ Preserve bidirectional linking in both directions
- ✅ Follow Go conventions (error handling, naming)
- ✅ Update `SupportedFrameworks` when adding frameworks
- ✅ Test changes with `go run main.go`
- ✅ Keep filename sanitization consistent
- ✅ Use relative Markdown links
- ✅ Handle hierarchical controls (GDPR sub-articles, NIST sub-controls)

### DON'T:
- ❌ Break the SCF mapping layer
- ❌ Remove bidirectional links
- ❌ Hardcode absolute URLs
- ❌ Skip error handling
- ❌ Modify `scf.xlsx` programmatically (manual updates only)
- ❌ Change generated file structure without updating links
- ❌ Add dependencies without justification
- ❌ Over-engineer simple functionality

### When Suggesting Changes:
1. **Explain the "why"** - What problem does this solve?
2. **Show the impact** - Which files need changes?
3. **Provide complete code** - Don't use placeholders
4. **Consider backwards compatibility** - Will existing links break?
5. **Test mentally** - Walk through the data flow

## Troubleshooting

### Framework not appearing in output

1. Check `SupportedFrameworks` map - is it enabled?
2. Verify column header in `scf.xlsx` matches exactly
3. Check if external URL is accessible
4. Look for errors in console output

### Links not working

1. Verify relative path format: `../framework/control.md`
2. Check filename sanitization - special characters removed?
3. Ensure control ID matches filename
4. Test link locally with Markdown preview

### Missing SCF mappings

1. Open `scf.xlsx` and find the control row
2. Check the framework column - is it populated?
3. Verify control IDs are correctly formatted
4. Look for parsing errors in `GetComplianceControlMappings()`

### Slow performance

1. Set `getFile = false` to use cached data
2. Check network connectivity
3. Verify external URLs are responsive
4. Consider reducing number of enabled frameworks

## Version History

- **Current:** SCF 2023.4
- **Go:** 1.21
- **Initial Release:** 2023

## Additional Resources

- **SCF Official Site:** https://securecontrolsframework.com/
- **Published GraphGRC Site:** https://engseclabs.github.io/graphgrc/
- **Source Repository:** https://github.com/engseclabs/graphgrc/
- **Go Documentation:** https://go.dev/doc/

---

**This document is maintained as part of the GraphGRC project. When making significant changes to the codebase, please update this file to keep it accurate for future AI assistants and human developers.**
