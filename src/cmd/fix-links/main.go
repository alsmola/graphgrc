package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: fix-links <directory>")
		os.Exit(1)
	}

	rootDir := os.Args[1]

	fmt.Printf("Fixing markdown links in: %s\n\n", rootDir)

	fixedFiles := 0
	fixedLinks := 0

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

		// Fix links in this file
		fixed, count := fixLinksInFile(path, rootDir)
		if fixed {
			fixedFiles++
			fixedLinks += count
			fmt.Printf("✓ Fixed %d links in: %s\n", count, path)
		}

		return nil
	})

	if err != nil {
		fmt.Printf("Error walking directory: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("\n=== Fix Summary ===\n")
	fmt.Printf("Files fixed: %d\n", fixedFiles)
	fmt.Printf("Links fixed: %d\n", fixedLinks)
}

func fixLinksInFile(filePath, rootDir string) (bool, int) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Printf("Error reading file %s: %v\n", filePath, err)
		return false, 0
	}

	originalContent := string(content)
	updatedContent := originalContent
	fixCount := 0

	// Regex to match markdown links: [text](path)
	linkRegex := regexp.MustCompile(`\[([^\]]+)\]\(([^\)]+)\)`)

	updatedContent = linkRegex.ReplaceAllStringFunc(updatedContent, func(match string) string {
		// Extract the link parts
		parts := linkRegex.FindStringSubmatch(match)
		if len(parts) < 3 {
			return match
		}

		linkText := parts[1]
		linkPath := parts[2]

		// Skip external links
		if isExternalLink(linkPath) {
			return match
		}

		// Skip anchor-only links
		if strings.HasPrefix(linkPath, "#") {
			return match
		}

		// Try to fix the link
		fixedPath := fixLinkPath(filePath, linkPath, rootDir)
		if fixedPath != linkPath {
			fixCount++
			return fmt.Sprintf("[%s](%s)", linkText, fixedPath)
		}

		return match
	})

	// Only write if we made changes
	if updatedContent != originalContent {
		err = os.WriteFile(filePath, []byte(updatedContent), 0644)
		if err != nil {
			fmt.Printf("Error writing file %s: %v\n", filePath, err)
			return false, 0
		}
		return true, fixCount
	}

	return false, 0
}

func fixLinkPath(sourceFile, linkPath, rootDir string) string {
	// Separate anchor from path
	parts := strings.Split(linkPath, "#")
	pathPart := parts[0]
	anchor := ""
	if len(parts) > 1 {
		anchor = "#" + parts[1]
	}

	// Get source directory
	sourceDir := filepath.Dir(sourceFile)

	// Calculate the target path
	var targetPath string
	if filepath.IsAbs(pathPart) {
		targetPath = filepath.Join(rootDir, pathPart)
	} else {
		targetPath = filepath.Join(sourceDir, pathPart)
	}
	targetPath = filepath.Clean(targetPath)

	// If the target already exists, no fix needed
	if _, err := os.Stat(targetPath); err == nil {
		return linkPath
	}

	// Try to find the file in known locations
	basename := filepath.Base(pathPart)

	// Check if it's a framework file (SOC 2, GDPR, etc.)
	fixedPath := tryFixFrameworkLink(sourceFile, basename, rootDir)
	if fixedPath != "" {
		return fixedPath + anchor
	}

	// No fix found
	return linkPath
}

