func solve(nums []int, difference int) int {
	count := 0
	j := 0
	n := len(nums)

	for i := 0; i < n; i++ {
		for j < n && (nums[j]-nums[i] <= difference) {
			j++
		}
		count += j - i - 1
	}

	return count
}

func smallestDistancePair(nums []int, k int) int {
	n := len(nums)
	sort.Ints(nums)

	low := 0
	high := nums[n-1] - nums[0]

	ans := -1

	for low <= high {
		mid := low + (high-low)/2
		count := solve(nums, mid)

		if count >= k {
			ans = mid
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return ans
}