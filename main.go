package main

import (
	"flag"
	"log"

	"github.com/alsmola/graphgrc/internal"
)

func main() {
	// CLI flags
	mode := flag.String("mode", "custom", "Control framework mode: custom or scf")
	getFile := flag.Bool("fetch", false, "Fetch fresh data from remote sources")
	flag.Parse()

	// Conditional execution based on mode
	if *mode == "scf" {
		runSCFMode(*getFile)
	} else if *mode == "custom" {
		runCustomMode(*getFile)
	} else {
		log.Fatalf("Invalid mode: %s. Use 'custom' or 'scf'", *mode)
	}
}

func runSCFMode(getFile bool) {
	log.Println("Running in SCF mode...")

	latestScfLink := "https://github.com/securecontrolsframework/securecontrolsframework/raw/main/Secure%20Controls%20Framework%20(SCF)%20-%202023.4.xlsx"
	scfControls, err := internal.ReturnSCFControls(latestScfLink, getFile)
	if err != nil {
		log.Fatal(err)
	}
	scfControlMappings := internal.GetComplianceControlMappings(scfControls)
	for scfControlID, controlMapping := range scfControlMappings {
		internal.GenerateSCFMarkdown(scfControls[scfControlID], scfControlID, controlMapping)
	}
	internal.GenerateSCFIndex(scfControlMappings, scfControls)

	soc2Link := "https://raw.githubusercontent.com/prowler-cloud/prowler/main/prowler/compliance/aws/soc2_aws.json"
	soc2Framework, err := internal.GetSOC2Controls(soc2Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, requirement := range soc2Framework.Requirements {
		err = internal.GenerateSOC2Markdown(requirement, scfControlMappings)
		if err != nil {
			log.Fatal(err)
		}
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
			if err != nil {
				log.Fatal(err)
			}
		}

	}
	internal.GenerateGDPRIndex(gdprFramework)

	iso27001 := internal.Framework("ISO 27001")
	iso27002 := internal.Framework("ISO 27002")

	iso27001Link := "https://raw.githubusercontent.com/JupiterOne/security-policy-templates/main/templates/standards/iso-iec-27001-2022.json"
	iso27001Framework, err := internal.GetISOControls(iso27001, iso27001Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, domain := range iso27001Framework.Domains {
		err = internal.GenerateISOMarkdown(iso27001, domain, scfControlMappings)
		if err != nil {
			log.Fatal(err)
		}
	}
	internal.GenerateISOIndex(iso27001, iso27001Framework)

	iso27002Link := "https://raw.githubusercontent.com/JupiterOne/security-policy-templates/main/templates/standards/iso-27002-2022.json"
	iso27002Framework, err := internal.GetISOControls(iso27002, iso27002Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, domain := range iso27002Framework.Domains {
		err = internal.GenerateISOMarkdown(iso27002, domain, scfControlMappings)
		if err != nil {
			log.Fatal(err)
		}
	}
	internal.GenerateISOIndex(iso27002, iso27002Framework)

	nist80053Link := "https://raw.githubusercontent.com/GSA/fedramp-automation/master/dist/content/rev5/baselines/json/FedRAMP_rev5_MODERATE-baseline-resolved-profile_catalog.json"
	nist80053Framework, err := internal.GetNIST80053Controls(nist80053Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, family := range nist80053Framework.Families {
		for _, control := range family.Controls {
			err = internal.GenerateNIST80053Markdown(control, scfControlMappings)
			if err != nil {
				log.Fatal(err)
			}
			for _, subcontrol := range control.Controls {
				err = internal.GenerateNIST80053Markdown(subcontrol, scfControlMappings)
				if err != nil {
					log.Fatal(err)
				}
			}

		}
	}
	internal.GenerateNIST80053Index(nist80053Framework)

	log.Println("SCF mode complete!")
}

func runCustomMode(getFile bool) {
	log.Println("Running in Custom mode...")

	// 1. Load custom controls (like loading SCF)
	customControls, err := internal.LoadCustomControls("custom_controls.json")
	if err != nil {
		log.Fatal(err)
	}

	// 2. Extract mappings (like GetComplianceControlMappings for SCF)
	customControlMappings := internal.GetCustomControlMappings(customControls)

	// 3. Generate custom control markdown (like SCF markdown generation)
	for scfControlID, controlMapping := range customControlMappings {
		// Convert SCFControlID back to CustomControlID for lookup
		customControlID := internal.CustomControlID(scfControlID)
		err := internal.GenerateCustomControlMarkdown(
			customControls.Controls[customControlID],
			customControlID,
			controlMapping,
		)
		if err != nil {
			log.Fatal(err)
		}
	}
	err = internal.GenerateCustomControlIndex(customControlMappings, customControls)
	if err != nil {
		log.Fatal(err)
	}

	// 4. SOC 2 with custom control mappings (SAME CODE as SCF mode)
	soc2Link := "https://raw.githubusercontent.com/prowler-cloud/prowler/main/prowler/compliance/aws/soc2_aws.json"
	soc2Framework, err := internal.GetSOC2Controls(soc2Link, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, requirement := range soc2Framework.Requirements {
		err = internal.GenerateSOC2Markdown(requirement, customControlMappings)
		if err != nil {
			log.Fatal(err)
		}
	}
	internal.GenerateSOC2Index(soc2Framework)

	// 5. GDPR with custom control mappings (SAME CODE as SCF mode)
	gdprLink := "https://raw.githubusercontent.com/enterpriseready/enterpriseready/master/content/gdpr/gdpr-abridged.md"
	gdprFramework, err := internal.GetGDPRControls(gdprLink, getFile)
	if err != nil {
		log.Fatal(err)
	}
	for _, article := range gdprFramework {
		if article.Title != "" {
			err = internal.GenerateGDPRMarkdown(article, customControlMappings)
			if err != nil {
				log.Fatal(err)
			}
		}
	}
	internal.GenerateGDPRIndex(gdprFramework)

	log.Println("Custom mode complete!")
}
