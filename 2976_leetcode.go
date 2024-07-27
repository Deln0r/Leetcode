func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
	const inf = math.MaxInt64
	n := 26 // (a-z)

	costMatrix := make([][]int, n)
	for i := range costMatrix {
		costMatrix[i] = make([]int, n)
		for j := range costMatrix[i] {
			if i != j {
				costMatrix[i][j] = inf
			}
		}
	}

	for i := range original {
		from := original[i] - 'a'
		to := changed[i] - 'a'
		costMatrix[from][to] = min(costMatrix[from][to], cost[i])
	}

	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if costMatrix[i][k] < inf && costMatrix[k][j] < inf {
					costMatrix[i][j] = min(costMatrix[i][j], costMatrix[i][k]+costMatrix[k][j])
				}
			}
		}
	}

	totalCost := int64(0)
	for i := range source {
		from := source[i] - 'a'
		to := target[i] - 'a'
		if from == to {
			continue
		}
		if costMatrix[from][to] == inf {
			return -1
		}
		totalCost += int64(costMatrix[from][to])
	}

	return totalCost
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}