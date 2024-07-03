func minDifference(nums []int) int {
	if len(nums) <= 4 {
		return 0
	}
	sort.Ints(nums)
	minDiff := nums[len(nums)-1] - nums[0]
	minDiff = min(minDiff, nums[len(nums)-4]-nums[0])
	minDiff = min(minDiff, nums[len(nums)-1]-nums[3])
	minDiff = min(minDiff, nums[len(nums)-2]-nums[2])
	minDiff = min(minDiff, nums[len(nums)-3]-nums[1])
	return minDiff
}