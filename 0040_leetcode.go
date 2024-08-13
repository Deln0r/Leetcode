func combinationSum2(candidates []int, target int) [][]int {

	var result [][]int
	sort.Ints(candidates)

	var backtrack func(index int, subset []int, sum int)
	backtrack = func(index int, subset []int, sum int) {

		if sum == target {
			result = append(result, append([]int(nil), subset...))
			return
		}

		for i := index; i < len(candidates); i++ {

			if i > index && candidates[i] == candidates[i-1] {
				continue
			}
			if candidates[i]+sum > target {
				return
			}

			sub := append(subset, candidates[i])
			backtrack(i+1, sub, sum+candidates[i])
		}
	}

	backtrack(0, []int{}, 0)
	return result

}