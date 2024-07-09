func findTheWinner(n int, k int) int {
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = i + 1 // friends start at 1, not 0
	}
	return solve(arr, 0, k)
}

func solve(arr []int, pos, k int) int {
	if len(arr) == 1 {
		return arr[0]
	}
	friendToRemove := ((pos + k - 1) % len(arr))
	return solve(append(arr[:friendToRemove], arr[friendToRemove+1:]...), friendToRemove, k)
}