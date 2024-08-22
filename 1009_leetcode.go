func bitwiseComplement(n int) int {
	if n == 0 {
		return 1
	}

	// Find the number of bits in num
	mask := n
	mask |= mask >> 1
	mask |= mask >> 2
	mask |= mask >> 4
	mask |= mask >> 8
	mask |= mask >> 16

	// XOR num with mask to flip all bits
	return n ^ mask
}