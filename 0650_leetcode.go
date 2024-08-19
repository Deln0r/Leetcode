func minSteps(x int) int {
	if x <= 1 {
		return 0
	}
	for i := (x / 2) - 1; i > 1; i-- {
		if x%i == 0 {
			return minSteps(i) + x/i
		}
	}
	return x
}