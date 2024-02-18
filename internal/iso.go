package internal

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"

	md "github.com/go-spectest/markdown"
)

type ISOFramework []ISOAnnex
type ISOAnnex struct {
	ID         string        `json:"id"`
	Title      string        `json:"title"`
	Body       string        `json:"body"`
	Subannexes []ISOSubannex `json:"subannexes"`
}
type ISOSubannex struct {
	ID            string           `json:"id"`
	Body          string           `json:"body"`
	Subsubannexes []ISOSubsubannex `json:"subsubannexes"`
}

type ISOSubsubannex struct {
	ID    string `json:"id"`
	Title string `json:"title"`
	Body  string `json:"body"`
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
		isoTextFile, err := os.Open("iso.txt")
		if err != nil {
			log.Fatal(err)
		}
		defer isoTextFile.Close()

		scanner := bufio.NewScanner(isoTextFile)
		annexID := -1
		subAnnexID := -1
		subsubAnnexID := -1
		for scanner.Scan() {
			line := scanner.Text()
			regexPattern := `^A.([0-9]+)\s`
			regex := regexp.MustCompile(regexPattern)
			annexMatches := regex.FindStringSubmatch(line)
			if len(annexMatches) > 0 {
				annexIDMatch, err := strconv.Atoi(annexMatches[1])
				if err != nil {
					log.Fatal("Bad ISO annex ID", annexMatches[1])
				}
				annexID = annexIDMatch - 1
				fmt.Printf("A%d\n", annexID+1)
				for len(isoFramework) < annexID {
					isoFramework = append(isoFramework, ISOAnnex{
						ID:         fmt.Sprintf("Annex %d", len(isoFramework)),
						Subannexes: []ISOSubannex{},
					})
				}
				annex := ISOAnnex{
					ID:         fmt.Sprintf("Annex %d", annexID+1),
					Subannexes: []ISOSubannex{},
					Title:      line,
				}
				isoFramework = append(isoFramework, annex)
				subAnnexID = -1
			} else {
				annex := isoFramework[annexID]
				subRegexPattern := `^A\.[0-9]+\.([0-9]+)\s`
				subRegex := regexp.MustCompile(subRegexPattern)
				subAnnexMatches := subRegex.FindStringSubmatch(line)
				if len(subAnnexMatches) > 0 {
					subAnnexIDMatch, err := strconv.Atoi(subAnnexMatches[1])
					if err != nil {
						log.Fatal("Bad subannex ID", subAnnexMatches[1])
					}
					subAnnexID = subAnnexIDMatch - 1
					fmt.Printf("A%d.%d\n", annexID+1, subAnnexID+1)
					if len(annex.Subannexes) != subAnnexID {
						subAnnexID = len(annex.Subannexes)
					}
					// body := strings.ReplaceAll(line, fmt.Sprintf("%s. ", strconv.Itoa(subAnnexID+1)), "")
					subannex := ISOSubannex{
						ID:   fmt.Sprintf("A%d.%d", annexID+1, subAnnexID+1),
						Body: line,
					}
					annex.Subannexes = append(annex.Subannexes, subannex)
					subsubAnnexID = -1
				} else {
					subSubRegexPattern := `^A\.[0-9]+\.[0-9]+\.([0-9]+)\s`
					subSubRegex := regexp.MustCompile(subSubRegexPattern)
					subsubAnnexMatches := subSubRegex.FindStringSubmatch(line)
					if len(subsubAnnexMatches) > 0 {
						subsubAnnexIDMatch, err := strconv.Atoi(subsubAnnexMatches[1])
						if err != nil {
							log.Fatal("Bad subsubannex ID", subsubAnnexMatches[1])
						}
						subsubAnnexID = subsubAnnexIDMatch - 1
						fmt.Printf("A%d.%d.%d\n", annexID+1, subAnnexID+1, subsubAnnexID+1)
						parts := strings.Split(line, " - ")

						subsubAnnex := ISOSubsubannex{
							ID:    fmt.Sprintf("A%d.%d.%d", annexID+1, subAnnexID+1, subsubAnnexID+1),
							Title: parts[0],
							Body:  parts[1],
						}
						annex.Subannexes[subAnnexID].Subsubannexes = append(annex.Subannexes[subAnnexID].Subsubannexes, subsubAnnex)
					} else {
						annex.Subannexes[subAnnexID].Body = annex.Subannexes[subAnnexID].Body + "\n" + line
					}
				}
				isoFramework[annexID] = annex
			}
		}
		file, err := json.MarshalIndent(isoFramework, "", " ")
		if err != nil {
			return isoFramework, err
		}
		err = os.WriteFile("iso.json", file, 0644)
		if err != nil {
			return isoFramework, err
		}
	}
	isoFile, err := os.Open("iso.json")
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

func GenerateISOMarkdown(isoAnnex ISOAnnex, scfControlMapping SCFControlMappings) error {
	// scfAnnex := strings.ReplaceAll(isoAnnex.ID, "Annex", "Art")
	scfAnnex := isoAnnex.ID
	f, err := os.Create(fmt.Sprintf("iso/%s.md", safeFileName(strings.ReplaceAll(scfAnnex, ".", "-"))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(isoAnnex.ID)).
		H2(isoAnnex.Title).
		PlainText(isoAnnex.Body)

	for _, isoSubAnnex := range isoAnnex.Subannexes {
		scfSubAnnex := isoSubAnnex.ID
		doc.H2(isoSubAnnex.Body)
		fcids := []string{}
		for scfID, controlMapping := range scfControlMapping {
			soc2FrameworkControlIDs := controlMapping["ISO 27001"]
			for _, fcid := range soc2FrameworkControlIDs {
				log.Println(fcidToAnnex(string(fcid)), scfSubAnnex)
				if fcidToAnnex(string(fcid)) == scfSubAnnex {
					fcids = append(fcids, fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID))))
				}
			}
		}
		if len(fcids) > 0 {
			slices.Sort(fcids)
			doc.H3("Mapped SCF controls").
				BulletList(fcids...)
		}
		for _, isoSubsubAnnex := range isoSubAnnex.Subsubannexes {
			scfSubsubAnnex := fcidToAnnex(isoSubsubAnnex.ID)
			doc.H3(isoSubsubAnnex.Title).
				PlainText(isoSubsubAnnex.Body)
			subfcids := []string{}
			for scfID, controlMapping := range scfControlMapping {
				soc2FrameworkControlIDs := controlMapping["ISO 27001"]
				for _, fcid := range soc2FrameworkControlIDs {
					if fcidToAnnex(string(fcid)) == scfSubsubAnnex {
						subfcids = append(subfcids, fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID))))
					}
				}
			}
			if len(subfcids) > 0 {
				slices.Sort(subfcids)
				doc.H4("Mapped SCF controls").
					BulletList(subfcids...)
			}
		}

	}
	doc.Build()
	return nil
}

func fcidToAnnex(fcid string) string {
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
		return fmt.Sprintf("A%s.%s", subAnnexMatches[1], subAnnexMatches[2])
	}
	log.Fatal("Could not parse FCID", fcid)
	return fcid
}

func GenerateISOIndex(isoFramework ISOFramework) error {
	f, err := os.Create("iso/index.md")
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1("ISO")
	controlLinks := []string{}
	for _, annex := range isoFramework {
		if annex.Title != "" {
			link := annex.ID
			controlLinks = append(controlLinks, fmt.Sprintf("[%s - %s](%s.md)", annex.ID, annex.Title, safeFileName(link)))
		}
	}
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}
