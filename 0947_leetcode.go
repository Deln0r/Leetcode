type UnionFinder []int

func (uf UnionFinder) Find(i int) (root int) {
	for uf[i] != i {
		i = uf[i]
	}
	return i
}
func (uf UnionFinder) Union(i, j int) {
	r1, r2 := uf.Find(i), uf.Find(j)
	if r1 != r2 {
		uf[r2] = r1
	}
}

func (uf UnionFinder) Count() (c int) {
	var m [10001]bool
	for _, i := range uf {
		r := uf.Find(i)
		if !m[r] {
			c++
		}
		m[r] = true
	}
	return
}

func removeStones(stones [][]int) int {
	var indX, indY [10001][]int
	for i, stone := range stones {
		indX[stone[0]] = append(indX[stone[0]], i)
		indY[stone[1]] = append(indY[stone[1]], i)
	}
	var uf UnionFinder = func() []int {
		s := make([]int, len(stones))
		for i := range s {
			s[i] = i
		}
		return s
	}()
	var search func(i int, root int)
	var visited [10001]bool
	search = func(i int, root int) {
		if visited[i] {
			return
		}
		visited[i] = true
		uf.Union(root, i)
		for _, p := range indX[stones[i][0]] {
			search(p, root)
		}
		for _, p := range indY[stones[i][1]] {
			search(p, root)
		}
	}
	for i := range stones {
		search(i, i)
	}
	return len(stones) - uf.Count()
}