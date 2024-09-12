func countConsistentStrings(allowed string, words []string) int {
	g := make([]bool, 27)
	for _, c := range allowed {
		g[int(c-'a')] = true
	}

	ans := 0
	for _, s := range words {
		good := true
		for _, c := range s {
			if !g[int(c-'a')] {
				good = false
				break
			}
		}
		if good {
			ans++
		}
	}

	return ans
}