func construct2DArray(original []int, m int, n int) [][]int {
	l := len(original)
	if m*n != l {
		return [][]int{}
	}
	res := make([][]int, m)
	pointer := 0
	for i := 0; i < m; i++ {
		res[i] = make([]int, n)
		for j := 0; j < n; j++ {
			res[i][j] = original[pointer]
			pointer++
		}
	}
	return res
}