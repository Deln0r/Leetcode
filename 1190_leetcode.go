func toString(a []string) string {
	res := ""
	for _, c := range a {
		res += c
	}
	return res
}

func reverseParentheses(s string) string {
	opened := []int{}
	pair := map[int]int{}

	for i, c := range s {
		if c == '(' {
			opened = append(opened, i)
		}
		if c == ')' {
			j := opened[len(opened)-1]
			opened = opened[:len(opened)-1]
			pair[i], pair[j] = j, i
		}
	}

	res := []string{}
	i, d := 0, 1
	for i < len(s) {
		if s[i] == '(' || s[i] == ')' {
			i = pair[i]
			d = -d
		} else {
			res = append(res, string(s[i]))
		}
		i += d
	}

	return toString(res)
}