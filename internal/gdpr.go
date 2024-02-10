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

type GDPRFramework []GDPRArticle
type GDPRArticle struct {
	ID          string           `json:"id"`
	Title       string           `json:"title"`
	Body        string           `json:"body"`
	Subarticles []GDPRSubarticle `json:"subarticles"`
}
type GDPRSubarticle struct {
	ID   string `json:"id"`
	Body string `json:"body"`
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
		articleID := -1
		subArticleID := -1
		for scanner.Scan() {
			line := strings.ReplaceAll(scanner.Text(), "### ", "")
			if line == "" {
				continue
			}
			regexPattern := `^Article\s([0-9]+)$`
			regex := regexp.MustCompile(regexPattern)
			articleMatches := regex.FindStringSubmatch(line)
			if len(articleMatches) > 0 {
				articleID, err := strconv.Atoi(articleMatches[1])
				if err != nil {
					log.Fatal("Bad GDPR article ID", articleMatches[1])
				}
				for len(gdprFramework) < articleID-1 {
					gdprFramework = append(gdprFramework, GDPRArticle{
						ID:          fmt.Sprintf("Article. %s", len(gdprFramework)),
						Subarticles: []GDPRSubarticle{},
					})
				}
				article := GDPRArticle{
					ID:          fmt.Sprintf("Article. %s", articleMatches[0]),
					Subarticles: []GDPRSubarticle{},
				}
				gdprFramework = append(gdprFramework, article)
				subArticleID = 0
			} else if articleID != -1 {
				article := gdprFramework[articleID]
				if article.Title == "" {
					article.Title = line
				} else {
					regexPattern := `^([0-9]+)\.`
					regex := regexp.MustCompile(regexPattern)
					subArticleMatches := regex.FindStringSubmatch(line)
					if len(subArticleMatches) > 0 {
						subArticleID, err := strconv.Atoi(subArticleMatches[0])
						if err != nil {
							log.Fatal("Bad subarticle ID", subArticleMatches[0])
						}
						if len(article.Subarticles) != subArticleID-1 {
							log.Fatal("Invalid subarticle ID", len(article.Subarticles), subArticleID)
						}
						// subArticleID = GDPRSubarticleID(fmt.Sprintf("%s.%s", articleID, strings.ReplaceAll(subArticleNumber, ".", "")))
						body := strings.ReplaceAll(line, fmt.Sprintf("%s. ", strconv.Itoa(subArticleID)), "")
						subarticle := GDPRSubarticle{
							ID:   fmt.Sprintf("%s.%s", article.ID, subArticleMatches[0]),
							Body: body,
						}
						article.Subarticles = append(article.Subarticles, subarticle)

					} else {
						if subArticleID == -1 {
							if article.Body == "" {
								article.Body = line
							} else {
								article.Body = "\n" + line
							}
						} else {
							article.Subarticles[subArticleID].Body = article.Subarticles[subArticleID].Body + "\n" + line
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

func GenerateGDPRMarkdown(gdprArticle GDPRArticle, scfControlMapping SCFControlMappings) error {
	scfArticle := strings.ReplaceAll(gdprArticle.ID, "Article", "Art")
	f, err := os.Create(fmt.Sprintf("gdpr/%s.md", safeFileName(strings.ReplaceAll(scfArticle, ".", "-"))))
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1(string(gdprArticle.ID)).
		H2(gdprArticle.Title).
		PlainText(gdprArticle.Body)

	gdprSubarticleIDs := []string{}
	for gdprSubArticleID := range gdprArticle.Subarticles {
		gdprSubarticleIDs = append(gdprSubarticleIDs, string(gdprSubArticleID))
	}
	for gdprSubArticleID, gdprSubArticle := range gdprSubarticleIDs {
		scfSubArticle := strings.ReplaceAll(string(gdprSubArticleID), "Article", "Art")
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

func GenerateGDPRIndex(gdprFramework GDPRFramework) error {
	f, err := os.Create("gdpr/index.md")
	if err != nil {
		return err
	}
	doc := md.NewMarkdown(f).
		H1("GDPR")
	controlLinks := []string{}
	// sortedIDs := []string{}
	// for gdprArticleID, _ := range gdprFramework {
	// 	sortedIDs = append(sortedIDs, gdprArticleID)
	// }
	// sortNumbers(sortedIDs)
	for _, article := range gdprFramework {

		controlLinks = append(controlLinks, fmt.Sprintf("[%s](%s.md)", article.ID, safeFileName(article.ID)))
	}
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}

// func sortNumbers(data []string) ([]string, error) {
// 	var lastErr error
// 	sort.Slice(data, func(i, j int) bool {
// 		a, err := strconv.ParseInt(data[i], 10, 64)
// 		if err != nil {
// 			lastErr = err
// 			return false
// 		}
// 		b, err := strconv.ParseInt(data[j], 10, 64)
// 		if err != nil {
// 			lastErr = err
// 			return false
// 		}
// 		return a < b
// 	})
// 	return data, lastErr
// }
