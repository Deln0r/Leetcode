func regionsBySlashes(grid []string) int {
	n := len(grid)
	// Create an expanded grid of size 3*n x 3*n
	expandedGrid := make([][]int, 3*n)
	for i := range expandedGrid {
		expandedGrid[i] = make([]int, 3*n)
	}

	// Fill the expanded grid based on the characters in the original grid
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == '/' {
				expandedGrid[3*i][3*j+2] = 1
				expandedGrid[3*i+1][3*j+1] = 1
				expandedGrid[3*i+2][3*j] = 1
			} else if grid[i][j] == '\\' {
				expandedGrid[3*i][3*j] = 1
				expandedGrid[3*i+1][3*j+1] = 1
				expandedGrid[3*i+2][3*j+2] = 1
			}
		}
	}

	// DFS function to explore and mark connected regions
	var dfs func(x, y int)
	dfs = func(x, y int) {
		if x < 0 || x >= 3*n || y < 0 || y >= 3*n || expandedGrid[x][y] != 0 {
			return
		}
		expandedGrid[x][y] = 1 // Mark the cell as visited
		dfs(x-1, y)            // Explore up
		dfs(x+1, y)            // Explore down
		dfs(x, y-1)            // Explore left
		dfs(x, y+1)            // Explore right
	}

	regions := 0
	// Count the number of distinct regions
	for i := 0; i < 3*n; i++ {
		for j := 0; j < 3*n; j++ {
			if expandedGrid[i][j] == 0 { // Found a new region
				regions++
				dfs(i, j)
			}
		}
	}

	return regions
}