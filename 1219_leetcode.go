func getMaximumGold(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	rows, cols := len(grid), len(grid[0])
	maxGold := 0

	// Define the directions (up, down, left, right)
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	// Define a helper function to perform DFS
	var dfs func(row, col, gold int)
	dfs = func(row, col, gold int) {
		// Check if the current cell is out of bounds or has no gold
		if row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] == 0 {
			return
		}

		// Collect gold from the current cell
		gold += grid[row][col]

		// Update maxGold if needed
		if gold > maxGold {
			maxGold = gold
		}

		// Mark the current cell as visited
		temp := grid[row][col]
		grid[row][col] = 0

		// Explore all possible directions
		for _, dir := range dirs {
			newRow, newCol := row+dir[0], col+dir[1]
			dfs(newRow, newCol, gold)
		}

		// Restore the grid
		grid[row][col] = temp
	}

	// Iterate through each cell in the grid
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			// Start DFS from each cell containing gold
			if grid[i][j] != 0 {
				dfs(i, j, 0)
			}
		}
	}

	return maxGold
}