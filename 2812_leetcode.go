import "sort"

func maximumSafenessFactor(grid [][]int) int {
	n := len(grid)

	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return 0
	}

	// compute safeness for each cell
	queue := make([][2]int, 0, n*n)
	for i := range n {
		for j := range n {
			if grid[i][j] == 1 {
				queue = append(queue, [2]int{i, j})
				grid[i][j] = 0
			} else {
				grid[i][j] = -1
			}
		}
	}

	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // Define directions once
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		i, j := curr[0], curr[1]
		safeness := grid[i][j]

		for _, dir := range dirs {
			newR, newC := i+dir[0], j+dir[1]
			if newR >= 0 && newR < n && newC >= 0 && newC < n && grid[newR][newC] == -1 {
				grid[newR][newC] = safeness + 1
				queue = append(queue, [2]int{newR, newC})
			}
		}
	}

	// find maximum valid safeness
	end := 0
	for i := range n {
		for j := range n {
			end = max(end, grid[i][j])
		}
	}

	ans := sort.SearchInts(makeRange(0, end+1), func(minSafeness int) bool {
		return !isValidSafeness(grid, n, minSafeness) // Use sort.SearchInts for binary search
	}) - 1

	return ans
}

func isValidSafeness(grid [][]int, n int, minSafeness int) bool {
	if grid[0][0] < minSafeness || grid[n-1][n-1] < minSafeness {
		return false
	}

	queue := make([][2]int, 0, n*n)
	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	// Reuse queue from maximumSafenessFactor
	queue = append(queue, [2]int{0, 0})
	visited[0][0] = true

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		i, j := curr[0], curr[1]

		if i == n-1 && j == n-1 {
			return true
		}

		for _, dir := range dirs {
			newR, newC := i+dir[0], j+dir[1]
			if newR >= 0 && newR < n && newC >= 0 && newC < n && !visited[newR][newC] && grid[newR][newC] >= minSafeness {
				visited[newR][newC] = true
				queue = append(queue, [2]int{newR, newC})
			}
		}
	}

	return false
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func makeRange(min, max int) []int {
	a := make([]int, max-min)
	for i := range a {
		a[i] = min + i
	}
	return a
}