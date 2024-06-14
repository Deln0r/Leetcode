func sortColors(nums []int) {
	low, i, hight := 0, 0, len(nums)-1
	for i <= hight {
		switch nums[i] {
		case 0:
			nums[low], nums[i] = nums[i], nums[low]
			low++
			i++
		case 1: // we can remove this and use `default`
			i++
		case 2:
			nums[i], nums[hight] = nums[hight], nums[i]
			hight--
		}
	}
}