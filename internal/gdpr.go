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
				articleIDMatch, err := strconv.Atoi(articleMatches[1])
				if err != nil {
					log.Fatal("Bad GDPR article ID", articleMatches[1])
				}
				articleID = articleIDMatch - 1
				for len(gdprFramework) < articleID {
					gdprFramework = append(gdprFramework, GDPRArticle{
						ID:          fmt.Sprintf("Article %d", len(gdprFramework)),
						Subarticles: []GDPRSubarticle{},
					})
				}
				article := GDPRArticle{
					ID:          fmt.Sprintf("Article %d", articleID+1),
					Subarticles: []GDPRSubarticle{},
				}
				gdprFramework = append(gdprFramework, article)
				subArticleID = -1
			} else if articleID != -1 {
				article := gdprFramework[articleID]
				if article.Title == "" {
					article.Title = line
				} else {
					regexPattern := `^([0-9]+)\.`
					regex := regexp.MustCompile(regexPattern)
					subArticleMatches := regex.FindStringSubmatch(line)
					if len(subArticleMatches) > 0 {
						subArticleIDMatch, err := strconv.Atoi(subArticleMatches[1])
						if err != nil {
							log.Fatal("Bad subarticle ID", subArticleMatches[1])
						}
						subArticleID = subArticleIDMatch - 1
						if len(article.Subarticles) != subArticleID {
							// log.Println("Invalid subarticle ID", len(article.Subarticles), subArticleID)
							subArticleID = len(article.Subarticles)
						}
						body := strings.ReplaceAll(line, fmt.Sprintf("%s. ", strconv.Itoa(subArticleID+1)), "")
						subarticle := GDPRSubarticle{
							ID:   fmt.Sprintf("%s.%s", article.ID, subArticleMatches[1]),
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

	for _, gdprSubArticle := range gdprArticle.Subarticles {
		scfSubArticle := strings.ReplaceAll(string(gdprSubArticle.ID), "Article", "Art")
		doc.H2(gdprSubArticle.ID).
			PlainText(gdprSubArticle.Body)
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
	for _, article := range gdprFramework {
		if article.Title != "" {
			link := strings.ReplaceAll(article.ID, "Article", "Art")
			controlLinks = append(controlLinks, fmt.Sprintf("[%s - %s](%s.md)", article.ID, article.Title, safeFileName(link)))
		}
	}
	doc.BulletList(controlLinks...)
	doc.Build()
	return nil
}
