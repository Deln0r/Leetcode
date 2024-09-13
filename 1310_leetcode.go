func xorQueries(arr []int, q [][]int) []int {
	ans := make([]int, len(q))
	for i := 1; i < len(arr); i++ {
		arr[i] ^= arr[i-1]
	}

	for i := 0; i < len(q); i++ {
		l, r := q[i][0], q[i][1]
		x := arr[r]
		if l > 0 {
			x ^= arr[l-1]
		}
		ans[i] = x
	}
	return ans
}