package internal

import "strings"

func safeFileName(input string) string {
	return strings.ReplaceAll(input, " ", "_")
}
