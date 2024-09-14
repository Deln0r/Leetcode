func longestSubarray(nums []int) int {
	res, curVal, curCount := 1, nums[0], 1
	for i := 1; i < len(nums); i++ {
		if curVal > nums[i] {
			curCount = 0
			continue
		}

		if curVal == nums[i] {
			curCount++
			res = max(res, curCount)
		} else {
			curVal = nums[i]
			curCount = 1
			res = 1
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}