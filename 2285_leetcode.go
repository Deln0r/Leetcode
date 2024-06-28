func maximumImportance(n int, roads [][]int) int64 {
	count := make([]int, n)

	for _, road := range roads {
		count[road[0]]++
		count[road[1]]++
	}

	sort.Ints(count)

	var max int64

	for i := 1; i <= n; i++ {
		max += int64(i) * int64(count[i-1])
	}

	return max
}