# GraphGRC

GraphGRC is data-driven documentation for a GRC program.

## What is this?

A practical, minimal control framework (24 controls) tailored for modern AWS SaaS organizations. Focuses on risk-reducing behaviors over checkbox compliance, with bidirectional mappings to SOC 2 and GDPR requirements.

```
Framework Controls (SOC 2, GDPR, ISO 27001, etc.)
    ⬆️ map to
Custom Controls (ACC-01, DAT-01, etc.)
    ⬆️ implement 
Standards, Processes, Policies, Charter
```

**Key features:**
- **Semantic:** GRC requirements (SOC 2, GDPR) parsed, structured, and rendered as navigable Markdown
- **Linked:** Bidirectional mappings show how controls satisfy multiple framework requirements
- **Practical:** Implementation guidance for real-world AWS SaaS environments (~100 people, macOS endpoints, cloud-native)

## Published Documentation

Browse the live example at **[engseclabs.github.io/graphgrc/](https://engseclabs.github.io/graphgrc/)**

The published site includes:
- [**24 Custom Controls**](https://engseclabs.github.io/graphgrc/custom/) - Organized by security domain with implementation guidance
- [**SOC 2 Mappings**](https://engseclabs.github.io/graphgrc/soc2/) - Each requirement linked to relevant controls
- [**GDPR Mappings**](https://engseclabs.github.io/graphgrc/gdpr/) - Each article linked to relevant controls

**Organization profile:** AWS SaaS, no physical datacenters, ~100 people, macOS endpoints, modern security practices (WebAuthn, full disk encryption, cloud-native)

## Two Modes Available

### Custom Mode (Default)

Uses a minimal, practical control framework (24 controls) tailored for AWS SaaS organizations. This is the mode used for the published documentation.

**Run custom mode:**
```bash
go run main.go --mode=custom
# or just
go run main.go
```

### SCF Mode (Comprehensive)

Uses the [Secure Controls Framework (SCF)](https://securecontrolsframework.com/) with 578 comprehensive controls covering multiple compliance frameworks including SOC 2, GDPR, ISO 27001, ISO 27002, and NIST 800-53.

**Run SCF mode:**
```bash
go run main.go --mode=scf
```

## Usage

### Command-line Flags

- `--mode` - Control framework mode: `custom` or `scf` (default: `custom`)
- `--fetch` - Fetch fresh data from remote sources instead of using cached files (default: `false`)

### Examples

```bash
# Generate using custom framework (default)
go run main.go

# Generate using SCF framework
go run main.go --mode=scf

# Fetch fresh data and generate with custom controls
go run main.go --fetch=true

# Fetch fresh data and generate with SCF
go run main.go --mode=scf --fetch=true
```

### Link Validation

Validate all markdown links before deployment:

```bash
# Validate all links in docs/
make validate-links

# Automatically fix broken links
make fix-links

# Clean build artifacts
make clean
```

See [docs/link-validation.md](docs/link-validation.md) for detailed documentation on link validation tools.

## Customization

### SCF Mode Customization

In [scf.go](internal/scf.go), specify the applicable frameworks in the `SupportedFrameworks` map:

```go
var SupportedFrameworks = map[Framework]ControlHeader{
	"SOC 2":       "AICPA TSC 2017 (Controls)",
	"GDPR":        "EMEA EU GDPR",
	"ISO 27001":   "ISO 27001 v2022",
	"ISO 27002":   "ISO 27002 v2022",
	"NIST 800-53": "NIST 800-53 rev5 (moderate)",
	// "HIPAA":    "US HIPAA",
}
```

### Custom Mode Customization

Edit [custom_controls.json](custom_controls.json) to:
- Modify control descriptions and implementation guidance
- Add/remove controls
- Update mappings to SOC 2 and GDPR requirements
- Change organization profile metadata

## Architecture

Both modes follow the same pattern:

1. Load control framework (SCF Excel or Custom JSON)
2. Parse framework-specific data (SOC 2, GDPR, ISO, NIST)
3. Generate bidirectional markdown links between controls and requirements
4. Create index pages for easy navigation
