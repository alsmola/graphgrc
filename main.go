package main

import (
	"log"

	"github.com/alsmola/compliance-mapper/internal"
)

func main() {
	// todo initialize flags
	latestScfLink := "https://github.com/securecontrolsframework/securecontrolsframework/raw/main/Secure%20Controls%20Framework%20(SCF)%20-%202023.4.xlsx"
	getFile := false
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
	soc2Framework, err := internal.GetSOC2Controls(soc2Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, requirement := range soc2Framework.Requirements {
		err = internal.GenerateSOC2Markdown(requirement, scfControlMappings)
	}
	if err != nil {
		log.Fatal(err)
	}
	internal.GenerateSOC2Index(soc2Framework)
	gdprLink := "https://raw.githubusercontent.com/enterpriseready/enterpriseready/master/content/gdpr/gdpr-abridged.md"
	gdprFramework, err := internal.GetGDPRControls(gdprLink, true)
	if err != nil {
		log.Fatal(err)
	}
	for _, article := range gdprFramework {
		if article.Title != "" {
			err = internal.GenerateGDPRMarkdown(article, scfControlMappings)
		}
	}
	if err != nil {
		log.Fatal(err)
	}
	internal.GenerateGDPRIndex(gdprFramework)
}
