package parser

import (
	"fmt"
	"path/filepath"
	"sort"
	"strings"
)

// BacklinkInfo represents information about a backlink to a document
type BacklinkInfo struct {
	SourceFile string // File that contains the link
	LinkText   string // Display text of the link
	Annotation string // Annotation text
}

// DocumentType represents the category of a document
type DocumentType string

const (
	TypeControls         DocumentType = "Controls"
	TypeStandards        DocumentType = "Standards"
	TypeProcesses        DocumentType = "Processes"
	TypePolicies         DocumentType = "Policies"
	TypeCharter          DocumentType = "Charter"
	TypeFrameworkControl DocumentType = "Framework Controls"
)

// BacklinkGraph maps target files to their backlinks, grouped by document type
// Structure: targetFile -> documentType -> []BacklinkInfo
type BacklinkGraph map[string]map[DocumentType][]BacklinkInfo

// BuildBacklinkGraph creates a bidirectional link graph from parsed links
func BuildBacklinkGraph(links []AnnotatedLink) BacklinkGraph {
	graph := make(BacklinkGraph)

	for _, link := range links {
		// Initialize map for target file if it doesn't exist
		if _, exists := graph[link.TargetFile]; !exists {
			graph[link.TargetFile] = make(map[DocumentType][]BacklinkInfo)
		}

		// Determine document type of source file
		docType := getDocumentType(link.SourceFile)

		// Add backlink info
		backlink := BacklinkInfo{
			SourceFile: link.SourceFile,
			LinkText:   link.LinkText,
			Annotation: link.Annotation,
		}

		graph[link.TargetFile][docType] = append(graph[link.TargetFile][docType], backlink)
	}

	// Sort backlinks within each type for consistent output
	for targetFile := range graph {
		for docType := range graph[targetFile] {
			sortBacklinks(graph[targetFile][docType])
		}
	}

	return graph
}

// getDocumentType determines the document type based on file path
func getDocumentType(filePath string) DocumentType {
	// Normalize path to use forward slashes
	filePath = filepath.ToSlash(filePath)

	// Remove leading slash and docs/ prefix for easier matching
	filePath = strings.TrimPrefix(filePath, "/")
	filePath = strings.TrimPrefix(filePath, "docs/")

	switch {
	case strings.HasPrefix(filePath, "controls/"), strings.HasPrefix(filePath, "custom/"):
		return TypeControls
	case strings.HasPrefix(filePath, "standards/"):
		return TypeStandards
	case strings.HasPrefix(filePath, "processes/"):
		return TypeProcesses
	case strings.HasPrefix(filePath, "policies/"):
		return TypePolicies
	case strings.HasPrefix(filePath, "charter/"):
		return TypeCharter
	case strings.HasPrefix(filePath, "frameworks/soc2/"),
		strings.HasPrefix(filePath, "frameworks/gdpr/"),
		strings.HasPrefix(filePath, "frameworks/iso27001/"),
		strings.HasPrefix(filePath, "frameworks/iso27002/"),
		strings.HasPrefix(filePath, "frameworks/nist80053/"),
		strings.HasPrefix(filePath, "frameworks/scf/"),
		strings.HasPrefix(filePath, "soc2/"),
		strings.HasPrefix(filePath, "gdpr/"),
		strings.HasPrefix(filePath, "iso27001/"),
		strings.HasPrefix(filePath, "iso27002/"),
		strings.HasPrefix(filePath, "nist80053/"),
		strings.HasPrefix(filePath, "scf/"):
		return TypeFrameworkControl
	default:
		// Default to Controls for unknown paths
		return TypeControls
	}
}

// sortBacklinks sorts backlinks by source file path for consistent output
func sortBacklinks(backlinks []BacklinkInfo) {
	sort.Slice(backlinks, func(i, j int) bool {
		return backlinks[i].SourceFile < backlinks[j].SourceFile
	})
}

// GetBacklinksForFile returns all backlinks for a specific file
func (g BacklinkGraph) GetBacklinksForFile(filePath string) (map[DocumentType][]BacklinkInfo, bool) {
	backlinks, exists := g[filePath]
	return backlinks, exists
}

// GetFilesWithBacklinks returns a sorted list of all files that have backlinks
func (g BacklinkGraph) GetFilesWithBacklinks() []string {
	files := make([]string, 0, len(g))
	for file := range g {
		files = append(files, file)
	}
	sort.Strings(files)
	return files
}

// Stats returns statistics about the backlink graph
func (g BacklinkGraph) Stats() map[string]int {
	stats := make(map[string]int)
	stats["total_files_with_backlinks"] = len(g)

	totalBacklinks := 0
	for _, backlinks := range g {
		for _, typeBacklinks := range backlinks {
			totalBacklinks += len(typeBacklinks)
		}
	}
	stats["total_backlinks"] = totalBacklinks

	return stats
}

// PrintSummary prints a human-readable summary of the backlink graph
func (g BacklinkGraph) PrintSummary() {
	stats := g.Stats()
	fmt.Printf("\nBacklink Graph Summary:\n")
	fmt.Printf("  Files with backlinks: %d\n", stats["total_files_with_backlinks"])
	fmt.Printf("  Total backlinks: %d\n", stats["total_backlinks"])

	// Count by document type
	typeCounts := make(map[DocumentType]int)
	for _, backlinks := range g {
		for docType, typeBacklinks := range backlinks {
			typeCounts[docType] += len(typeBacklinks)
		}
	}

	if len(typeCounts) > 0 {
		fmt.Printf("\n  Backlinks by type:\n")

		// Print in consistent order
		types := []DocumentType{
			TypeControls,
			TypeStandards,
			TypeProcesses,
			TypePolicies,
			TypeCharter,
			TypeFrameworkControl,
		}

		for _, docType := range types {
			if count, exists := typeCounts[docType]; exists && count > 0 {
				fmt.Printf("    %s: %d\n", docType, count)
			}
		}
	}
}
