func minSwaps(nums []int) int {
	n := len(nums)

	totalOnes := 0

	for _, num := range nums {
		totalOnes += num
	}

	maxOnes := 0
	t := 0

	for i := 0; i < totalOnes; i++ {
		t += nums[i]
	}

	maxOnes = t

	l, r := 0, totalOnes-1

	for l < n {

		t -= nums[l]
		l++

		r++
		t += nums[r%n]

		maxOnes = max(maxOnes, t)
	}

	return totalOnes - maxOnes
}