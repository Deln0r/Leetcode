func beautifulSubsets(nums []int, k int) int {
	n := len(nums)
	count := 0

	// Helper function for backtracking
	var backtrack func(start int, subset []int)
	backtrack = func(start int, subset []int) {
		// Each subset we form is a valid non-empty subset
		if len(subset) > 0 {
			count++
		}

		for i := start; i < n; i++ {
			// Check if adding nums[i] would violate the beautiful subset condition
			valid := true
			for _, val := range subset {
				if abs(val-nums[i]) == k {
					valid = false
					break
				}
			}
			if valid {
				subset = append(subset, nums[i])
				backtrack(i+1, subset)
				subset = subset[:len(subset)-1] // Backtrack
			}
		}
	}

	// Start backtracking from the first element
	backtrack(0, []int{})
	return count
}

// Helper function to get the absolute value
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}