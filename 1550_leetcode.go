func threeConsecutiveOdds(arr []int) bool {
	count := 0

	for _, i := range arr {

		if i%2 != 0 {
			count++
			if count == 3 {
				return true
			}
		} else {
			count = 0
		}
	}
	return false
}