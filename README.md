# GraphGRC

GraphGRC is data-driven documentation for a GRC program.

See [source code](https://github.com/alsmola/graphgrc/) and a [published documentation example](https://alsmola.github.io/graphgrc/).

- Semantic: GRC program requirements (SOC 2, ISO 27001, GDPR, etc.) parsed, structured, and rendered with Markdown
- Linkable: Map similar controls from different frameworks with SCF or custom control framework
- Flexible: Choose between comprehensive SCF (578 controls) or tailored custom framework (24 controls)

## Two Modes Available

### SCF Mode (Comprehensive)

Uses the [Secure Controls Framework (SCF)](https://securecontrolsframework.com/) with 578 comprehensive controls covering multiple compliance frameworks.

**Generated frameworks:**
- [SCF](scf/index.md) - 578 controls organized by security domain
- [SOC 2](soc2/index.md) - Mapped to SCF controls
- [GDPR](gdpr/index.md) - Mapped to SCF controls
- [ISO 27001](iso27001/index.md) - Mapped to SCF controls
- [ISO 27002](iso27002/index.md) - Mapped to SCF controls
- [NIST 800-53](nist80053/index.md) - Mapped to SCF controls

**Run SCF mode:**
```bash
go run main.go --mode=scf
```

### Custom Mode (Tailored)

Uses a minimal, practical control framework (24 controls) tailored for AWS SaaS organizations with ~100 people and macOS endpoints. Focuses on risk-reducing behaviors over checkbox compliance.

**Generated frameworks:**
- [Custom Controls](custom/index.md) - 24 controls with implementation guidance
- [SOC 2](soc2/index.md) - Mapped to custom controls
- [GDPR](gdpr/index.md) - Mapped to custom controls

**Organization profile:** AWS SaaS, no physical datacenters, ~100 people, macOS endpoints, modern security practices (WebAuthn, full disk encryption, cloud-native)

**Run custom mode:**
```bash
go run main.go --mode=custom
```

## Usage

### Command-line Flags

- `--mode` - Control framework mode: `scf` or `custom` (default: `scf`)
- `--fetch` - Fetch fresh data from remote sources instead of using cached files (default: `false`)

### Examples

```bash
# Generate using SCF framework (default)
go run main.go

# Generate using custom framework
go run main.go --mode=custom

# Fetch fresh data and generate with SCF
go run main.go --mode=scf --fetch=true

# Fetch fresh data and generate with custom controls
go run main.go --mode=custom --fetch=true
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
