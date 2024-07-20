
func threeSumClosest(nums []int, target int) int {
	rs := nums[0] + nums[1] + nums[2]
	if len(nums) == 3 {
		return rs
	}
	sort.Ints(nums)

	min := math.MaxInt32

	for i := 0; i < len(nums)-2; i++ {
		start := i + 1
		end := len(nums) - 1

		for start < end {
			sum := nums[i] + nums[start] + nums[end]
			dif := int(math.Abs(float64(target - sum)))

			if dif < min {
				rs = sum
				min = dif
			}
			if sum == target {
				return rs
			} else if sum < target {
				start++
			} else {
				end--
			}
		}

	}

	return rs
}