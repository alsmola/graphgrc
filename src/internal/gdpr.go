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

func GetGDPRControls(url string, getFile bool) (GDPRFramework, error) {
	gdprFramework := GDPRFramework{}
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
						subArticleID = len(article.Subarticles)
						body := strings.ReplaceAll(line, fmt.Sprintf("%s. ", strconv.Itoa(subArticleID+1)), "")
						subarticle := GDPRSubarticle{
							ID:   fmt.Sprintf("%s.%d", article.ID, subArticleID+1),
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
		err = os.WriteFile("../data/gdpr.json", file, 0644)
		if err != nil {
			return gdprFramework, err
		}
	}
	gdprFile, err := os.Open("../data/gdpr.json")
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
		H1(fmt.Sprintf("GDPR - %s", string(gdprArticle.ID))).
		H2(gdprArticle.Title).
		PlainText(gdprArticle.Body).
		LF()

	// Determine if we're using SCF or custom controls based on control ID format
	// SCF IDs contain " - " (e.g., "AST-01 - Asset Governance")
	// Custom IDs are simple (e.g., "ACC-01")
	controlType := "scf"
	for scfID := range scfControlMapping {
		if !strings.Contains(string(scfID), " - ") {
			controlType = "custom"
			break
		}
	}

	headerText := "Mapped SCF controls"
	if controlType == "custom" {
		headerText = "Mapped custom controls"
	}

	// Also get the article-level mapping for controls that map to entire articles
	articleArt := strings.ReplaceAll(gdprArticle.ID, "Article", "Art")

	for _, gdprSubArticle := range gdprArticle.Subarticles {
		scfSubArticle := strings.ReplaceAll(string(gdprSubArticle.ID), "Article", "Art")
		doc.H2(gdprSubArticle.ID).
			PlainText(gdprSubArticle.Body)
		fcids := []string{}
		for scfID, controlMapping := range scfControlMapping {
			gdprFrameworkControlIDs := controlMapping["GDPR"]
			for _, fcid := range gdprFrameworkControlIDs {
				// Match either the specific subarticle (e.g., "Art 32.1") or the whole article (e.g., "Art 32")
				if string(fcid) == scfSubArticle || string(fcid) == articleArt {
					link := fmt.Sprintf("[%s](../%s/%s.md)", string(scfID), controlType, safeFileName(string(scfID)))
					// Avoid duplicates
					found := false
					for _, existing := range fcids {
						if existing == link {
							found = true
							break
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
			doc.H3(headerText)
			for _, fcid := range fcids {
				doc.PlainText(fmt.Sprintf("- %s", fcid))
			}
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
