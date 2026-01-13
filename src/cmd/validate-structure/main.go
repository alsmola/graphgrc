package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type ValidationResult struct {
	FilePath string
	Issues   []string
}

func main() {
	repoRootFlag := flag.String("root", "", "Repository root directory (defaults to current directory)")
	verboseFlag := flag.Bool("verbose", false, "Enable verbose output")
	flag.Parse()

	repoRoot := *repoRootFlag
	if repoRoot == "" {
		var err error
		repoRoot, err = os.Getwd()
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: failed to get current directory: %v\n", err)
			os.Exit(1)
		}
	}

	repoRoot, err := filepath.Abs(repoRoot)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: failed to resolve repository root: %v\n", err)
		os.Exit(1)
	}

	if *verboseFlag {
		fmt.Printf("Repository root: %s\n\n", repoRoot)
	}

	var allResults []ValidationResult

	// Validate custom controls
	fmt.Println("Validating custom controls...")
	customResults := validateCustomControls(repoRoot)
	allResults = append(allResults, customResults...)

	// Validate standards
	fmt.Println("Validating standards...")
	standardsResults := validateGRCDocs(repoRoot, "standards")
	allResults = append(allResults, standardsResults...)

	// Validate processes
	fmt.Println("Validating processes...")
	processResults := validateGRCDocs(repoRoot, "processes")
	allResults = append(allResults, processResults...)

	// Validate policies
	fmt.Println("Validating policies...")
	policyResults := validateGRCDocs(repoRoot, "policies")
	allResults = append(allResults, policyResults...)

	// Validate charter
	fmt.Println("Validating charter...")
	charterResults := validateGRCDocs(repoRoot, "charter")
	allResults = append(allResults, charterResults...)

	// Print results
	fmt.Println("\n" + strings.Repeat("=", 80))
	fmt.Println("VALIDATION RESULTS")
	fmt.Println(strings.Repeat("=", 80))

	issueCount := 0
	for _, result := range allResults {
		if len(result.Issues) > 0 {
			issueCount += len(result.Issues)
			fmt.Printf("\n%s:\n", result.FilePath)
			for _, issue := range result.Issues {
				fmt.Printf("  ❌ %s\n", issue)
			}
		}
	}

	if issueCount == 0 {
		fmt.Println("\n✅ All files are properly structured!")
	} else {
		fmt.Printf("\n❌ Found %d issues across %d files\n", issueCount, len(allResults))
		os.Exit(1)
	}
}

func validateCustomControls(repoRoot string) []ValidationResult {
	var results []ValidationResult
	customDir := filepath.Join(repoRoot, "custom")

	filepath.Walk(customDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() || !strings.HasSuffix(info.Name(), ".md") || info.Name() == "index.md" {
			return nil
		}

		content, err := os.ReadFile(path)
		if err != nil {
			return nil
		}

		fileContent := string(content)
		relPath, _ := filepath.Rel(repoRoot, path)

		var issues []string

		// Check for required sections
		if !strings.Contains(fileContent, "## Framework Mapping") {
			issues = append(issues, "Missing '## Framework Mapping' section")
		}

		if !strings.Contains(fileContent, "## Referenced By") {
			issues = append(issues, "Missing '## Referenced By' section")
		}

		// Check for YAML frontmatter
		if !strings.HasPrefix(fileContent, "---\n") {
			issues = append(issues, "Missing YAML frontmatter")
		}

		// Check for required frontmatter fields
		requiredFields := []string{"id:", "title:", "category:", "owner:"}
		for _, field := range requiredFields {
			if !strings.Contains(fileContent, field) {
				issues = append(issues, fmt.Sprintf("Missing frontmatter field: %s", field))
			}
		}

		if len(issues) > 0 {
			results = append(results, ValidationResult{
				FilePath: relPath,
				Issues:   issues,
			})
		}

		return nil
	})

	return results
}

func validateGRCDocs(repoRoot string, dirName string) []ValidationResult {
	var results []ValidationResult
	dir := filepath.Join(repoRoot, dirName)

	if _, err := os.Stat(dir); os.IsNotExist(err) {
		return results
	}

	filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() || !strings.HasSuffix(info.Name(), ".md") || info.Name() == "index.md" {
			return nil
		}

		content, err := os.ReadFile(path)
		if err != nil {
			return nil
		}

		fileContent := string(content)
		relPath, _ := filepath.Rel(repoRoot, path)

		var issues []string

		// Check for required sections
		if !strings.Contains(fileContent, "## Control Mapping") {
			issues = append(issues, "Missing '## Control Mapping' section")
		}

		// Standards/processes/policies/charter should NOT have Referenced By sections
		// They only link TO controls, not receive backlinks

		// Check for YAML frontmatter
		if !strings.HasPrefix(fileContent, "---\n") {
			issues = append(issues, "Missing YAML frontmatter")
		}

		if len(issues) > 0 {
			results = append(results, ValidationResult{
				FilePath: relPath,
				Issues:   issues,
			})
		}

		return nil
	})

	return results
}
