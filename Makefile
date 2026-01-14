.PHONY: help validate-links fix-links build-validator build-fixer clean test convert-framework-mappings

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
	@echo "  test                        - Run all tests"
	@echo "  generate                    - Generate all documentation"

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

# Run tests
test:
	@cd src && go test ./...

# Generate all documentation
generate:
	@cd src && go run main.go
	@echo "✓ Documentation generated"

# Convert framework mappings from bullet to annotation format
convert-framework-mappings:
	@mkdir -p bin
	@cd src/cmd/convert-framework-mappings && go build -o ../../../bin/convert-framework-mappings .
	@echo "✓ Converter built: bin/convert-framework-mappings"
	@./bin/convert-framework-mappings
	@echo "✓ Framework mappings converted"
