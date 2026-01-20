package parser

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

// AnnotatedLink represents a parsed link with annotation from markdown
type AnnotatedLink struct {
	SourceFile string // Absolute path from repo root (e.g., "/custom/acc-01.md")
	TargetFile string // Absolute path from repo root (e.g., "/standards/aws-security-standard.md")
	LinkText   string // Display text of the link
	Annotation string // Text inside ^[...]
	LineNumber int    // Line number where link was found
}

// linkPattern matches: [text](path.md) ^[annotation]
var linkPattern = regexp.MustCompile(`\[([^\]]+)\]\(([^)]+\.md)\)\s*\^\[([^\]]+)\]`)

// dashLinkPattern matches: - [text](path.md) - annotation
var dashLinkPattern = regexp.MustCompile(`^-\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*-\s*(.+)$`)

// ParseMarkdownLinks extracts all annotated links from a markdown file
// Excludes links in the "## Referenced By" and "## Satisfies Framework Controls" sections to avoid parsing backlinks
func ParseMarkdownLinks(filePath string, repoRoot string) ([]AnnotatedLink, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("failed to open file %s: %w", filePath, err)
	}
	defer file.Close()

	var links []AnnotatedLink
	scanner := bufio.NewScanner(file)
	lineNumber := 0
	inReferencedBySection := false
	inFrameworkMappingsSection := false
	skipDashLinks := false

	// Convert filePath to absolute path from repo root
	sourceFile, err := normalizeToRepoPath(filePath, repoRoot)
	if err != nil {
		return nil, fmt.Errorf("failed to normalize source path: %w", err)
	}

	// Check if this is a custom control file - if so, skip dash-formatted links in Framework Mappings
	isCustomControl := strings.HasPrefix(sourceFile, "/custom/")

	for scanner.Scan() {
		lineNumber++
		line := scanner.Text()

		// Check if we've entered the Referenced By or Implemented By section
		if strings.Contains(line, "## Referenced By") || strings.Contains(line, "## Implemented By") {
			inReferencedBySection = true
			continue
		}

		// Check if we've entered a Framework Mapping section (only in custom controls)
		if isCustomControl && strings.Contains(line, "## Framework Mapping") {
			inFrameworkMappingsSection = true
			skipDashLinks = true
			continue
		}

		// Check if we've entered a Control Mapping section (in standards/processes/policies)
		if !isCustomControl && strings.Contains(line, "## Control Mapping") {
			// Don't skip - we want to parse links FROM standards TO controls
			continue
		}

		// Exit section when we hit a different ## heading
		if inFrameworkMappingsSection && strings.HasPrefix(strings.TrimSpace(line), "##") && !strings.Contains(line, "## Framework Mapping") {
			inFrameworkMappingsSection = false
			skipDashLinks = false
		}

		// Skip links in the Referenced By section
		if inReferencedBySection {
			continue
		}

		// Find all matches in the line (can have multiple links per line)
		// Try the ^[annotation] pattern first
		matches := linkPattern.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			if len(match) != 4 {
				continue
			}

			linkText := strings.TrimSpace(match[1])
			relativePath := strings.TrimSpace(match[2])
			annotation := strings.TrimSpace(match[3])

			// Resolve relative path to absolute path from repo root
			targetFile, err := resolveRelativePath(filePath, relativePath, repoRoot)
			if err != nil {
				// Don't fail on individual link resolution errors, just skip
				fmt.Fprintf(os.Stderr, "Warning: failed to resolve path %s from %s: %v\n",
					relativePath, filePath, err)
				continue
			}

			links = append(links, AnnotatedLink{
				SourceFile: sourceFile,
				TargetFile: targetFile,
				LinkText:   linkText,
				Annotation: annotation,
				LineNumber: lineNumber,
			})
		}

		// Also try the dash-separated pattern: - [text](path.md) - annotation
		// Skip dash links if we're in the Framework Mappings section of a custom control
		if !skipDashLinks {
			if dashMatch := dashLinkPattern.FindStringSubmatch(line); dashMatch != nil && len(dashMatch) == 4 {
				linkText := strings.TrimSpace(dashMatch[1])
				relativePath := strings.TrimSpace(dashMatch[2])
				annotation := strings.TrimSpace(dashMatch[3])

				// Resolve relative path to absolute path from repo root
				targetFile, err := resolveRelativePath(filePath, relativePath, repoRoot)
				if err != nil {
					// Don't fail on individual link resolution errors, just skip
					fmt.Fprintf(os.Stderr, "Warning: failed to resolve path %s from %s: %v\n",
						relativePath, filePath, err)
					continue
				}

				links = append(links, AnnotatedLink{
					SourceFile: sourceFile,
					TargetFile: targetFile,
					LinkText:   linkText,
					Annotation: annotation,
					LineNumber: lineNumber,
				})
			}
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("error reading file %s: %w", filePath, err)
	}

	return links, nil
}

// ParseAllMarkdownFiles scans directories and parses all markdown files
func ParseAllMarkdownFiles(repoRoot string, directories []string) ([]AnnotatedLink, error) {
	var allLinks []AnnotatedLink

	for _, dir := range directories {
		fullDir := filepath.Join(repoRoot, dir)

		// Check if directory exists
		if _, err := os.Stat(fullDir); os.IsNotExist(err) {
			fmt.Fprintf(os.Stderr, "Warning: directory %s does not exist, skipping\n", fullDir)
			continue
		}

		// Walk the directory
		err := filepath.Walk(fullDir, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			// Only process .md files
			if !info.IsDir() && strings.HasSuffix(info.Name(), ".md") {
				links, err := ParseMarkdownLinks(path, repoRoot)
				if err != nil {
					// Log error but continue processing other files
					fmt.Fprintf(os.Stderr, "Warning: failed to parse %s: %v\n", path, err)
					return nil
				}
				allLinks = append(allLinks, links...)
			}

			return nil
		})

		if err != nil {
			return nil, fmt.Errorf("error walking directory %s: %w", fullDir, err)
		}
	}

	return allLinks, nil
}

// resolveRelativePath converts a relative link path to an absolute path from repo root
// Example: from /custom/acc-01.md, link ../standards/aws.md -> /standards/aws.md
func resolveRelativePath(sourceFilePath, relativePath, repoRoot string) (string, error) {
	// Get directory of source file
	sourceDir := filepath.Dir(sourceFilePath)

	// Join with relative path and clean
	absolutePath := filepath.Join(sourceDir, relativePath)
	absolutePath = filepath.Clean(absolutePath)

	// Convert to repo-relative path
	return normalizeToRepoPath(absolutePath, repoRoot)
}

// normalizeToRepoPath converts an absolute filesystem path to a path relative to repo root
// with a leading slash (e.g., "/custom/acc-01.md")
func normalizeToRepoPath(absolutePath, repoRoot string) (string, error) {
	// Clean both paths
	absolutePath = filepath.Clean(absolutePath)
	repoRoot = filepath.Clean(repoRoot)

	// Get relative path from repo root
	relPath, err := filepath.Rel(repoRoot, absolutePath)
	if err != nil {
		return "", fmt.Errorf("failed to get relative path: %w", err)
	}

	// Add leading slash and convert to forward slashes (for consistency)
	return "/" + filepath.ToSlash(relPath), nil
}
