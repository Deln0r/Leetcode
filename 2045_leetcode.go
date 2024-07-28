func secondMinimum(n int, edges [][]int, time int, change int) int {
	g := make([][]int, n)
	for _, p := range edges {
		g[p[0]-1] = append(g[p[0]-1], p[1]-1)
		g[p[1]-1] = append(g[p[1]-1], p[0]-1)
	}
	v := make([]int, n)
	for i := range v {
		v[i] = -1
	}
	s := []int{n - 1}
	// since we need to find second shortest path, one of the options is
	// shortest path from 1 to n plus shortest path from n to n
	// therefore, we say that shortest path from n to n is 2
	v[n-1] = 2
	t := 0
	var s2 []int
	for len(s) > 0 {
		t++
		for _, i := range s {
			for _, j := range g[i] {
				if v[j] == -1 {
					s2 = append(s2, j)
					v[j] = t
				}
			}
		}
		s, s2 = s2, s[:0]
	}
	v1 := make([]int, n) // odd lengths
	v2 := make([]int, n) // even lengths
	for i := range v1 {
		v1[i] = -1
		v2[i] = -1
	}
	v2[0] = 0
	t = 0
	s = append(s, 0)
	for len(s) > 0 {
		t++
		if t > v[0] { // we're not interested in paths longer than shortest path from 1 to n
			break
		}
		for _, i := range s {
			for _, j := range g[i] {
				if v1[j] == -1 {
					s2 = append(s2, j)
					v1[j] = t
				}
			}
		}
		s, s2 = s2, s[:0]
		t++
		if t > v[0] {
			break
		}
		for _, i := range s {
			for _, j := range g[i] {
				if v2[j] == -1 {
					s2 = append(s2, j)
					v2[j] = t
				}
			}
		}
		s, s2 = s2, s[:0]
	}
	// let's find shortest path among shortest paths from every vertex
	// which is reachable from vertex 1 in exactly v[0] steps
	steps := -1
	if v[0]&1 == 0 {
		for i, s := range v2 {
			if s != -1 && (steps == -1 || steps > v[i]) {
				steps = v[i]
			}
		}
	} else {
		for i, s := range v1 {
			if s != -1 && (steps == -1 || steps > v[i]) {
				steps = v[i]
			}
		}
	}
	steps += v[0] // ... and add v[0] steps to reach that vertex from vertex 1
	// now some final math to find time
	t = (time-1)%(2*change) + 1
	m := change / t
	if m*t < change {
		m++
	}
	t = m * time
	if q := t % (2 * change); q != 0 {
		t += 2*change - q
	}
	return (steps-1)/m*t + time*(1+(steps-1)%m)
}