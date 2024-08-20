func stoneGameII(piles []int) int {
	n := len(piles)
	sums := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		sums[i] = sums[i+1] + piles[i]
	}

	dp := make([][]int, n+1)
	for idx := range dp {
		dp[idx] = make([]int, n+1)
		for j := range dp[idx] {
			dp[idx][j] = 0
		}
	}

	var calc func(start, m int) int
	calc = func(start, m int) int {
		if start >= n {
			return 0
		}

		ans := dp[start][m]
		if ans > 0 {
			return ans
		}

		for i := 1; i <= 2*m; i++ {
			ans = max(ans, sums[start]-calc(start+i, max(m, i)))
		}

		dp[start][m] = ans
		return ans
	}

	return calc(0, 1)
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}