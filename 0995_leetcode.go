func minKBitFlips(nums []int, k int) int {
	n := len(nums)
	flipped := make([]int, n)
	flip := 0
	result := 0

	for i := 0; i < n; i++ {
		if i >= k {
			flip ^= flipped[i-k]
		}

		if nums[i] == flip {
			if i+k > n {
				return -1
			}

			result++
			flip ^= 1
			flipped[i] = 1
		}
	}

	return result
}
