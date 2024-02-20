# Compliance Mapper

Use [Secure Controls Framework (SCF)](https://securecontrolsframework.com/) to connect and understand all of the applicable framework controls for your security program.

See the default selected frameworks:

- [GDPR](gdpr/index.md)
- [SOC 2](soc2/index.md)
- [ISO 27001](iso27001/index.md)
- [ISO 27002](iso27002/index.md)

Applicable SCF controls:

- [SCF](scf/index.md)

# To customize

In [scf.go](internal/scf.go), specify the applicable frameworks in the `SupportedFrameworks` map, e.g.:

```
var SupportedFrameworks = map[Framework]ControlHeader{
	"SOC 2":     "AICPA TSC 2017 (Controls)",
	"GDPR":      "EMEA EU GDPR",
	"ISO 27001": "ISO 27001 v2022",
	"ISO 27002":   "ISO 27002 v2022",
	// "ISO 27701":   "ISO 27701 v2019",
	// "NIST 800-53": "NIST 800-53 rev5 (moderate)",
	// "HIPAA":       "US HIPAA",
}
```

Then, run the following command to generate the Markdown and create the internal links:

`go run main.go`
