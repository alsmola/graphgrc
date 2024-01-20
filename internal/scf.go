package internal

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"slices"
	"strings"

	md "github.com/go-spectest/markdown"

	"github.com/xuri/excelize/v2"
)

type ControlHeader string
type ControlValue string
type Framework string
type FrameworkControlID string
type SCFControlID string

type Control map[ControlHeader]ControlValue
type SCFControls map[SCFControlID]Control

type ControlMapping map[Framework][]FrameworkControlID

func (c ControlMapping) MapsToControls() bool {
	for _, mappings := range c {
		if len(mappings) > 0 {
			return true
		}
	}
	return false
}

type SCFControlMappings map[SCFControlID]ControlMapping

const Description = "Description"
const ComplianceMethods = "Compliance Methods"
const ControlQuestions = "Control Questions"
const NotPerformed = "Not Performed"
const PerformedInternally = "Performed Informally"
const PlannedAndTracked = "Planned & Tracked"
const WellDefined = "Well Defined"
const QuantitativelyControlled = "Quantitatively Controlled"
const ContinuouslyImproving = "Continuously Improving"

var SCFColumnMapping = map[string]ControlHeader{
	Description:              "Secure Controls Framework (SCF) Control Description",
	ControlQuestions:         "SCF Control Question",
	NotPerformed:             "SP-CMM 0 Not Performed",
	PerformedInternally:      "SP-CMM 1 Performed Informally",
	PlannedAndTracked:        "SP-CMM 2 Planned & Tracked",
	WellDefined:              "SP-CMM 3 Well Defined",
	QuantitativelyControlled: "SP-CMM 4 Quantitatively Controlled",
	ContinuouslyImproving:    "SP-CMM 5 Continuously Improving",
}

var SupportedFrameworks = map[Framework]ControlHeader{
	"SOC 2": "AICPA TSC 2017 (Controls)",
	// "ISO 27001":   "ISO 27001 v2022",
	// "ISO 27002":   "ISO 27002 v2022",
	// "ISO 27701":   "ISO 27701 v2019",
	// "NIST 800-53": "NIST 800-53 rev5 (moderate)",
	// "HIPAA":       "US HIPAA",
}

func ReturnSCFControls(url string, getFile bool) (SCFControls, error) {
	controls := map[SCFControlID]Control{}
	if getFile {
		resp, err := http.Get(url)
		if err != nil {
			return nil, err
		}
		defer resp.Body.Close()
		out, err := os.Create("scf.xlsx")
		if err != nil {
			return nil, err
		}
		defer out.Close()
		io.Copy(out, resp.Body)
	}

	f, err := excelize.OpenFile("scf.xlsx")
	if err != nil {
		return nil, err
	}
	defer func() {
		if err := f.Close(); err != nil {
			log.Println(err)
		}
	}()
	rows, err := f.GetRows("SCF 2023.4")
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	headers := []ControlHeader{}
	for idx, row := range rows {
		if idx == 0 {
			for _, header := range row {
				headers = append(headers, ControlHeader(strings.ReplaceAll(header, "\n", " ")))
			}
		} else {
			scfControlID := fmt.Sprintf("%s - %s", row[2], strings.TrimSpace(strings.ReplaceAll(row[1], "\n", " ")))
			control := Control{}
			for idx, val := range row {
				control[headers[idx]] = ControlValue(strings.ReplaceAll(val, "▪", "-"))
			}
			controls[SCFControlID(scfControlID)] = control
		}
	}
	return controls, nil
}

func GenerateSCFMarkdown(scfControl Control, scfControlID SCFControlID, controlMapping ControlMapping) error {
	f, err := os.Create(fmt.Sprintf("scf/%s.md", safeFileName(string(scfControlID))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(scfControlID)).
		PlainText(string(scfControl[SCFColumnMapping[Description]])).
		H2("Mapped framework controls")

	for framework, frameworkControlIDs := range controlMapping {
		fcids := []string{}
		for _, fcid := range frameworkControlIDs {
			fcids = append(fcids, string(fcid))
		}
		slices.Sort(fcids)
		doc.H3(string(framework)).
			BulletList(fcids...)
	}
	doc.Build()
	return nil
}

func GetComplianceControlMappings(controls SCFControls) SCFControlMappings {
	controlMappings := map[SCFControlID]ControlMapping{}
	for controlID, control := range controls {
		controlMapping := ControlMapping{}
		for framework, header := range SupportedFrameworks {
			fcids := strings.Split(string(control[header]), "\n")
			frameworkControlIDs := []FrameworkControlID{}
			for _, fcid := range fcids {
				frameworkControlIDs = append(frameworkControlIDs, FrameworkControlID(fcid))
			}
			controlMapping[framework] = frameworkControlIDs
			if len(controlMapping[framework]) == 1 && controlMapping[framework][0] == "" {
				controlMapping[framework] = []FrameworkControlID{}
			}
		}
		if controlMapping.MapsToControls() {
			controlMappings[controlID] = controlMapping
		}
	}
	return controlMappings
}

func GenerateSCFIndex(scfControls SCFControls) error {
	f, err := os.Create("scf/index.md")
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1("SCF Controls")
	controlLinks := []string{}
	for scfControlID, _ := range scfControls {
		controlLinks = append(controlLinks, fmt.Sprintf("[%s](scr/%s.md)", scfControlID, safeFileName(string(scfControlID))))
	}
	slices.Sort(controlLinks)
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}

var BadCharacters = []string{
	"../",
	"<!--",
	"-->",
	"<",
	">",
	"'",
	"\"",
	"/",
	"&",
	"$",
	"#",
	"{", "}", "[", "]", "=",
	";", "?", "%20", "%22",
	"%3c", // <
	"%253",
}
