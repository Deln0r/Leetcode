func passThePillow(n int, time int) int {
	if time <= n-1 {
		return time + 1
	}
	x := ((time / (n - 1)) % 2)
	//fmt.Printf("(%d / (%d-1)) mod 2) = %d\n", time, n, x)
	mod := time % (n - 1)
	//fmt.Printf("%d mod (%d-1) = %d\n", time, n, mod)
	if x != 0 {
		// start from right
		return n - mod
	}
	return mod + 1
}