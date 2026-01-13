package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"

	"github.com/engseclabs/graphgrc/internal/generator"
	"github.com/engseclabs/graphgrc/internal/parser"
)

func main() {
	// Parse command line flags
	repoRootFlag := flag.String("root", "", "Repository root directory (defaults to current directory)")
	verboseFlag := flag.Bool("verbose", false, "Enable verbose output")
	validateFlag := flag.Bool("validate", false, "Only validate that files have backlink sections")
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
	}

	// Define directories to scan for links
	// Note: Scan custom controls and GRC documents for links (they link upward to framework controls)
	// Also scan framework controls for any cross-framework links
	directories := []string{
		"custom",
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

	// If validate mode, just check for missing sections
	if *validateFlag {
		if *verboseFlag {
			fmt.Println("Validating backlink sections...")
		}

		missing, err := generator.ValidateBacklinkSections(repoRoot, directories)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error during validation: %v\n", err)
			os.Exit(1)
		}

		if len(missing) > 0 {
			fmt.Printf("Warning: %d files are missing '## Referenced By' section:\n", len(missing))
			for _, file := range missing {
				fmt.Printf("  - %s\n", file)
			}
			os.Exit(0)
		}

		fmt.Println("All files have backlink sections!")
		os.Exit(0)
	}

	// Step 1: Parse all markdown files to extract annotated links
	if *verboseFlag {
		fmt.Println("Scanning directories for markdown files...")
	}

	links, err := parser.ParseAllMarkdownFiles(repoRoot, directories)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing markdown files: %v\n", err)
		os.Exit(1)
	}

	if *verboseFlag {
		fmt.Printf("Found %d annotated links\n", len(links))
	}

	// Step 2: Build the backlink graph
	if *verboseFlag {
		fmt.Println("Building backlink graph...")
	}

	graph := parser.BuildBacklinkGraph(links)

	if *verboseFlag {
		graph.PrintSummary()
	}

	// Step 3: Update all files with backlinks
	if *verboseFlag {
		fmt.Println("\nUpdating files with backlinks...")
	}

	updatedCount, err := generator.UpdateAllBacklinks(repoRoot, graph)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error updating backlinks: %v\n", err)
		os.Exit(1)
	}

	// Print summary
	fmt.Printf("\nBacklink generation complete!\n")
	fmt.Printf("  Processed %d annotated links\n", len(links))
	fmt.Printf("  Updated %d files with backlinks\n", updatedCount)

	stats := graph.Stats()
	fmt.Printf("  Total files with backlinks: %d\n", stats["total_files_with_backlinks"])
	fmt.Printf("  Total backlinks generated: %d\n", stats["total_backlinks"])
}
