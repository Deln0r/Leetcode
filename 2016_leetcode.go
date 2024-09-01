func maximumDifference(nums []int) int {
	n := len(nums)
	minValue := nums[0] // Минимальное значение на текущий момент
	maxDiff := -1       // Начальное значение максимальной разницы

	for i := 1; i < n; i++ {
		if nums[i] > minValue {
			maxDiff = int(math.Max(float64(maxDiff), float64(nums[i]-minValue)))
		} else {
			minValue = nums[i]
		}
	}

	return maxDiff
}