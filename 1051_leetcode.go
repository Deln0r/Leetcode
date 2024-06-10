func heightChecker(heights []int) int {
	expected := make([]int, len(heights))
	copy(expected, heights)
	sort.Ints(expected)
	var ans int
	for i := 0; i < len(heights); i++ {
		if heights[i] != expected[i] {
			ans++
		}
	}
	return ans
}