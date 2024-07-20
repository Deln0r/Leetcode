func luckyNumbers(matrix [][]int) []int {
	maxIndexCols := make([]int, len(matrix[0]), len(matrix[0]))

	for i := 0; i < len(matrix[0]); i++ {
		var maxIndexRow int

		for j := 0; j < len(matrix); j++ {
			element := matrix[j][i]
			if element > matrix[maxIndexRow][i] {
				maxIndexRow = j
			}
		}

		maxIndexCols[i] = maxIndexRow
	}

	res := make([]int, 0)
outer:
	for i := 0; i < len(maxIndexCols); i++ {
		maxIndexRow := maxIndexCols[i]

		min := matrix[maxIndexRow][i]
		for j := 0; j < len(matrix[maxIndexRow]); j++ {
			num := matrix[maxIndexRow][j]
			if num < min {
				continue outer
			}
		}

		res = append(res, min)
	}

	return res
}