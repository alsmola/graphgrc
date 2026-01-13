package internal

import "strings"

func safeFileName(input string) string {
	output := input
	removeCharacters := []string{".", "_", " ", "(", ")"}
	for _, c := range removeCharacters {
		output = strings.ReplaceAll(output, c, "")
	}
	return strings.ToLower(output)
}
