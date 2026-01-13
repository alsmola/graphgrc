package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	repoRootFlag := flag.String("root", "", "Repository root directory (defaults to current directory)")
	verboseFlag := flag.Bool("verbose", false, "Enable verbose output")
	dryRunFlag := flag.Bool("dry-run", false, "Show what would be added without making changes")
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
		fmt.Printf("Repository root: %s\n", repoRoot)
		if *dryRunFlag {
			fmt.Println("Running in DRY RUN mode - no files will be modified")
		}
	}

	// Directories that should have "## Satisfies Controls" section
	dirs := []string{
		"standards",
		"processes",
		"policies",
		"charter",
	}

	totalFiles := 0
	totalUpdated := 0

	for _, dir := range dirs {
		fullDir := filepath.Join(repoRoot, dir)

		if _, err := os.Stat(fullDir); os.IsNotExist(err) {
			if *verboseFlag {
				fmt.Printf("Skipping %s (directory does not exist)\n", dir)
			}
			continue
		}

		if *verboseFlag {
			fmt.Printf("\nProcessing %s/...\n", dir)
		}

		err := filepath.Walk(fullDir, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			if !info.IsDir() && strings.HasSuffix(info.Name(), ".md") {
				totalFiles++

				updated, err := addSatisfiesSection(path, *dryRunFlag, *verboseFlag)
				if err != nil {
					fmt.Fprintf(os.Stderr, "Error processing %s: %v\n", path, err)
					return nil
				}

				if updated {
					totalUpdated++
				}
			}

			return nil
		})

		if err != nil {
			fmt.Fprintf(os.Stderr, "Error walking directory %s: %v\n", fullDir, err)
		}
	}

	fmt.Printf("\nCompleted!\n")
	fmt.Printf("  Files processed: %d\n", totalFiles)
	fmt.Printf("  Files updated: %d\n", totalUpdated)

	if *dryRunFlag {
		fmt.Println("\nThis was a DRY RUN - no files were modified")
		fmt.Println("Run without --dry-run to apply changes")
	}
}

func addSatisfiesSection(filePath string, dryRun bool, verbose bool) (bool, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return false, fmt.Errorf("failed to read file: %w", err)
	}

	fileContent := string(content)

	// Check if section already exists
	if strings.Contains(fileContent, "## Satisfies Controls") {
		return false, nil // Already has section
	}

	// Find the --- separator before "## Referenced By"
	lines := strings.Split(fileContent, "\n")
	var result []string
	inserted := false

	for i, line := range lines {
		// Look for the --- separator that comes before ## Referenced By
		if strings.TrimSpace(line) == "---" {
			// Check if next non-empty line contains "## Referenced By"
			foundReferencedBy := false
			for j := i + 1; j < len(lines) && j < i+5; j++ {
				if strings.Contains(lines[j], "## Referenced By") {
					foundReferencedBy = true
					break
				}
			}

			if foundReferencedBy && !inserted {
				// Insert the new section before the ---
				result = append(result, "## Satisfies Controls")
				result = append(result, "")
				result = append(result, "<!-- This section is used to generate backlinks from custom controls to this standard/process/policy. -->")
				result = append(result, "<!-- Add links to custom controls using the format: [Control Name](../custom/control-id.md) ^[annotation] -->")
				result = append(result, "")
				result = append(result, line)
				inserted = true
				continue
			}
		}

		result = append(result, line)
	}

	if !inserted {
		// If we didn't find the right place, don't modify
		return false, nil
	}

	newContent := strings.Join(result, "\n")

	if verbose {
		relPath := filepath.Base(filePath)
		if dryRun {
			fmt.Printf("  [DRY RUN] Would add section to: %s\n", relPath)
		} else {
			fmt.Printf("  Adding section to: %s\n", relPath)
		}
	}

	if !dryRun {
		err = os.WriteFile(filePath, []byte(newContent), 0644)
		if err != nil {
			return false, fmt.Errorf("failed to write file: %w", err)
		}
	}

	return true, nil
}
