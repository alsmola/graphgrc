package internal

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func safeFileName(input string) string {
	output := input
	removeCharacters := []string{".", "_", " ", "(", ")"}
	for _, c := range removeCharacters {
		output = strings.ReplaceAll(output, c, "")
	}
	return strings.ToLower(output)
}

func generateMetadata(filename, framework, controlID, controlTitle, controlSummary string) error {
	type MetadataAttributes struct {
		Framework string `json:"framework"`
		ID        string `json:"id"`
		Title     string `json:"title"`
		Summary   string `json:"summary"`
	}
	type ControlMetadata struct {
		Attributes MetadataAttributes `json:"metadataAttributes"`
	}
	attributes := MetadataAttributes{
		Framework: framework,
		ID:        controlID,
		Title:     controlTitle,
		Summary:   controlSummary,
	}
	jsonData, err := json.MarshalIndent(ControlMetadata{attributes}, "", "    ")
	if err != nil {
		return err
	}
	file, err := os.Create(fmt.Sprintf("%s.metadata.json", filename))
	if err != nil {
		return err
	}
	defer file.Close()
	_, err = file.Write(jsonData)
	if err != nil {
		return err
	}
	return nil
}
