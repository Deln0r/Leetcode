func spiralMatrixIII(R int, C int, r0 int, c0 int) [][]int {
	res, round, temp := [][]int{}, 0, [][]int{
		[]int{0, 1},
		[]int{1, 0},
		[]int{0, -1},
		[]int{-1, 0},
	}
	res = append(res, []int{r0, c0})
	for i := 0; len(res) < R*C; i++ {
		for j := 0; j < i/2+1; j++ {
			r0 += temp[round%4][0]
			c0 += temp[round%4][1]
			if r0 >= 0 && r0 < R && c0 >= 0 && c0 < C {
				res = append(res, []int{r0, c0})
			}
		}
		round++
	}
	return res
}