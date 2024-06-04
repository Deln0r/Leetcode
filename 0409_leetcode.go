func longestPalindrome(s string) int {
	// count each character frequency
	freq := make(map[string]int, 0)
	for _, v := range s {
		freq[string(v)] += 1
	}

	isOdd := false
	length := 0

	// Process each character frequency
	for _, count := range freq {
		// if even add the total freq(count) into the length
		if count%2 == 0 {
			length += count
		} else {
			// if odd subtract by 1 then add it into the length
			length = length + count - 1
			// mark it as odd because one of the char we can put it on the middle of the string later.
			isOdd = true
		}
	}

	if isOdd {
		length += 1
	}

	return length
}