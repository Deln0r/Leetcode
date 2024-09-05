func missingRolls(rolls []int, mean int, n int) []int {
	ans := make([]int, n)
	totalRoll := len(rolls) + n  // total rolls
	totalSum := totalRoll * mean // total sum of rolls
	sum := 0                     // current sum of given rolls
	for _, v := range rolls {
		sum += v
	}
	leftRoll := totalSum - sum // missing sum of rolls

	// return empty array
	// if missing rolls sum is greater than maximum sum of missing rolls
	// ie n*6 as dice can have max value of 6
	// or missing rolls sum is less missing rolls, n
	// ie as dice can have minimum value of 1
	if leftRoll > n*6 || leftRoll < n {
		return []int{}
	}

	avgRoll := leftRoll / n // calculate average roll

	// Push avgRoll in n-1 missing roll data
	for i := 0; i < n-1; i++ {
		ans[i] = avgRoll
		leftRoll -= avgRoll
	}

	// In last missing roll assign left over sum
	// if its less than 6
	// otherwise assign equally
	if leftRoll > 6 {
		ans[n-1] = avgRoll
		leftRoll -= avgRoll
		for leftRoll > 0 {
			ans[leftRoll]++
			leftRoll--
		}
	} else {
		ans[n-1] = leftRoll
	}
	return ans
}