func survivedRobotsHealths(pos []int, hp []int, dirc string) []int {
	left, right := groupsOf(pos, dirc)
	st := []int{}
	m := len(left)
	lIdx := 0

	var top int

	for _, idx := range right {
		for lIdx < m && pos[left[lIdx]] > pos[idx] {
			st = append(st, left[lIdx])
			lIdx++
		}

		for len(st) > 0 {
			top = st[len(st)-1]
			if hp[top] > hp[idx] {
				hp[idx] = 0
				hp[top]--
				break
			}
			if hp[top] == hp[idx] {
				hp[idx], hp[top] = 0, 0
				st = st[:len(st)-1]
				break
			}
			hp[top] = 0
			hp[idx]--
			st = st[:len(st)-1]
		}
	}

	res := []int{}
	for i := range hp {
		if hp[i] > 0 {
			res = append(res, hp[i])
		}
	}
	return res
}

func groupsOf(pos []int, dirc string) ([]int, []int) {
	left, right := []int{}, []int{}

	for i := range dirc {
		if dirc[i] == byte('L') {
			left = append(left, i)
		} else {
			right = append(right, i)
		}
	}

	sort.Slice(left, func(i, j int) bool {
		return pos[left[i]] > pos[left[j]]
	})

	sort.Slice(right, func(i, j int) bool {
		return pos[right[i]] > pos[right[j]]
	})

	return left, right
}