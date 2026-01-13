package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// Parse command line flags
	repoRootFlag := flag.String("root", "", "Repository root directory (defaults to current directory)")
	verboseFlag := flag.Bool("verbose", false, "Enable verbose output")
	dryRunFlag := flag.Bool("dry-run", false, "Show what would be removed without making changes")
	flag.Parse()

	// Determine repository root
	repoRoot := *repoRootFlag
	if repoRoot == "" {
		// Use current directory as default
		var err error
		repoRoot, err = os.Getwd()
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: failed to get current directory: %v\n", err)
			os.Exit(1)
		}
	}

	// Ensure the path is absolute
	repoRoot, err := filepath.Abs(repoRoot)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: failed to resolve repository root: %v\n", err)
		os.Exit(1)
	}

	if *verboseFlag {
		fmt.Printf("Repository root: %s\n", repoRoot)
		if *dryRunFlag {
			fmt.Println("Running in DRY RUN mode - no files will be modified")
		}
	}

	// Framework directories that need cleanup
	frameworkDirs := []string{
		"soc2",
		"gdpr",
		"iso27001",
		"iso27002",
		"nist80053",
		"scf",
	}

	totalFiles := 0
	totalCleaned := 0

	// Process each framework directory
	for _, dir := range frameworkDirs {
		fullDir := filepath.Join(repoRoot, dir)

		// Check if directory exists
		if _, err := os.Stat(fullDir); os.IsNotExist(err) {
			if *verboseFlag {
				fmt.Printf("Skipping %s (directory does not exist)\n", dir)
			}
			continue
		}

		if *verboseFlag {
			fmt.Printf("\nProcessing %s/...\n", dir)
		}

		// Walk the directory
		err := filepath.Walk(fullDir, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			// Only process .md files (skip index files)
			if !info.IsDir() && strings.HasSuffix(info.Name(), ".md") && info.Name() != "index.md" {
				totalFiles++

				cleaned, err := cleanupFrameworkControl(path, *dryRunFlag, *verboseFlag)
				if err != nil {
					fmt.Fprintf(os.Stderr, "Error processing %s: %v\n", path, err)
					return nil // Continue with other files
				}

				if cleaned {
					totalCleaned++
				}
			}

			return nil
		})

		if err != nil {
			fmt.Fprintf(os.Stderr, "Error walking directory %s: %v\n", fullDir, err)
		}
	}

	// Print summary
	fmt.Printf("\nCleanup complete!\n")
	fmt.Printf("  Files processed: %d\n", totalFiles)
	fmt.Printf("  Files cleaned: %d\n", totalCleaned)

	if *dryRunFlag {
		fmt.Println("\nThis was a DRY RUN - no files were modified")
		fmt.Println("Run without --dry-run to apply changes")
	}
}

// cleanupFrameworkControl removes old main.go generated sections from a framework control file
func cleanupFrameworkControl(filePath string, dryRun bool, verbose bool) (bool, error) {
	// Read the file
	content, err := os.ReadFile(filePath)
	if err != nil {
		return false, fmt.Errorf("failed to read file: %w", err)
	}

	fileContent := string(content)

	// Check if file has the old "Mapped custom controls" section (can be ## or ###)
	if !strings.Contains(fileContent, "Mapped custom controls") {
		return false, nil // Nothing to clean
	}

	// Parse the file and remove all "### Mapped custom controls" sections
	newContent := removeOldMappedSections(fileContent)

	// Check if anything changed
	if newContent == fileContent {
		return false, nil
	}

	if verbose {
		relPath := filepath.Base(filePath)
		if dryRun {
			fmt.Printf("  [DRY RUN] Would clean: %s\n", relPath)
		} else {
			fmt.Printf("  Cleaning: %s\n", relPath)
		}
	}

	// Write back to file (unless dry run)
	if !dryRun {
		err = os.WriteFile(filePath, []byte(newContent), 0644)
		if err != nil {
			return false, fmt.Errorf("failed to write file: %w", err)
		}
	}

	return true, nil
}

// removeOldMappedSections removes all "Mapped custom controls" sections (## or ###) and their content
func removeOldMappedSections(content string) string {
	lines := strings.Split(content, "\n")
	var result []string
	inMappedSection := false
	lastWasEmpty := false

	for i, line := range lines {
		trimmed := strings.TrimSpace(line)

		// Check if this is the start of a "Mapped custom controls" section (## or ###)
		if trimmed == "## Mapped custom controls" || trimmed == "### Mapped custom controls" {
			inMappedSection = true
			// Don't add this line
			continue
		}

		// If we're in a mapped section, skip lines until we hit a separator or another section
		if inMappedSection {
			// Check if this is the end of the section (empty line followed by ## or ---)
			if trimmed == "" {
				// Look ahead to see if next non-empty line is a section header or separator
				nextIsSection := false
				for j := i + 1; j < len(lines); j++ {
					nextTrimmed := strings.TrimSpace(lines[j])
					if nextTrimmed == "" {
						continue
					}
					if strings.HasPrefix(nextTrimmed, "##") || nextTrimmed == "---" {
						nextIsSection = true
					}
					break
				}

				if nextIsSection {
					inMappedSection = false
					// Don't add excess empty lines
					continue
				}
			}
			// Skip this line (it's part of the mapped section)
			continue
		}

		// Not in a mapped section, keep the line
		// But avoid adding multiple consecutive empty lines
		if trimmed == "" {
			if lastWasEmpty {
				continue
			}
			lastWasEmpty = true
		} else {
			lastWasEmpty = false
		}

		result = append(result, line)
	}

	// Clean up trailing whitespace
	output := strings.Join(result, "\n")
	output = strings.TrimRight(output, "\n") + "\n"

	return output
}
