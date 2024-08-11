func letterCombinations(digits string) []string {
	var res []string
	if digits == "" {
		return res
	}
	m := []string{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	backTrack("", digits, &res, m)
	return res
}
func backTrack(cur, digits string, res *[]string, input []string) {
	if len(digits) == 0 {
		*res = append(*res, cur)
		return
	}

	letters := input[digits[0]-'2'] // Get the letters corresponding to the current digit
	for _, val := range letters {
		backTrack(cur+string(val), digits[1:], res, input) // Recurse with updated current combination and remaining digits
	}
}