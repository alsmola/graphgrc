package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"

	"github.com/alsmola/graphgrc/internal/generator"
)

func main() {
	// Parse command line flags
	repoRootFlag := flag.String("root", "", "Repository root directory (defaults to current directory)")
	dryRunFlag := flag.Bool("dry-run", false, "Show what would be done without making changes")
	flag.Parse()

	// Determine repository root
	repoRoot := *repoRootFlag
	if repoRoot == "" {
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

	fmt.Printf("Repository root: %s\n", repoRoot)

	// Define directories to process
	directories := []string{
		"standards",
		"processes",
		"policies",
		"charter",
		"soc2",
		"gdpr",
		"iso27001",
		"iso27002",
		"nist80053",
		"scf",
	}

	addedCount := 0
	skippedCount := 0

	for _, dir := range directories {
		fullDir := filepath.Join(repoRoot, dir)

		// Check if directory exists
		if _, err := os.Stat(fullDir); os.IsNotExist(err) {
			fmt.Printf("Directory %s does not exist, skipping\n", dir)
			continue
		}

		fmt.Printf("\nProcessing directory: %s\n", dir)

		// Walk the directory
		err := filepath.Walk(fullDir, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			// Only process .md files
			if info.IsDir() || filepath.Ext(info.Name()) != ".md" {
				return nil
			}

			// Check if file already has the section
			content, err := os.ReadFile(path)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Warning: failed to read %s: %v\n", path, err)
				return nil
			}

			if string(content) == "" || len(content) == 0 {
				fmt.Fprintf(os.Stderr, "Warning: %s is empty, skipping\n", path)
				skippedCount++
				return nil
			}

			// Check if already has section
			if generator.HasBacklinkSection(string(content)) {
				skippedCount++
				return nil
			}

			// Add the section
			if *dryRunFlag {
				fmt.Printf("  Would add section to: %s\n", path)
			} else {
				err = generator.EnsureBacklinkSection(path)
				if err != nil {
					fmt.Fprintf(os.Stderr, "Warning: failed to update %s: %v\n", path, err)
					return nil
				}
				fmt.Printf("  Added section to: %s\n", path)
			}

			addedCount++
			return nil
		})

		if err != nil {
			fmt.Fprintf(os.Stderr, "Error walking directory %s: %v\n", fullDir, err)
		}
	}

	// Print summary
	fmt.Printf("\n")
	if *dryRunFlag {
		fmt.Printf("Dry run complete:\n")
		fmt.Printf("  Would add section to %d files\n", addedCount)
	} else {
		fmt.Printf("Complete:\n")
		fmt.Printf("  Added section to %d files\n", addedCount)
	}
	fmt.Printf("  Skipped %d files (already have section or empty)\n", skippedCount)
}
