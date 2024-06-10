func subarraysDivByK(nums []int, k int) int {
	dp := make(map[int]int)
	n := len(nums)
	sum := 0
	count := 0
	dp[0] = 1
	for i := 0; i < n; i++ {
		sum = (sum + nums[i]) % k
		if sum < 0 {
			sum += k
		}
		count += dp[sum]
		dp[sum]++
	}
	return count
}