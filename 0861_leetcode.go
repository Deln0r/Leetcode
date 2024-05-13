func matrixScore(grid [][]int) int {
	var m, n = len(grid), len(grid[0])
	for row := 0; row < m; row++ {
		if grid[row][0] == 0 {
			for col := 0; col < n; col++ {
				grid[row][col] ^= 1
			}
		}
	}
	var score = 0
	var zeros, ones int
	var bit = 1 << (n - 1)
	for col := 0; col < n; col++ {
		zeros = 0
		for row := 0; row < m; row++ {
			if grid[row][col] == 0 {
				zeros++
			}
		}
		ones = m - zeros
		score += max(ones, zeros) * bit
		bit >>= 1
	}
	return score
}