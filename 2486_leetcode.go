func appendCharacters(s string, t string) int {
	i, j := 0, 0
	for i < len(s) && j < len(t) {
		if t[j] == s[i] {
			j += 1
		}
		i += 1
	}
	return len(t) - j
}