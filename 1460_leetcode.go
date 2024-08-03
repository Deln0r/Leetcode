func canBeEqual(target []int, arr []int) bool {
	if len(target) != len(arr) {
		return false
	}
	itarget := make([]int, 1001, 1001)
	iarr := make([]int, 1001, 1001)
	for i := 0; i < len(target); i++ {
		itarget[target[i]]++
		iarr[arr[i]]++
	}
	for i := 0; i < 1000; i++ {
		if itarget[i] != iarr[i] {
			return false
		}
	}
	return true
}