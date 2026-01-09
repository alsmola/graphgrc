package internal

import (
	"encoding/json"
	"fmt"
	"os"
	"slices"

	md "github.com/go-spectest/markdown"
)

type CustomControlID string

type CustomControl struct {
	ID             string              `json:"id"`
	Category       string              `json:"category"`
	Title          string              `json:"title"`
	Description    string              `json:"description"`
	Objective      string              `json:"objective"`
	Implementation []string            `json:"implementation"`
	Examples       []string            `json:"examples"`
	AuditEvidence  []string            `json:"audit_evidence"`
	Mappings       map[Framework][]FrameworkControlID `json:"mappings"`
}

type FrameworkMetadata struct {
	Name               string `json:"name"`
	Version            string `json:"version"`
	OrganizationProfile string `json:"organization_profile"`
	LastUpdated        string `json:"last_updated"`
}

type CustomControlFramework struct {
	Metadata FrameworkMetadata                  `json:"metadata"`
	Controls map[CustomControlID]CustomControl  `json:"controls"`
}

// CustomControlMappings is the same type as SCFControlMappings for compatibility
// with SOC2/GDPR generation functions
type CustomControlMappings = SCFControlMappings

// LoadCustomControls loads the custom control framework from JSON file
func LoadCustomControls(path string) (CustomControlFramework, error) {
	var framework CustomControlFramework

	data, err := os.ReadFile(path)
	if err != nil {
		return framework, fmt.Errorf("failed to read custom controls file: %w", err)
	}

	if err := json.Unmarshal(data, &framework); err != nil {
		return framework, fmt.Errorf("failed to parse custom controls JSON: %w", err)
	}

	return framework, nil
}

// GetCustomControlMappings builds control mappings from custom controls
// This mirrors GetComplianceControlMappings() for SCF to ensure compatibility
// Returns SCFControlMappings type so it works with existing SOC2/GDPR functions
func GetCustomControlMappings(framework CustomControlFramework) CustomControlMappings {
	controlMappings := make(CustomControlMappings)

	for controlID, control := range framework.Controls {
		controlMapping := ControlMapping{}

		// Extract mappings from control
		for fwName, frameworkControlIDs := range control.Mappings {
			controlMapping[fwName] = frameworkControlIDs
		}

		// Only include controls that have mappings
		if controlMapping.MapsToControls() {
			// Cast CustomControlID to SCFControlID to match type signature
			controlMappings[SCFControlID(string(controlID))] = controlMapping
		}
	}

	return controlMappings
}

// GenerateCustomControlMarkdown generates markdown for a custom control
// This mirrors GenerateSCFMarkdown() structure
func GenerateCustomControlMarkdown(
	control CustomControl,
	controlID CustomControlID,
	controlMapping ControlMapping,
) error {
	f, err := os.Create(fmt.Sprintf("custom/%s.md", safeFileName(string(controlID))))
	if err != nil {
		return err
	}
	defer f.Close()

	doc := md.NewMarkdown(f).
		H1(fmt.Sprintf("%s: %s", controlID, control.Title)).
		LF().
		PlainText(md.Bold("Category: ") + control.Category).
		LF().
		H2("Objective").
		PlainText(control.Objective).
		LF().
		H2("Description").
		PlainText(control.Description).
		LF()

	// Implementation guidance
	if len(control.Implementation) > 0 {
		doc.H2("Implementation Guidance")
		for _, impl := range control.Implementation {
			doc.PlainText(impl).LF()
		}
		doc.LF()
	}

	// Examples
	if len(control.Examples) > 0 {
		doc.H2("Examples of Good Implementation")
		doc.BulletList(control.Examples...)
		doc.LF()
	}

	// Audit evidence
	if len(control.AuditEvidence) > 0 {
		doc.H2("Audit Evidence")
		doc.BulletList(control.AuditEvidence...)
		doc.LF()
	}

	// Add horizontal rule before framework mappings
	doc.PlainText("---").LF()

	// Framework mappings (similar to how SCF shows mapped frameworks)
	doc.H2("Mapped framework controls")

	orderedFrameworks := []string{}
	for framework := range controlMapping {
		orderedFrameworks = append(orderedFrameworks, string(framework))
	}
	slices.Sort(orderedFrameworks)

	for _, framework := range orderedFrameworks {
		frameworkControlIDs := controlMapping[Framework(framework)]
		fcids := []string{}
		for _, fcid := range frameworkControlIDs {
			link := fmt.Sprintf("[%s](../%s/%s.md)", string(fcid), safeFileName(string(framework)), safeFileName(string(fcid)))

			// Handle special link formats for different frameworks (same as SCF)
			if framework == "GDPR" {
				// Basic link for now - can enhance with article subarticle logic if needed
				link = fmt.Sprintf("[%s](../%s/%s.md)", string(fcid), safeFileName(string(framework)), safeFileName(string(fcid)))
			} else if framework == "SOC 2" {
				// SOC 2 IDs like CC6.1 need to be converted for file names
				id := string(fcid)
				link = fmt.Sprintf("[%s](../soc2/%s.md)", id, safeFileName(id))
			}

			fcids = append(fcids, link)
		}

		if len(fcids) > 0 {
			slices.Sort(fcids)
			doc.H3(string(framework)).
				BulletList(fcids...).
				LF()
		}
	}

	doc.Build()
	return nil
}

// GenerateCustomControlIndex generates index page for custom controls
// This mirrors GenerateSCFIndex() structure but groups by category instead of family
func GenerateCustomControlIndex(controlMappings CustomControlMappings, controls CustomControlFramework) error {
	f, err := os.Create("custom/index.md")
	if err != nil {
		return err
	}
	defer f.Close()

	doc := md.NewMarkdown(f).
		H1(controls.Metadata.Name).
		PlainText(fmt.Sprintf("**Version:** %s", controls.Metadata.Version)).
		PlainText(fmt.Sprintf("**Organization Profile:** %s", controls.Metadata.OrganizationProfile)).
		PlainText(fmt.Sprintf("**Last Updated:** %s", controls.Metadata.LastUpdated)).
		LF()

	// Group controls by category
	categoryControls := make(map[string][]string)
	categories := []string{}

	for controlID := range controlMappings {
		control := controls.Controls[CustomControlID(controlID)]
		category := control.Category

		if _, exists := categoryControls[category]; !exists {
			categories = append(categories, category)
			categoryControls[category] = []string{}
		}

		categoryControls[category] = append(categoryControls[category], string(controlID))
	}

	slices.Sort(categories)

	for _, category := range categories {
		controlIDs := categoryControls[category]
		slices.Sort(controlIDs)

		doc.H2(category)

		controlLinks := []string{}
		for _, controlID := range controlIDs {
			control := controls.Controls[CustomControlID(controlID)]
			link := fmt.Sprintf("[%s - %s](%s.md)", controlID, control.Title, safeFileName(controlID))
			controlLinks = append(controlLinks, link)
		}

		doc.BulletList(controlLinks...)
	}

	doc.Build()
	return nil
}
