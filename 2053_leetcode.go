func kthDistinct(arr []string, k int) string {
	h := make(map[string]int)
	for _, i := range arr {
		h[i]++
	}

	for _, i := range arr {
		c, _ := h[i]
		if c == 1 {
			k--
			if k == 0 {
				return i
			}
		}
	}

	return ""
}