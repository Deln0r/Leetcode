func wordBreak(s string, wordDict []string) []string {
	wordMap := make(map[string]bool)

	for _, word := range wordDict {
		wordMap[word] = true
	}

	res := make([]string, 0)

	currentSentence := ""
	l := 0

	var traverse func(pos int)
	traverse = func(pos int) {
		if pos == len(s) {
			if string(currentSentence[len(currentSentence)-1]) == " " {
				res = append(res, ""+currentSentence[:len(currentSentence)-1])
			}
			return
		}
		currentSentence += string(s[pos])
		_, ok := wordMap[currentSentence[l:]]
		if ok {
			currentSentence += " "
			temp := l
			l = len(currentSentence)
			traverse(pos + 1)
			currentSentence = currentSentence[:len(currentSentence)-1]
			l = temp
		}
		traverse(pos + 1)
		currentSentence = currentSentence[:len(currentSentence)-1]
	}
	traverse(0)
	return res
}