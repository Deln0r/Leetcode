func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

// Backtracking function to find all palindrome partitions
func backtrack(result *[][]string, tempList []string, s string, start int) {
	if start == len(s) {
		// If we've reached the end of the string, add the current partitioning to the result
		newList := make([]string, len(tempList))
		copy(newList, tempList)
		*result = append(*result, newList)
	} else {
		for i := start; i < len(s); i++ {
			// Check if the current substring is a palindrome
			if isPalindrome(s[start : i+1]) {
				// If it is, add it to the current path and continue to partition the remaining string
				tempList = append(tempList, s[start:i+1])
				backtrack(result, tempList, s, i+1)
				// Backtrack and remove the last added substring
				tempList = tempList[:len(tempList)-1]
			}
		}
	}
}

// Main function to partition the string into all possible palindrome partitions
func partition(s string) [][]string {
	var result [][]string
	backtrack(&result, []string{}, s, 0)
	return result
}