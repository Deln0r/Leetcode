func toIdx(c byte) int {
	switch c {
	case 'a':
		return 0
	case 'e':
		return 1
	case 'i':
		return 2
	case 'o':
		return 3
	case 'u':
		return 4
	}
	return -1
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func findTheLongestSubstring(s string) int {
	var shortestPrefix [32]int
	var state uint
	shortestPrefix[state] = 0
	ans := 0
	for i := 0; i < len(s); i++ {
		idx := toIdx(s[i])
		if idx >= 0 {
			state ^= 1 << idx
		}
		startIdx := shortestPrefix[state]
		if state == 0 || startIdx != 0 {
			ans = max(ans, i+1-startIdx)
			continue
		}
		shortestPrefix[state] = i + 1
	}
	return ans
}