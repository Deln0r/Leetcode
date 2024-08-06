func minimumPushes(word string) int {
	cc := make([]int, 27)
	ch := make([]int, 27)

	for i := 0; i < len(ch); i++ {
		ch[i] = i
	}
	for _, c := range word {
		cc[int(c)-'a']++
	}

	sort.Slice(ch, func(i, j int) bool {
		return cc[ch[i]] > cc[ch[j]]
	})

	ans := 0
	for i := 0; i < len(ch); i++ {
		ans += (i/8 + 1) * cc[ch[i]]
	}

	return ans
}