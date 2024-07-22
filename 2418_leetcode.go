type P struct {
	N string
	H int
}

func sortPeople(names []string, heights []int) []string {
	pers := make([]P, len(names))
	for i := 0; i < len(names); i++ {
		pers[i] = P{N: names[i], H: heights[i]}
	}

	sort.Slice(pers, func(i, j int) bool {
		return pers[i].H > pers[j].H
	})

	res := make([]string, len(names))
	for i := 0; i < len(names); i++ {
		res[i] = pers[i].N
	}

	return res
}