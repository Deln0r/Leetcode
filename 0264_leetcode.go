func nthUglyNumber(n int) int {
	arr := make([]int, n)
	if n == 1 {
		return n
	}
	arr[0] = 1
	in2 := 0
	in3 := 0
	in5 := 0
	for i := 1; i < n; i++ {
		a := arr[in2] * 2
		b := arr[in3] * 3
		c := arr[in5] * 5
		min := Min(a, Min(c, b))
		arr[i] = min
		if min == a {
			in2++
		}
		if min == b {
			in3++
		}
		if min == c {
			in5++
		}
	}
	return arr[n-1]
}

//[1, 2, 3, 4, 5, 6, 1,8, 9, 10]

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}