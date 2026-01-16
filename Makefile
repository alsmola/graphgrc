.PHONY: help validate-links fix-links build-validator build-fixer clean clean-generated test convert-framework-mappings generate regenerate

# Default target
help:
	@echo "GraphGRC Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  validate-links              - Validate all markdown links in docs/"
	@echo "  fix-links                   - Automatically fix broken markdown links"
	@echo "  build-validator             - Build the link validator binary"
	@echo "  build-fixer                 - Build the link fixer binary"
	@echo "  convert-framework-mappings  - Convert framework mappings from bullet to annotation format"
	@echo "  clean                       - Remove build artifacts"
	@echo "  clean-generated             - Remove all generated framework documentation"
	@echo "  test                        - Run all tests"
	@echo "  generate                    - Generate all documentation"
	@echo "  regenerate                  - Clean and regenerate all documentation"

# Validate all markdown links
validate-links: build-validator
	@echo "Validating markdown links..."
	@./bin/validate-links docs/

# Fix broken markdown links
fix-links: build-fixer
	@echo "Fixing markdown links..."
	@./bin/fix-links docs/

# Build the link validator
build-validator:
	@mkdir -p bin
	@cd src/cmd/validate-links && go build -o ../../../bin/validate-links .
	@echo "✓ Link validator built: bin/validate-links"

# Build the link fixer
build-fixer:
	@mkdir -p bin
	@cd src/cmd/fix-links && go build -o ../../../bin/fix-links .
	@echo "✓ Link fixer built: bin/fix-links"

# Clean build artifacts
clean:
	@rm -rf bin/
	@find docs -name "*.tmp" -type f -delete
	@echo "✓ Cleaned build artifacts and temporary files"

# Clean all generated framework documentation
clean-generated:
	@echo "Removing generated framework documentation..."
	@rm -rf docs/frameworks/scf/*.md docs/frameworks/soc2/*.md docs/frameworks/gdpr/*.md docs/frameworks/iso27001/*.md docs/frameworks/iso27002/*.md docs/frameworks/nist80053/*.md 2>/dev/null || true
	@rm -f docs/frameworks/scf/index.md docs/frameworks/soc2/index.md docs/frameworks/gdpr/index.md docs/frameworks/iso27001/index.md docs/frameworks/iso27002/index.md docs/frameworks/nist80053/index.md 2>/dev/null || true
	@echo "✓ Cleaned generated documentation files"

# Run tests
test:
	@cd src && go test ./...

# Generate all documentation
generate:
	@echo "Generating documentation..."
	@cd src && go run main.go
	@echo "✓ Documentation generated"

# Clean and regenerate all documentation
regenerate: clean-generated generate
	@echo "✓ Documentation regenerated successfully"

# Convert framework mappings from bullet to annotation format
convert-framework-mappings:
	@mkdir -p bin
	@cd src/cmd/convert-framework-mappings && go build -o ../../../bin/convert-framework-mappings .
	@echo "✓ Converter built: bin/convert-framework-mappings"
	@./bin/convert-framework-mappings
	@echo "✓ Framework mappings converted"
