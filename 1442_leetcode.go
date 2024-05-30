func countTriplets(arr []int) int {
	n := len(arr)
	count := 0

	prefixXOR := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefixXOR[i+1] = prefixXOR[i] ^ arr[i]
	}

	for k := 1; k <= n; k++ {
		for i := 0; i < k; i++ {
			if prefixXOR[i] == prefixXOR[k] {
				count += k - i - 1
			}
		}
	}

	return count
}