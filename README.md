# GraphGRC

GraphGRC is data-driven documentation for a GRC program.

See [source code](https://github.com/alsmola/graphgrc/) and a [published documentation example](https://alsmola.github.io/graphgrc/).

- Semantic: GRC program requirements (SOC 2, GDPR, etc.) parsed, structured, and rendered with Markdown
- Linkable: Map similar controls from different frameworks with a custom control framework
- Practical: Minimal, risk-focused control framework (24 controls) tailored for modern organizations

## Published Documentation

The published example uses a custom control framework (24 controls) tailored for AWS SaaS organizations with ~100 people and macOS endpoints. Focuses on risk-reducing behaviors over checkbox compliance.

**View the documentation:**
- [Custom Controls](custom/index.md) - 24 controls with implementation guidance
- [SOC 2](soc2/index.md) - Mapped to custom controls
- [GDPR](gdpr/index.md) - Mapped to custom controls

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
