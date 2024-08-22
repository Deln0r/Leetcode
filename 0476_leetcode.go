func findComplement(num int) int {
	if num == 0 {
		return 1
	}

	// Find the number of bits in num
	mask := num
	mask |= mask >> 1
	mask |= mask >> 2
	mask |= mask >> 4
	mask |= mask >> 8
	mask |= mask >> 16

	// XOR num with mask to flip all bits
	return num ^ mask
}