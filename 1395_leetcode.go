func numTeams(rating []int) int {
	n := len(rating)
	if n < 3 {
		return 0
	}

	type soldier struct {
		rating, index int
	}

	soldiers := make([]soldier, n)
	for i, r := range rating {
		soldiers[i] = soldier{r, i}
	}
	sort.Slice(soldiers, func(i, j int) bool {
		return soldiers[i].rating < soldiers[j].rating
	})

	indexMap := make([]int, n)
	for i, s := range soldiers {
		indexMap[s.index] = i
	}

	countTeams := func(ascending bool) int {
		bit := make([]int, n+1)
		teams := 0

		for i := 0; i < n; i++ {
			rank := indexMap[i] + 1
			var left, right int
			if ascending {
				left = getSum(bit, rank-1)
				right = n - rank - (getSum(bit, n) - getSum(bit, rank))
			} else {
				left = getSum(bit, n) - getSum(bit, rank)
				right = rank - 1 - getSum(bit, rank-1)
			}
			teams += left * right
			update(bit, rank, 1)
		}

		return teams
	}

	return countTeams(true) + countTeams(false)
}

func update(bit []int, index, val int) {
	for index < len(bit) {
		bit[index] += val
		index += index & (-index)
	}
}

func getSum(bit []int, index int) int {
	sum := 0
	for index > 0 {
		sum += bit[index]
		index -= index & (-index)
	}
	return sum
}