var (
	land  = 1
	water = 0

	directions = [][]int{
		{1, 0}, {-1, 0},
		{0, 1}, {0, -1},
	}
)

func invalidMove(grid1, grid2 [][]int, row, col int) bool {
	rowOverflow := row < 0 || row >= len(grid2)
	colOverflow := col < 0 || col >= len(grid2[0])

	return rowOverflow || colOverflow || grid2[row][col] != land
}

func isSubIsland(grid1, grid2 [][]int, row, col int) bool {
	if invalidMove(grid1, grid2, row, col) {
		return true
	}

	if grid1[row][col] != land {
		return false
	}

	grid2[row][col] = water

	ans := true
	for _, direction := range directions {
		rn := row + direction[0]
		cn := col + direction[1]

		if !isSubIsland(grid1, grid2, rn, cn) {
			ans = false
		}
	}

	return ans
}

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	ans := 0

	for row, _ := range grid2 {
		for col, _ := range grid2[row] {
			if grid1[row][col] == land && grid2[row][col] == land {
				if isSubIsland(grid1, grid2, row, col) {
					ans++
				}
			}
		}
	}

	return ans
}