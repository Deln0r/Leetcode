func maxDistance(arrays [][]int) int {
	smallest := arrays[0][0]
	biggest := arrays[0][len(arrays[0])-1]
	maxDistance := 0

	for i := 1; i < len(arrays); i++ {
		// Update maxDistance considering the current array
		maxDistance = int(math.Max(float64(maxDistance), math.Abs(float64(arrays[i][len(arrays[i])-1]-smallest))))
		maxDistance = int(math.Max(float64(maxDistance), math.Abs(float64(biggest-arrays[i][0]))))

		// Update smallest and biggest
		smallest = int(math.Min(float64(smallest), float64(arrays[i][0])))
		biggest = int(math.Max(float64(biggest), float64(arrays[i][len(arrays[i])-1])))
	}

	return maxDistance
}