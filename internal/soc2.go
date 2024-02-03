package internal

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"slices"
	"strings"

	md "github.com/go-spectest/markdown"
)

type Requirement struct {
	ID          string `json:"Id"`
	Name        string `json:"Name"`
	Description string `json:"Description"`
	Attributes  []struct {
		ItemID  string `json:"ItemId"`
		Section string `json:"Section"`
		Service string `json:"Service"`
		Type    string `json:"Type"`
	} `json:"Attributes"`
}

type FrameworkSummary struct {
	Framework    string        `json:"Framework"`
	Version      string        `json:"Version"`
	Provider     string        `json:"Provider"`
	Description  string        `json:"Description"`
	Requirements []Requirement `json:"Requirements"`
}

func GetSOC2Controls(url string, getFile bool) (FrameworkSummary, error) {
	frameworkSummary := FrameworkSummary{}
	if getFile {
		resp, err := http.Get(url)
		if err != nil {
			return frameworkSummary, err
		}
		defer resp.Body.Close()
		out, err := os.Create("soc2.json")
		if err != nil {
			return frameworkSummary, err
		}
		defer out.Close()
		io.Copy(out, resp.Body)
	}
	soc2File, err := os.Open("soc2.json")
	defer soc2File.Close()
	soc2Bytes, err := io.ReadAll(soc2File)
	if err != nil {
		return frameworkSummary, err
	}
	if err := json.Unmarshal(soc2Bytes, &frameworkSummary); err != nil {
		return frameworkSummary, err
	}
	return frameworkSummary, nil
}

// Thanks ChatGPT
func getFirstWord(input string) string {
	words := strings.Fields(input)
	if len(words) > 0 {
		return words[0]
	}
	return ""
}

func GenerateSOC2Markdown(requirement Requirement, scfControlMapping SCFControlMappings) error {
	socControlID := getFirstWord(requirement.Name)
	id := strings.ReplaceAll(requirement.ID, "cc_a", "a")
	id = strings.ReplaceAll(id, "cc_c", "c")
	f, err := os.Create(fmt.Sprintf("soc2/%s.md", safeFileName(id)))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(requirement.Name)

	descriptions := parseSOC2Description(requirement.Description)
	for heading, content := range descriptions {
		if heading == "" {
			doc.PlainText(content)
		} else {
			doc.H2(heading).PlainText(content)
		}

	}

	doc.H2("Mapped SCF controls")
	fcids := []string{}
	for scfID, controlMapping := range scfControlMapping {
		soc2FrameworkControlIDs := controlMapping["SOC 2"]
		for _, fcid := range soc2FrameworkControlIDs {
			if string(fcid) == socControlID {
				fcids = append(fcids, fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID))))
			}
		}
	}
	slices.Sort(fcids)
	doc.BulletList(fcids...)
	doc.Build()
	return nil
}

func parseSOC2Description(description string) map[string]string {
	descriptions := map[string]string{}
	sentences := strings.Split(description, ". ")
	lastHeader := ""
	for _, sentence := range sentences {
		if strings.Contains(sentence, " - ") {
			parts := strings.Split(sentence, " - ")
			descriptions[parts[0]] = parts[1]
			lastHeader = parts[0]

		} else {
			descriptions[lastHeader] = fmt.Sprintf("%s. %s.", descriptions[lastHeader], sentence)
		}
	}
	return descriptions
}