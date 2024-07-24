func frequencySort(nums []int) []int {
	c := make([]int, 201)
	for _, num := range nums {
		c[num+100]++
	}

	sort.Slice(nums, func(i, j int) bool {
		if c[nums[i]+100] == c[nums[j]+100] {
			return nums[i] > nums[j]
		}
		return c[nums[i]+100] < c[nums[j]+100]
	})

	return nums
}