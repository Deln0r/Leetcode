func threeSum(nums []int) [][]int {

	sort.Ints(nums)
	cache := make(map[int]int)
	result := make([][]int, 0)
	for i := 0; i < len(nums); i++ {
		cache[nums[i]] = i
	}

	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i-1] == nums[i] {
			continue //skip duplicates ONLY for this loop
		}
		for j := i + 1; j < len(nums); j++ {
			if j > i+1 && nums[j-1] == nums[j] {
				continue //skip duplicates ONLY for this loop
			}
			if cache[-nums[i]-nums[j]] > j { //check only with bigger indexes
				result = append(result, []int{nums[i], nums[j], -nums[i] - nums[j]})
			}
		}
	}
	return result
}