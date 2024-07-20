func restoreMatrix(rowSum []int, colSum []int) [][]int {
	result := make([][]int, len(rowSum))
	for i, _ := range rowSum {
		result[i] = make([]int, len(colSum))
		for j, _ := range colSum {
			minNum := min(rowSum[i], colSum[j])
			result[i][j] = minNum
			rowSum[i] -= minNum
			colSum[j] -= minNum
		}
	}
	return result
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}