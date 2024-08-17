func maxPoints(points [][]int) int64 {
	m, n := len(points), len(points[0])
	dp := make([]int64, n)

	for j, val := range points[0] {
		dp[j] = int64(val)
	}

	for i := 1; i < m; i++ {
		newDp := make([]int64, n)

		leftMax := dp[0]
		for j := 0; j < n; j++ {
			leftMax = max(leftMax, dp[j])
			newDp[j] = leftMax + int64(points[i][j])
			leftMax--
		}

		rightMax := dp[n-1]
		for j := n - 1; j >= 0; j-- {
			rightMax = max(rightMax, dp[j])
			newDp[j] = max(newDp[j], rightMax+int64(points[i][j]))
			rightMax--
		}

		dp = newDp
	}

	var res int64
	for j := 0; j < n; j++ {
		res = max(res, dp[j])
	}

	return res
}

func max(x, y int64) int64 {
	if x >= y {
		return x
	} else {
		return y
	}
}
