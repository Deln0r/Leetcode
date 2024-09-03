func getLucky(s string, k int) int {
	str := ""
	sum := 0
	for i := 0; i < len(s); i++ {
		n := int(s[i]) - 96
		str += strconv.Itoa(n)
	}

	for j := 0; j < k; j++ {
		sum = 0
		for i := 0; i < len(str); i++ {
			n, _ := strconv.Atoi(string(str[i]))
			for n > 0 {
				res := n % 10
				n /= 10
				sum += res
			}
		}
		str = strconv.Itoa(sum)
	}
	return sum
}