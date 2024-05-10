# GraphGRC

GraphGRC is data-driven documentation for a GRC program.

See [source code](https://github.com/alsmola/graphgrc/) and a [published documentation example](https://alsmola.github.io/graphgrc/).

- Semantic: GRC program requirements (SOC 2, ISO 27001, GDPR, etc.) parsed, structured, and redered with Markdown
- Linkable: Map similar controls from different Framework with the [Secure Controls Framework (SCF)](https://securecontrolsframework.com/)

Use to connect and understand all of the applicable framework controls for your security program.

See the default selected frameworks:

- [GDPR](gdpr/index.md)
- [SOC 2](soc2/index.md)
- [ISO 27001](iso27001/index.md)
- [ISO 27002](iso27002/index.md)
- [NIST 800-53](nist80053/index.md)

See the one single SCF control set that maps all frameworks:

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
	"NIST 800-53": "NIST 800-53 rev5 (moderate)",
	// "HIPAA":       "US HIPAA",
}
```

Then, run the following command to generate the Markdown and create the internal links:

`go run main.go`
