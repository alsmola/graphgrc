package internal

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"regexp"
	"slices"
	"sort"
	"strings"

	md "github.com/go-spectest/markdown"
)

type GDPRArticleID string
type GDPRSubarticleID string
type GDPRFramework map[GDPRArticleID]GDPRArticle
type GDPRArticle struct {
	Title       string                      `json:"title"`
	Body        string                      `json:"body"`
	Subarticles map[GDPRSubarticleID]string `json:"subarticles"`
}

// type GDPRControlLink struct {
// 	name string
// 	link string
// }

func GetGDPRControls(url string, getFile bool) (GDPRFramework, error) {
	gdprFramework := GDPRFramework{}
	// file, err := os.Open("gdpr-articles.txt")
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// defer file.Close()
	// scanner := bufio.NewScanner(file)
	// for scanner.Scan() {
	// 	link := scanner.Text()
	// 	linkName := strings.ReplaceAll(strings.ReplaceAll(strings.ReplaceAll(link, "https://gdpr.eu/", ""), "/", ""), "-", " ")
	// 	regexPattern := `article\s[0-9]+`
	// 	regex := regexp.MustCompile(regexPattern)
	// 	articleMatches := regex.FindStringSubmatch(linkName)
	// 	caser := cases.Title(language.English)
	// 	article := caser.String(articleMatches[0])
	// 	name := caser.String(strings.ReplaceAll(linkName, articleMatches[0]+" ", ""))
	// 	gdprControls[MakeSCFControlID(article)] = GDPRControlLink{
	// 		name: name,
	// 		link: link,
	// 	}
	// }
	// if err := scanner.Err(); err != nil {
	// 	log.Fatal(err)
	// }
	// gdpfFramework := GDPRFramework{}
	if getFile {
		resp, err := http.Get(url)
		if err != nil {
			return gdprFramework, err
		}
		scanner := bufio.NewScanner(resp.Body)
		articleID := GDPRArticleID("")
		subArticleID := GDPRSubarticleID("")
		for scanner.Scan() {
			line := strings.ReplaceAll(scanner.Text(), "### ", "")
			if line == "" {
				continue
			}
			regexPattern := `^Article\s[0-9]+`
			regex := regexp.MustCompile(regexPattern)
			articleMatches := regex.FindStringSubmatch(line)
			if len(articleMatches) > 0 {
				fmt.Println("New article", line)
				articleID = GDPRArticleID(articleMatches[0])
				gdprFramework[articleID] = GDPRArticle{
					Subarticles: map[GDPRSubarticleID]string{},
				}
				subArticleID = GDPRSubarticleID("")
			} else if articleID != GDPRArticleID("") {
				article := gdprFramework[articleID]
				if article.Title == "" {
					fmt.Println("Article title", line)
					article.Title = line
				} else {
					regexPattern := `^[0-9]+\.`
					regex := regexp.MustCompile(regexPattern)
					subArticleMatches := regex.FindStringSubmatch(line)
					if len(subArticleMatches) > 0 {
						fmt.Println("Article subtitle", line)
						subArticleNumber := subArticleMatches[0]
						subArticleID = GDPRSubarticleID(fmt.Sprintf("%s.%s", articleID, strings.ReplaceAll(subArticleNumber, ".", "")))
						article.Subarticles[subArticleID] = strings.ReplaceAll(line, subArticleNumber, "")
					} else {
						if subArticleID == GDPRSubarticleID("") {
							if article.Body == "" {
								article.Body = line
							} else {
								article.Body = "\n" + line
							}
						} else {
							article.Subarticles[subArticleID] = article.Subarticles[subArticleID] + "\n" + line
						}
					}
				}
				gdprFramework[articleID] = article
			}
		}
		defer resp.Body.Close()
		file, err := json.MarshalIndent(gdprFramework, "", " ")
		if err != nil {
			return gdprFramework, err
		}
		err = os.WriteFile("gdpr.json", file, 0644)
		if err != nil {
			return gdprFramework, err
		}
	}
	gdprFile, err := os.Open("gdpr.json")
	if err != nil {
		return gdprFramework, err
	}
	defer gdprFile.Close()
	gdprBytes, err := io.ReadAll(gdprFile)
	if err != nil {
		return gdprFramework, err
	}
	if err := json.Unmarshal(gdprBytes, &gdprFramework); err != nil {
		return gdprFramework, err
	}
	return gdprFramework, nil
}

func GenerateGDPRMarkdown(gdprArticle GDPRArticle, gdprArticleID GDPRArticleID, scfControlMapping SCFControlMappings) error {
	scfArticle := strings.ReplaceAll(string(gdprArticleID), "Article", "Art")
	f, err := os.Create(fmt.Sprintf("gdpr/%s.md", safeFileName(strings.ReplaceAll(scfArticle, ".", "-"))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(gdprArticleID)).
		H2(gdprArticle.Title).
		PlainText(gdprArticle.Body)

	gdprSubarticleIDs := []string{}
	for gdprSubArticleID := range gdprArticle.Subarticles {
		gdprSubarticleIDs = append(gdprSubarticleIDs, string(gdprSubArticleID))
	}
	sort.Strings(gdprSubarticleIDs)
	for _, gdprSubArticleID := range gdprSubarticleIDs {
		scfSubArticle := strings.ReplaceAll(string(gdprSubArticleID), "Article", "Art")
		gdprSubArticle := gdprArticle.Subarticles[GDPRSubarticleID(gdprSubArticleID)]
		doc.H2(string(gdprSubArticleID)).
			PlainText(gdprSubArticle)
		fcids := []string{}
		for scfID, controlMapping := range scfControlMapping {
			soc2FrameworkControlIDs := controlMapping["GDPR"]
			for _, fcid := range soc2FrameworkControlIDs {
				if string(fcid) == scfSubArticle {
					fcids = append(fcids, fmt.Sprintf("[%s](../scf/%s.md)", string(scfID), safeFileName(string(scfID))))
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
