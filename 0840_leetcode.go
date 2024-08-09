func numMagicSquaresInside(grid [][]int) int {
	res, m, n := 0, len(grid), len(grid[0])

	for i := 1; i < m-1; i++ {
		for j := 1; j < n-1; j++ {
			if isMagic(grid, i, j) {
				res++
			}
		}
	}

	return res
}

func isMagic(grid [][]int, i, j int) bool {
	m, index := make(map[byte]int), 0
	distinct := make(map[int]bool)

	for r := i - 1; r <= i+1; r++ {
		for c := j - 1; c <= j+1; c++ {
			val := grid[r][c]
			if val < 1 || val > 9 {
				return false
			}
			distinct[val] = true
			m['a'+byte(index)] = val
			index++
		}
	}

	if len(distinct) != 9 {
		return false
	}

	combis := []string{"abc", "def", "ghi", "adg", "beh", "cfi", "aei", "ceg"}
	prev := 0

	for _, combi := range combis {
		cur := 0
		for k := 0; k < 3; k++ {
			cur += m[combi[k]]
		}
		if prev != 0 && cur != prev {
			return false
		}
		prev = cur
	}

	return true
}