func scoreOfString(s string) int {
	counter := 0.0
	j := 1
	for i := 0; i < len(s)-1; i++ {
		num := float64(s[i]) - float64(s[j])
		counter += math.Abs(num)
		j++
	}
	return int(counter)
}