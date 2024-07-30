func minimumDeletions(s string) int {
	dels := 0
	b := 0

	for i := 0; i < len(s); i++ {
		if s[i] == 'a' && b > 0 {
			b--
			dels++
		} else if s[i] == 'b' {
			b++
		}
	}

	return dels
}