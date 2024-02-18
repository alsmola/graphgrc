package internal

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"regexp"
	"slices"
	"strings"

	md "github.com/go-spectest/markdown"
)

type ISOControl struct {
	Ref     string `json:"ref"`
	Title   string `json:"title"`
	Summary string `json:"summary"`
}

type ISODomain struct {
	Title    string       `json:"title"`
	Controls []ISOControl `json:"controls"`
}
type ISOFramework struct {
	Domains []ISODomain `json:"domains"`
}

func GetISOControls(isoLink string, getFile bool) (ISOFramework, error) {
	isoFramework := ISOFramework{}
	if getFile {
		resp, err := http.Get(isoLink)
		if err != nil {
			return isoFramework, err
		}
		defer resp.Body.Close()
		out, err := os.Create("iso27001.json")
		if err != nil {
			return isoFramework, err
		}
		defer out.Close()
		io.Copy(out, resp.Body)
	}
	isoFile, err := os.Open("iso27001.json")
	if err != nil {
		return isoFramework, err
	}
	defer isoFile.Close()
	isoBytes, err := io.ReadAll(isoFile)
	if err != nil {
		return isoFramework, err
	}
	if err := json.Unmarshal(isoBytes, &isoFramework); err != nil {
		return isoFramework, err
	}
	return isoFramework, nil
}

func GenerateISOMarkdown(isoDomain ISODomain, scfControlMapping SCFControlMappings) error {
	// scfAnnex := strings.ReplaceAll(isoAnnex.ID, "Annex", "Art")
	f, err := os.Create(fmt.Sprintf("iso27001/%s.md", safeFileName(shortenDomain(isoDomain.Title))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(isoDomain.Title))

	for _, isoControl := range isoDomain.Controls {
		scfSubAnnex := isoControl.Ref
		doc.H2(isoControl.Ref).
			PlainText(md.Bold(isoControl.Title) + "\n").
			PlainText(isoControl.Summary)
		fcids := []string{}
		alreadyAdded := []string{}
		for scfID, controlMapping := range scfControlMapping {
			soc2FrameworkControlIDs := controlMapping["ISO 27001"]
			for _, fcid := range soc2FrameworkControlIDs {
				if FCIDToAnnex(string(fcid)) == scfSubAnnex {
					found := false
					for _, a := range alreadyAdded {
						if a == scfSubAnnex {
							found = true
						}
					}
					if !found {
						alreadyAdded = append(alreadyAdded, scfSubAnnex)
						fcids = append(fcids, fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID))))
					}
				}
			}
		}
		if len(fcids) > 0 {
			slices.Sort(fcids)
			doc.H3("Mapped SCF controls").
				BulletList(fcids...)
		}
	}
	doc.Build()
	return nil
}

func FCIDToAnnex(fcid string) string {
	subSubRegexPattern := `^A?([0-9]+)\.([0-9]+)\.([0-9]+).*`
	subSubRegex := regexp.MustCompile(subSubRegexPattern)
	subsubAnnexMatches := subSubRegex.FindStringSubmatch(fcid)
	if len(subsubAnnexMatches) > 0 {
		return fmt.Sprintf("A%s.%s.%s", subsubAnnexMatches[1], subsubAnnexMatches[2], subsubAnnexMatches[3])
	}
	subRegexPattern := `^([0-9]+)\.([0-9]+).*`
	subRegex := regexp.MustCompile(subRegexPattern)
	subAnnexMatches := subRegex.FindStringSubmatch(fcid)
	if len(subAnnexMatches) > 0 {
		return fmt.Sprintf("A.%s.%s", subAnnexMatches[1], subAnnexMatches[2])
	}
	log.Fatal("Could not parse FCID", fcid)
	return fcid
}

func GenerateISOIndex(isoFramework ISOFramework) error {
	f, err := os.Create("iso27001/index.md")
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1("ISO 27001")
	controlLinks := []string{}
	for _, domain := range isoFramework.Domains {
		controlLinks = append(controlLinks, fmt.Sprintf("[%s](%s.md)", domain.Title, safeFileName(shortenDomain(domain.Title))))
	}
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}

func shortenDomain(domain string) string {
	return strings.ReplaceAll(domain[0:3], ".", "-")
}
