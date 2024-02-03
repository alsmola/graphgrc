package main

import (
	"log"

	"github.com/alsmola/compliance-mapper/internal"
)

func main() {
	// todo initialize flags
	latestScfLink := "https://github.com/securecontrolsframework/securecontrolsframework/raw/main/Secure%20Controls%20Framework%20(SCF)%20-%202023.4.xlsx"
	getFile := true
	scfControls, err := internal.ReturnSCFControls(latestScfLink, getFile)
	if err != nil {
		log.Fatal(err)
	}
	scfControlMappings := internal.GetComplianceControlMappings(scfControls)
	for scfControlID, controlMapping := range scfControlMappings {
		internal.GenerateSCFMarkdown(scfControls[scfControlID], scfControlID, controlMapping)
	}
	internal.GenerateSCFIndex(scfControlMappings, scfControls)
	soc2Link := "https://raw.githubusercontent.com/prowler-cloud/prowler/c3ecd2b3e5858b54098e179a568bc83bdbe2b82c/prowler/compliance/aws/soc2_aws.json"
	frameworkSummary, err := internal.GetSOC2Controls(soc2Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, requirement := range frameworkSummary.Requirements {
		err = internal.GenerateSOC2Markdown(requirement, scfControlMappings)
	}
	if err != nil {
		log.Fatal(err)
	}

}