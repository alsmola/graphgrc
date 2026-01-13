# Link Validation for GraphGRC Documentation

This document describes the link validation tools available for the GraphGRC documentation system.

## Overview

The GraphGRC documentation contains thousands of interconnected markdown files with links between controls, frameworks, policies, and standards. To ensure documentation quality, we provide automated tools to validate and fix broken links.

## Validation Results (Current)

- **Total links:** 4,860
- **Valid links:** 4,689 (96.5%)
- **Broken links:** 171 (3.5%)

The remaining broken links fall into these categories:
1. **Template placeholders** (24) - `../custom/control-id.md` - intentional placeholders in templates
2. **Missing framework controls** (147) - references to controls not yet generated (ISO 27701, some GDPR articles, SOC 2 PI controls)

## Available Make Targets

### `make validate-links`

Validates all markdown links in the `docs/` directory.

```bash
make validate-links
```

**Output:**
- Summary of total links, valid links, and broken links
- Detailed list of each broken link with file location and line number
- Exit code 1 if any broken links are found (useful for CI/CD)

**Use cases:**
- Pre-deployment validation
- CI/CD pipeline integration
- Regular documentation health checks

### `make fix-links`

Automatically fixes broken links by finding the correct paths.

```bash
make fix-links
```

**What it fixes:**
- Framework links (SOC 2, GDPR, ISO, NIST, SCF)
- Custom control references
- Cross-directory links
- Relative path corrections

**What it doesn't fix:**
- Links to non-existent files
- Placeholder/template links
- External URLs

**Output:**
- List of files modified
- Count of links fixed per file
- Summary of total fixes

### `make clean`

Removes build artifacts and temporary files.

```bash
make clean
```

Removes:
- `bin/` directory (compiled binaries)
- `*.tmp` files in docs/

## Implementation Details

### Link Validator (`src/cmd/validate-links/main.go`)

**Features:**
- Recursively scans all markdown files in a directory
- Extracts markdown links using regex: `[text](path)`
- Validates that target files/directories exist
- Skips external links (http://, https://, mailto:)
- Skips anchor-only links (#section)
- Reports line numbers for debugging

**Algorithm:**
1. Walk directory tree
2. For each `.md` file:
   - Parse all markdown links
   - Resolve relative paths
   - Check if target exists
   - Report broken links

### Link Fixer (`src/cmd/fix-links/main.go`)

**Features:**
- Automatically corrects common link pattern errors
- Handles framework-specific link patterns
- Preserves anchors (#section references)
- Uses pattern matching to identify control types

**Link patterns recognized:**

| Pattern | Type | Example | Fixed Path |
|---------|------|---------|------------|
| `cc*.md` | SOC 2 | `cc61.md` | `frameworks/soc2/cc61.md` |
| `art*.md` | GDPR | `art32.md` | `frameworks/gdpr/art32.md` |
| `a-*.md` | ISO 27002 | `a-5.md` | `frameworks/iso27002/a-5.md` |
| `\d+.md` | ISO 27001 | `7.md` | `frameworks/iso27001/7.md` |
| `[a-z]{2}-\d+.md` | NIST | `ac-2.md` | `frameworks/nist80053/ac-2.md` |
| `[a-z]{3}-\d{2}.md` | Custom | `acc-01.md` | `custom/acc-01.md` |
| `[a-z]{3}-\d+*.md` | SCF | `gov-01.md` | `frameworks/scf/gov-01-*.md` |

**Algorithm:**
1. Read file content
2. Find all markdown links
3. For each link:
   - Skip if external or anchor-only
   - Check if target exists
   - If not, try pattern matching
   - Replace with correct path
4. Write updated content if changes made

## CI/CD Integration

Add to your GitHub Actions workflow:

```yaml
name: Validate Documentation Links

on:
  push:
    paths:
      - 'docs/**/*.md'
  pull_request:
    paths:
      - 'docs/**/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Go
        uses: actions/setup-go@v4
        with:
          go-version: '1.21'

      - name: Validate links
        run: make validate-links
```

## Common Broken Link Types

### 1. Framework Control References

**Problem:** Custom controls link to framework controls without full path
```markdown
[CC6.1](cc61.md)
```

**Fixed to:**
```markdown
[CC6.1](frameworks/soc2/cc61.md)
```

### 2. SCF Control References

**Problem:** Links use short names but files have long descriptive names
```markdown
[GOV-01](gov-01.md)
```

**Fixed to:**
```markdown
[GOV-01](frameworks/scf/gov-01-cybersecurity&dataprotectiongovernanceprogram.md)
```

### 3. Cross-Framework Links

**Problem:** Framework files link to other frameworks without relative path
```markdown
[Article 32](art32.md)
```

**Fixed to:**
```markdown
[Article 32](../gdpr/art32.md)
```

### 4. ISO Numeric Controls

**Problem:** SCF files link to ISO controls by number only
```markdown
[7.4.a](7.md#74a)
```

**Fixed to:**
```markdown
[7.4.a](../iso27001/7.md#74a)
```

## Known Limitations

### Unfixable Broken Links

The following link types cannot be automatically fixed:

1. **Template placeholders:** `../custom/control-id.md` - intentional placeholders
2. **Missing controls:** References to controls not yet generated
3. **Typos in link text:** Validator can't detect semantic errors

### Missing Framework Controls

Some framework controls referenced in SCF mappings don't have generated markdown files:

- **SOC 2 PI controls:** PI1.1, PI1.2, PI1.4, PI1.5
- **GDPR articles:** Article 43 and others
- **ISO 27701:** P5.2, P5.1, P4.3, C1.1, C1.2

These would need to be added to the documentation generation process in `src/main.go`.

## Development

### Building the Tools

```bash
# Build validator
make build-validator

# Build fixer
make build-fixer

# Run directly
./bin/validate-links docs/
./bin/fix-links docs/
```

### Adding New Link Patterns

To add support for new framework link patterns:

1. Edit `src/cmd/fix-links/main.go`
2. Add pattern detection in `tryFixFrameworkLink()`
3. Add helper function if needed (like `isNISTControl()`)
4. Test with sample files

Example:
```go
} else if strings.HasPrefix(filename, "pci-") {
    // PCI DSS control
    frameworkPaths = []string{
        "frameworks/pcidss/" + filename,
    }
}
```

## Troubleshooting

### Validator reports false positives

- Check if the file actually exists at the reported path
- Verify the link syntax is correct: `[text](path)`
- Ensure paths use forward slashes, not backslashes

### Fixer doesn't fix certain links

- Check if the target file actually exists
- Verify the link pattern is recognized (see table above)
- Run validator after fixer to see remaining issues

### Performance issues with large documentation sets

- The tools process all files in memory
- For very large documentation (>10,000 files), consider:
  - Running on subdirectories
  - Increasing system memory limits
  - Parallelizing file processing

## Future Enhancements

Potential improvements:

1. **Parallel processing** - Process files concurrently for speed
2. **Incremental validation** - Only check changed files in git
3. **Anchor validation** - Verify that `#section` anchors exist
4. **External link checking** - Validate HTTP/HTTPS links (with caching)
5. **Auto-fix on commit** - Git pre-commit hook integration
6. **Link suggestion** - Fuzzy matching for typos
7. **Report formats** - JSON, HTML, or markdown output

## Related Documentation

- [Project README](../README.md)
- [Documentation Structure](STRUCTURE.md)
- [GraphGRC Architecture](../CLAUDE.md)