func tryFixFrameworkLink(sourceFile, filename, rootDir string) string {
	sourceDir := filepath.Dir(sourceFile)

	// Determine which framework based on filename pattern
	var frameworkPaths []string

	if strings.HasPrefix(filename, "cc") || strings.HasPrefix(filename, "a1") || strings.HasPrefix(filename, "a2") {
		// SOC 2 control
		frameworkPaths = []string{
			"frameworks/soc2/" + filename,
		}
	} else if strings.HasPrefix(filename, "art") {
		// GDPR article
		frameworkPaths = []string{
			"frameworks/gdpr/" + filename,
		}
	} else if strings.Contains(filename, "iso") || strings.HasPrefix(filename, "a-") || isISONumericControl(filename) {
		// ISO control (can be a-5.md or just 5.md for ISO 27001)
		frameworkPaths = []string{
			"frameworks/iso27001/" + filename,
			"frameworks/iso27002/" + filename,
		}
	} else if strings.Contains(filename, "nist") || isNISTControl(filename) {
		// NIST control (ac-2.md, ia-2-1.md, etc.)
		frameworkPaths = []string{
			"frameworks/nist80053/" + filename,
		}
	} else if isCustomControl(filename) {
		// Custom control (acc-01.md, dat-01.md, etc.)
		frameworkPaths = []string{
			"custom/" + filename,
		}
	} else if isSCFControl(filename) {
		// SCF control - need to find the full filename
		scfMatch := findSCFControl(rootDir, filename)
		if scfMatch != "" {
			frameworkPaths = []string{scfMatch}
		}
	}

	// Special case for directory links
	if filename == "soc2/" || filename == "soc2" {
		frameworkPaths = []string{"frameworks/soc2/"}
	} else if filename == "gdpr/" || filename == "gdpr" {
		frameworkPaths = []string{"frameworks/gdpr/"}
	}

	// Try each possible path
	for _, relPath := range frameworkPaths {
		// Calculate the absolute path
		absPath := filepath.Join(rootDir, relPath)

		// Check if it exists
		if _, err := os.Stat(absPath); err == nil {
			// Calculate relative path from source file to target
			relFromSource, err := filepath.Rel(sourceDir, absPath)
			if err == nil {
				return relFromSource
			}
		}
	}

	return ""
}

func isCustomControl(filename string) bool {
	// Custom controls follow pattern: acc-01.md, dat-02.md, etc.
	pattern := regexp.MustCompile(`^[a-z]{3}-\d{2}\.md$`)
	return pattern.MatchString(filename)
}

func isSCFControl(filename string) bool {
	// SCF controls follow pattern: gov-01.md, iac-01.md, etc.
	// But they can have longer names like gov-01-something.md
	pattern := regexp.MustCompile(`^[a-z]{3}-\d`)
	return pattern.MatchString(filename)
}

func isISONumericControl(filename string) bool {
	// ISO 27001 numeric controls: 4.md, 5.md, 6.md, 7.md, 8.md, 9.md, 10.md
	pattern := regexp.MustCompile(`^\d+\.md$`)
	return pattern.MatchString(filename)
}

func isNISTControl(filename string) bool {
	// NIST controls follow pattern: ac-2.md, ia-2-1.md, si-3.md, etc.
	pattern := regexp.MustCompile(`^[a-z]{2}-\d+(-\d+)?\.md$`)
	return pattern.MatchString(filename)
}

func findSCFControl(rootDir, shortName string) string {
	// Extract the control ID prefix (e.g., "gov-01" from "gov-01.md")
	prefix := strings.TrimSuffix(shortName, ".md")

	// Look in the SCF directory for a file that starts with this prefix
	scfDir := filepath.Join(rootDir, "frameworks/scf")

	entries, err := os.ReadDir(scfDir)
	if err != nil {
		return ""
	}

	for _, entry := range entries {
		if !entry.IsDir() && strings.HasSuffix(entry.Name(), ".md") {
			// Check if this file starts with our prefix
			if strings.HasPrefix(entry.Name(), prefix) {
				return "frameworks/scf/" + entry.Name()
			}
		}
	}

	return ""
}

func isExternalLink(path string) bool {
	return strings.HasPrefix(path, "http://") ||
		strings.HasPrefix(path, "https://") ||
		strings.HasPrefix(path, "mailto:") ||
		strings.HasPrefix(path, "ftp://")
}
