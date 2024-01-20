package internal

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
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

func GetSOC2Controls(url string) (FrameworkSummary, error) {
	frameworkSummary := FrameworkSummary{}
	getFile := true
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
	soc2Bytes, err := ioutil.ReadAll(soc2File)
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
	f, err := os.Create(fmt.Sprintf("soc2/%s.md", safeFileName(requirement.ID)))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(requirement.Name).
		PlainText(requirement.Description).
		H2("Mapped SCF controls")

	fcids := []string{}
	for scfID, controlMapping := range scfControlMapping {
		soc2FrameworkControlIDs := controlMapping["SOC 2"]
		for _, fcid := range soc2FrameworkControlIDs {
			if string(fcid) == socControlID {
				fcids = append(fcids, string(scfID))
			}
		}
	}
	doc.BulletList(fcids...)
	doc.Build()
	return nil

}
