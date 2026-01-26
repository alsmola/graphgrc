.PHONY: help validate-links generate-backlinks build clean

# Default target
help:
	@echo "GraphGRC Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  validate-links      - Validate all markdown links in docs/"
	@echo "  generate-backlinks  - Regenerate implementation backlinks"
	@echo "  build               - Build both tools"
	@echo "  clean               - Remove build artifacts and temporary files"

# Validate all markdown links
validate-links:
	@echo "Validating markdown links..."
	@./bin/validate-links docs/

# Generate backlinks
generate-backlinks:
	@echo "Generating backlinks..."
	@./bin/generate-backlinks -root=docs -verbose

# Build both tools
build:
	@echo "Building tools..."
	@mkdir -p bin
	@cd src/cmd/validate-links && go build -o ../../../bin/validate-links .
	@echo "✓ validate-links built"
	@cd src/cmd/generate-backlinks && go build -o ../../../bin/generate-backlinks .
	@echo "✓ generate-backlinks built"
	@echo "Build complete!"

# Clean build artifacts and temporary files
clean:
	@rm -rf bin/
	@find docs -name "*.tmp" -type f -delete
	@echo "✓ Cleaned build artifacts and temporary files"
