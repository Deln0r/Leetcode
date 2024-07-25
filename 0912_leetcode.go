func sortArray(nums []int) []int {
	siftDown := func(i, n int) {
		for 2*i+1 < n {
			swap := i
			if nums[swap] < nums[2*i+1] {
				swap = 2*i + 1
			}
			if 2*i+2 < n && nums[swap] < nums[2*i+2] {
				swap = 2*i + 2
			}
			nums[i], nums[swap] = nums[swap], nums[i]
			if i == swap {
				break
			}
			i = swap
		}
	}

	n := len(nums)
	for i := (n - 1) / 2; i >= 0; i-- {
		siftDown(i, n)
	}

	for i := n - 1; i >= 0; i-- {
		nums[0], nums[i] = nums[i], nums[0]
		siftDown(0, i)
	}

	return nums
}