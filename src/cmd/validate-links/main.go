package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

// LinkReference represents a markdown link found in a file
type LinkReference struct {
	SourceFile string
	LineNumber int
	LinkText   string
	LinkPath   string
}

// ValidationResult tracks validation results
type ValidationResult struct {
	TotalLinks    int
	BrokenLinks   []LinkReference
	ValidLinks    int
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: validate-links <directory>")
		os.Exit(1)
	}

	rootDir := os.Args[1]

	// Validate that the directory exists
	if _, err := os.Stat(rootDir); os.IsNotExist(err) {
		fmt.Printf("Error: Directory '%s' does not exist\n", rootDir)
		os.Exit(1)
	}

	fmt.Printf("Validating markdown links in: %s\n\n", rootDir)

	result := validateDirectory(rootDir)

	// Print summary
	fmt.Printf("\n=== Link Validation Summary ===\n")
	fmt.Printf("Total links found: %d\n", result.TotalLinks)
	fmt.Printf("Valid links: %d\n", result.ValidLinks)
	fmt.Printf("Broken links: %d\n", len(result.BrokenLinks))

	if len(result.BrokenLinks) > 0 {
		fmt.Printf("\n=== Broken Links ===\n")
		for _, link := range result.BrokenLinks {
			fmt.Printf("❌ %s:%d\n", link.SourceFile, link.LineNumber)
			fmt.Printf("   Link: [%s](%s)\n", link.LinkText, link.LinkPath)
			fmt.Printf("   Target does not exist: %s\n\n", link.LinkPath)
		}
		os.Exit(1)
	} else {
		fmt.Printf("\n✅ All links are valid!\n")
	}
}

func validateDirectory(rootDir string) ValidationResult {
	result := ValidationResult{
		BrokenLinks: make([]LinkReference, 0),
	}

	// Walk through all markdown files
	err := filepath.Walk(rootDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// Skip directories and non-markdown files
		if info.IsDir() || !strings.HasSuffix(path, ".md") {
			return nil
		}

		// Skip hidden directories (like .git)
		if strings.Contains(path, "/.") {
			return nil
		}

		// Extract and validate links from this file
		links := extractLinks(path)
		for _, link := range links {
			result.TotalLinks++

			// Skip external links (http://, https://, mailto:, etc.)
			if isExternalLink(link.LinkPath) {
				result.ValidLinks++
				continue
			}

			// Skip anchor-only links (#section)
			if strings.HasPrefix(link.LinkPath, "#") {
				result.ValidLinks++
				continue
			}

			// Validate the link
			if !validateLink(path, link.LinkPath, rootDir) {
				result.BrokenLinks = append(result.BrokenLinks, link)
			} else {
				result.ValidLinks++
			}
		}

		return nil
	})

	if err != nil {
		fmt.Printf("Error walking directory: %v\n", err)
		os.Exit(1)
	}

	return result
}

func extractLinks(filePath string) []LinkReference {
	links := make([]LinkReference, 0)

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("Error opening file %s: %v\n", filePath, err)
		return links
	}
	defer file.Close()

	// Regex to match markdown links: [text](path)
	linkRegex := regexp.MustCompile(`\[([^\]]+)\]\(([^\)]+)\)`)

	scanner := bufio.NewScanner(file)
	lineNumber := 0

	for scanner.Scan() {
		lineNumber++
		line := scanner.Text()

		// Find all links in this line
		matches := linkRegex.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			if len(match) >= 3 {
				linkText := match[1]
				linkPath := match[2]

				// Remove anchor from link path for file validation
				linkPathWithoutAnchor := strings.Split(linkPath, "#")[0]

				// Skip empty paths (pure anchor links)
				if linkPathWithoutAnchor == "" {
					continue
				}

				links = append(links, LinkReference{
					SourceFile: filePath,
					LineNumber: lineNumber,
					LinkText:   linkText,
					LinkPath:   linkPathWithoutAnchor,
				})
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Printf("Error reading file %s: %v\n", filePath, err)
	}

	return links
}

func isExternalLink(path string) bool {
	return strings.HasPrefix(path, "http://") ||
		strings.HasPrefix(path, "https://") ||
		strings.HasPrefix(path, "mailto:") ||
		strings.HasPrefix(path, "ftp://")
}

func validateLink(sourceFile, linkPath, rootDir string) bool {
	// Get the directory of the source file
	sourceDir := filepath.Dir(sourceFile)

	// Resolve the absolute path
	var targetPath string
	if filepath.IsAbs(linkPath) {
		targetPath = filepath.Join(rootDir, linkPath)
	} else {
		targetPath = filepath.Join(sourceDir, linkPath)
	}

	// Clean the path to resolve .. and .
	targetPath = filepath.Clean(targetPath)

	// Check if the target exists (file or directory)
	_, err := os.Stat(targetPath)
	return err == nil
}
