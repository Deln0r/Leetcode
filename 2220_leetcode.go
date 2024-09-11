func minBitFlips(start int, goal int) int {
	x := start ^ goal
	count := 0
	for ; x != 0; count++ {
		x &= x - 1
	}
	return count
}