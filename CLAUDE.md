# CLAUDE.md - AI Assistant Guide for GraphGRC

> Context for AI assistants working on the GraphGRC custom security controls framework.

## Project Overview

**GraphGRC** is a custom security controls framework with 76 AI-generated controls that map directly to compliance frameworks (SOC 2, GDPR, ISO 27001, NIST 800-53).

- **Language:** Go (for tools), Python (for scripts), Markdown (for documentation)
- **Repository:** https://github.com/engseclabs/graphgrc/
- **Published Site:** https://engseclabs.github.io/graphgrc/
- **License:** MIT

### What This Provides

**76 custom security controls** organized by family (IAM, cryptography, data privacy, incident response, etc.) with:
- Detailed implementation guidance
- Framework mappings (which SOC 2/GDPR/ISO/NIST requirements each control satisfies)
- Evidence requirements for audits
- Bidirectional traceability showing which standards/policies/processes implement each control

## Architecture

### Simple Direct Mapping

```
Implementation Docs ──→ Controls ──→ Frameworks
(Standards/Policies)       (76)     (SOC 2/GDPR/ISO/NIST)
```

**Key Principle:** Frameworks and implementation docs **never link directly to each other**. Controls are the only connection point.

**Link Structure:**
- Standards/Policies/Processes → Controls (via "Control Mapping")
- Controls → Frameworks (via "Framework Mapping")
- Controls ← Implementation Docs (auto-generated "Implemented By")
- Frameworks ← Controls (auto-generated "Referenced By")

**NOT:**
- ❌ Standards/Policies → Frameworks (wrong!)
- ❌ Frameworks → Standards/Policies (wrong!)

## Key Design Decisions

### 1. Custom Controls (Not SCF)

**Approach:** 76 custom AI-generated controls that directly map to frameworks
**Why:** More control over content, simpler architecture, no external dependencies
**Previous:** Used Secure Controls Framework (SCF) as mapping layer - removed in v2.0

### 2. Information Density

**Principle:** Controls should be specific and concrete, not vague umbrellas
- ✅ Good: "Multi-Factor Authentication", "Cloud IAM", "Encryption at Rest"
- ❌ Bad: "Identity & Authentication", "Least Privilege & RBAC"

### 3. Controls vs. Processes

**Rule:** Controls implement capabilities. Processes orchestrate controls.
- ✅ Control: "Vulnerability Detection" (scanning tools)
- ❌ Control: "Vulnerability Management Process" → This is a process

### 4. Bidirectional Traceability

**Goal:** Complete audit trail: framework requirements → controls → implementation
**Implementation:** Forward links manual (curated), backward links auto-generated

## Common Tasks

### Adding a New Control

```bash
# 1. Create file
vim docs/controls/iam/new-control.md

# 2. Add framework mappings
## Framework Mapping
### SOC 2
- [CC6.3](../../frameworks/soc2/cc63.md) ^[How this satisfies CC6.3]

# 3. Reference from implementation docs
vim docs/standards/aws-security-standard.md
- [New Control](../controls/iam/new-control.md) ^[How implemented]

# 4. Regenerate backlinks
./bin/generate-backlinks -root=docs -verbose
```

### Regenerating Backlinks

```bash
cd src/cmd/generate-backlinks && go build -o ../../../bin/generate-backlinks .
cd ../../..
./bin/generate-backlinks -root=docs -verbose
```

## Quality Metrics

- ✅ 100% controls filled (76/76)
- ✅ 100% controls have framework mappings (76/76)
- ✅ 100% controls have implementation backlinks (76/76)
- ✅ 551 total implementation backlinks

## AI Assistant Guidelines

### DO:
- ✅ Keep controls specific and information-dense
- ✅ Regenerate backlinks after changes
- ✅ Use annotated links: `[Name](path.md) ^[explanation]`
- ✅ Maintain bidirectional traceability

### DON'T:
- ❌ Create vague umbrella controls
- ❌ Put processes in controls/
- ❌ Manually edit "Implemented By" sections (auto-generated)
- ❌ Break bidirectional links

---

See [README.md](README.md) for full documentation.
