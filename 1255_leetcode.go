func maxScoreWords(words []string, letters []byte, score []int) int {
	// Use unique letter counters
	var let = make([]int, 26)
	for _, l := range letters {
		let[l-'a']++
	}

	var (
		maxScore int
		curScore int
		search   func(pos int)
	)
	search = func(pos int) {
		if pos == len(words) {
			// reached end of current branch,
			// check if have max score
			if curScore > maxScore {
				maxScore = curScore
			}
			return
		}
		// opt into branch were words[pos] is not selected
		search(pos + 1)

		// check if can select words[pos]
		for i, ch := range words[pos] {
			if let[ch-'a'] == 0 {
				// no letters available
				// rollback and leave branch
				for j := 0; j < i; j++ {
					let[words[pos][j]-'a']++
					curScore -= score[words[pos][j]-'a']
				}
				return
			}
			// decrement letter counter
			let[ch-'a']--
			// update score
			curScore += score[ch-'a']
		}
		// opt into branch where words[pos] is selected
		search(pos + 1)

		// done with this branch
		// rollback letter counters and current score
		for _, ch := range words[pos] {
			let[ch-'a']++
			curScore -= score[ch-'a']
		}
	}
	// scan possible branches starting from 0 position
	search(0)
	return maxScore
}