func commonChars(words []string) []string {
	if len(words) == 0 {
		return []string{}
	}

	minFreq := make([]int, 26)
	for i := range minFreq {
		minFreq[i] = 101
	}

	for _, word := range words {
		freq := make([]int, 26)
		for _, ch := range word {
			freq[ch-'a']++
		}

		for i := 0; i < 26; i++ {
			if freq[i] < minFreq[i] {
				minFreq[i] = freq[i]
			}
		}
	}

	var result []string
	for i := 0; i < 26; i++ {
		for minFreq[i] > 0 {
			result = append(result, string('a'+i))
			minFreq[i]--
		}
	}

	return result
}