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

func GetISOControls(standard Framework, isoLink string, getFile bool) (ISOFramework, error) {
	isoFramework := ISOFramework{}
	filename := fmt.Sprintf("%s.json", safeFileName(string(standard)))
	if getFile {
		resp, err := http.Get(isoLink)
		if err != nil {
			return isoFramework, err
		}
		defer resp.Body.Close()
		out, err := os.Create(filename)
		if err != nil {
			return isoFramework, err
		}
		defer out.Close()
		io.Copy(out, resp.Body)
	}
	isoFile, err := os.Open(filename)
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

func GenerateISOMarkdown(standard Framework, isoDomain ISODomain, scfControlMapping SCFControlMappings) error {
	if standard == Framework("ISO 27001") && strings.HasPrefix(isoDomain.Title, "A") {
		return nil
	}
	filename := fmt.Sprintf("%s/%s.md", safeFileName(string(standard)), safeFileName(shortenDomain(standard, isoDomain.Title)))
	f, err := os.Create(filename)
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(fmt.Sprintf("%s - %s", standard, string(isoDomain.Title)))

	for _, isoControl := range isoDomain.Controls {
		doc.H2(isoControl.Ref).
			PlainText(md.Bold(isoControl.Title) + "\n").
			PlainText(isoControl.Summary).
			LF()
		fcids := []string{}
		for scfID, controlMapping := range scfControlMapping {
			soc2FrameworkControlIDs := controlMapping[standard]
			for _, fcid := range soc2FrameworkControlIDs {
				if FCIDToAnnex(standard, string(fcid)) == isoControl.Ref {
					link := fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID)))
					found := false
					for _, f := range fcids {
						if f == link {
							found = true
						}
					}
					if !found {
						fcids = append(fcids, link)
					}
				}
			}
		}
		if len(fcids) > 0 {
			slices.Sort(fcids)
			doc.H3("Mapped SCF controls").
				BulletList(fcids...).
				LF()
		}
	}
	doc.Build()
	err = generateMetadata(filename, string(standard), isoDomain.Title, isoDomain.Title)
	if err != nil {
		return err
	}
	return nil
}

func FCIDToAnnex(framework Framework, fcid string) string {
	if framework == Framework("ISO 27002") {
		fcid = "A" + fcid
	}
	subSubRegexPattern := `^A([0-9]+)\.([0-9]+)\.([0-9]+).*`
	subSubRegex := regexp.MustCompile(subSubRegexPattern)
	subsubAnnexMatches := subSubRegex.FindStringSubmatch(fcid)
	if len(subsubAnnexMatches) > 0 {
		return fmt.Sprintf("A.%s.%s.%s", subsubAnnexMatches[1], subsubAnnexMatches[2], subsubAnnexMatches[3])
	}
	subRegexPattern := `^A([0-9]+)\.([0-9]+).*`
	subRegex := regexp.MustCompile(subRegexPattern)
	subAnnexMatches := subRegex.FindStringSubmatch(fcid)
	if len(subAnnexMatches) > 0 {
		return fmt.Sprintf("A.%s.%s", subAnnexMatches[1], subAnnexMatches[2])
	}
	if framework == Framework("ISO 27002") {
		log.Fatal("ISO 27002 not annex")
	}
	return strings.ReplaceAll(strings.ReplaceAll(fcid, ")", ""), "(", ".")
}

func FCIDToRequirement(fcid string) string {
	return strings.ReplaceAll(strings.ReplaceAll(fcid, ")", ""), "(", ".")
}

func GenerateISOIndex(standard Framework, isoFramework ISOFramework) error {
	f, err := os.Create(fmt.Sprintf("%s/index.md", safeFileName(string(standard))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(standard))
	controlLinks := []string{}
	for _, domain := range isoFramework.Domains {
		controlLinks = append(controlLinks, fmt.Sprintf("[%s](%s.md)", domain.Title, safeFileName(shortenDomain(standard, domain.Title))))
	}
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}

func shortenDomain(standard Framework, domain string) string {
	if standard == Framework("ISO 27001") {
		parts := strings.Split(domain, " -")
		return strings.ReplaceAll(parts[0], ".", "-")
	} else {
		return strings.ReplaceAll(domain[0:3], ".", "-")
	}

}
