.PHONY: help download-frameworks generate-frameworks generate-custom generate-backlinks generate clean clean-generated regenerate

# Base directories
DOCS_DIR = ../docs
SRC_DIR = .

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

download-frameworks: ## Download framework data from external sources (SCF, Prowler, etc.)
	@echo "Downloading framework data..."
	go run main.go download

generate-frameworks: ## Generate framework control pages (SCF, SOC2, GDPR, ISO, NIST)
	@echo "Generating framework control pages..."
	go run main.go generate-frameworks

generate-custom: ## Generate custom control pages with semantic markdown
	@echo "Generating custom control pages..."
	go run main.go generate-custom

cleanup-framework-controls: ## Remove old main.go generated sections from framework controls
	@echo "Cleaning up framework control pages..."
	@go build -o bin/cleanup-framework-controls ./cmd/cleanup-framework-controls
	@./bin/cleanup-framework-controls -verbose

add-satisfies-sections: ## Add '## Satisfies Controls' sections to standards/processes/policies/charter
	@echo "Adding Satisfies Controls sections..."
	@go build -o bin/add-satisfies-sections ./cmd/add-satisfies-sections
	@./bin/add-satisfies-sections -verbose

validate-structure: ## Validate that all files have required sections for backlink generation
	@echo "Validating document structure..."
	@go build -o bin/validate-structure ./cmd/validate-structure
	@./bin/validate-structure -root=$(DOCS_DIR) -verbose

clean-backlinks: ## Remove all backlink sections (will be regenerated)
	@cd $(DOCS_DIR) && python3 ../src/scripts/clean-backlinks.py

generate-backlinks: ## Generate backlinks in standards/processes/policies/frameworks
	@echo "Generating backlinks..."
	@go build -o bin/generate-backlinks ./cmd/generate-backlinks
	@./bin/generate-backlinks -root=$(DOCS_DIR) -verbose

regenerate-backlinks: clean-backlinks generate-backlinks ## Clean and regenerate all backlinks

generate: generate-frameworks generate-custom cleanup-framework-controls generate-backlinks ## Generate all documentation

clean: ## Remove all generated files
	@echo "Cleaning generated files..."
	rm -rf $(DOCS_DIR)/soc2/*.md $(DOCS_DIR)/gdpr/*.md $(DOCS_DIR)/iso27001/*.md $(DOCS_DIR)/iso27002/*.md $(DOCS_DIR)/nist80053/*.md $(DOCS_DIR)/scf/*.md
	@echo "Clean complete"

clean-generated: ## Remove all generated framework documentation
	@echo "Cleaning generated framework documentation..."
	@rm -rf $(DOCS_DIR)/frameworks/scf/*.md $(DOCS_DIR)/frameworks/soc2/*.md $(DOCS_DIR)/frameworks/gdpr/*.md $(DOCS_DIR)/frameworks/iso27001/*.md $(DOCS_DIR)/frameworks/iso27002/*.md $(DOCS_DIR)/frameworks/nist80053/*.md 2>/dev/null || true
	@echo "✓ Cleaned generated documentation files"

regenerate: clean-generated generate-frameworks ## Clean and regenerate all framework documentation
	@echo "✓ Framework documentation regenerated successfully"

validate: ## Validate all markdown links and frontmatter
	@echo "Validating documentation..."
	go run main.go validate

watch: ## Watch for changes and regenerate
	@echo "Watching for changes..."
	@while true; do \
		inotifywait -q -r -e modify $(DOCS_DIR)/custom/ $(DOCS_DIR)/standards/ $(DOCS_DIR)/processes/ $(DOCS_DIR)/policies/ $(DOCS_DIR)/charter/; \
		make generate-backlinks; \
	done
