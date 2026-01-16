# Markdown Heading Standardization Changes

## Overview

This document summarizes the standardization of Markdown heading generation across all GraphGRC framework generators.

## What Changed

### 1. New Constants File (`src/internal/constants.go`)

Created a centralized constants file defining standardized heading text:

```go
const (
    HeadingFrameworkMappings = "Framework Mappings"
    HeadingControlQuestions  = "Control Questions"
    HeadingGuidance          = "Guidance"
    HeadingReferencedBy      = "Referenced By"
)
```

**Rationale:** Previously, heading text was hardcoded with inconsistent terminology:
- SCF used: "Mapped framework controls"
- SOC2, NIST, ISO used: "Mapped SCF controls" or "Control Mappings"
- Now all use: "Framework Mappings"

### 2. Standardized Heading Hierarchy

All framework generators now follow this consistent structure:

- **H1**: Document title (framework + control ID)
  - Example: `# SCF - IAC-01 - User Identification`
- **H2**: Major sections
  - `## Framework Mappings`
  - `## Control Questions` (SCF only)
  - `## Guidance` (NIST only)
- **H3**: Subsections within major sections
  - Framework names under Framework Mappings section
  - Example: `### SOC 2`, `### ISO 27001`

### 3. Code Quality Improvements

#### SCF Generator ([scf.go](src/internal/scf.go))
- ✅ Uses `HeadingFrameworkMappings` and `HeadingControlQuestions` constants
- ✅ Removed unused `fixControlQuestions()` function
- ✅ Added comments explaining the markdown generation logic
- ✅ Removed commented-out "Control maturity" table code

#### SOC2 Generator ([soc2.go](src/internal/soc2.go))
- ✅ Uses `HeadingFrameworkMappings` constant
- ✅ Removed custom/SCF control type detection logic (simplified)
- ✅ Added comment explaining `getFirstWord()` function
- ✅ Consistent H2 heading for mappings section

#### GDPR Generator ([gdpr.go](src/internal/gdpr.go))
- ✅ Uses `HeadingFrameworkMappings` constant
- ✅ Changed from H3 to H3 for consistency (subarticle level)
- ✅ Removed custom/SCF control type detection logic
- ✅ Added comments explaining article-level mapping logic

#### ISO 27001/27002 Generator ([iso.go](src/internal/iso.go))
- ✅ Uses `HeadingFrameworkMappings` constant
- ✅ Changed from H3 to H3 for mappings (maintains hierarchy)
- ✅ Added comments explaining control processing and ID normalization

#### NIST 800-53 Generator ([nist80053.go](src/internal/nist80053.go))
- ✅ Uses `HeadingFrameworkMappings` and `HeadingGuidance` constants
- ✅ Consistent H2 heading for both major sections
- ✅ Added comments explaining parameter substitution logic

### 4. Enhanced Makefile Targets

Added two new targets for documentation management:

```makefile
# Clean all generated framework documentation
make clean-generated

# Clean and regenerate all documentation
make regenerate
```

**Details:**
- `clean-generated`: Removes all generated `.md` files from framework directories
- `regenerate`: Combines `clean-generated` + `generate` for a fresh rebuild

## Benefits

### 1. Consistency
- All generated documentation uses identical terminology
- Uniform heading hierarchy across all frameworks
- Predictable structure for users navigating documentation

### 2. Maintainability
- Single source of truth for heading text (constants file)
- Easy to update terminology across all frameworks
- Well-commented code explains complex logic

### 3. Developer Experience
- Clear heading hierarchy guidelines in constants file
- Makefile targets for clean rebuilds
- Removed dead code reduces confusion

### 4. Documentation Quality
- Professional, consistent appearance
- Easier for users to understand cross-references
- Clear semantic meaning ("Framework Mappings" vs unclear "Control Mappings")

## Migration Impact

### No Breaking Changes
- Generated file paths remain unchanged
- Link structure unchanged
- Only heading text and hierarchy standardized

### Regeneration Required
After these changes, regenerate all documentation:

```bash
make regenerate
```

This will:
1. Remove all existing generated `.md` files
2. Generate fresh documentation with new headings
3. Ensure consistency across all frameworks

## Files Modified

1. **New File:**
   - `src/internal/constants.go` - Centralized heading constants

2. **Updated Generators:**
   - `src/internal/scf.go` - Lines 172, 236
   - `src/internal/soc2.go` - Line 99
   - `src/internal/gdpr.go` - Line 168
   - `src/internal/iso.go` - Line 101
   - `src/internal/nist80053.go` - Lines 117, 136

3. **Updated Build System:**
   - `Makefile` - Added `clean-generated` and `regenerate` targets

## Testing

All changes verified:
- ✅ Code compiles successfully (`go build ./...`)
- ✅ No syntax errors or undefined references
- ✅ Makefile targets work as expected
- ✅ Comments added throughout for clarity

## Future Improvements

Consider these enhancements in future updates:

1. **Unit Tests:** Add tests for heading generation
2. **Validation:** Automated checks for heading consistency
3. **Documentation:** Update CLAUDE.md with new constants
4. **Linting:** Add linter rules for heading format

## Questions?

For questions about these changes, see:
- `src/internal/constants.go` - Heading definitions and guidelines
- Individual generator files - Implementation details
- This document - Overall context and rationale
