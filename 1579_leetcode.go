type UnionFind struct {
	representative []int
	componentSize  []int
	components     int
}

func New(n int) *UnionFind {
	uf := UnionFind{}
	uf.components = n
	uf.representative = make([]int, n+1)
	uf.componentSize = make([]int, n+1)
	for i := range uf.representative {
		uf.representative[i] = i
		uf.componentSize[i] = 1
	}
	return &uf
}

func (uf *UnionFind) findRepresentative(x int) int {
	if uf.representative[x] == x {
		return x
	}
	uf.representative[x] = uf.findRepresentative(uf.representative[x])
	return uf.representative[x]
}

func (uf *UnionFind) performUnion(x int, y int) int {
	x, y = uf.findRepresentative(x), uf.findRepresentative(y)

	if x == y {
		return 0
	}
	if uf.componentSize[x] > uf.componentSize[y] {
		uf.representative[y] = x
		uf.componentSize[x] += uf.componentSize[y]
	} else {
		uf.representative[x] = y
		uf.componentSize[y] += uf.componentSize[x]
	}
	uf.components--
	return 1
}

func (uf *UnionFind) isConnected() bool {
	return uf.components == 1
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
	Alice, Bob := New(n), New(n)
	edgesRequired := 0
	for _, edge := range edges {
		if edge[0] == 3 {
			edgesRequired += Alice.performUnion(edge[1], edge[2]) | Bob.performUnion(edge[1], edge[2])
		}
	}

	for _, edge := range edges {
		if edge[0] == 1 {
			edgesRequired += Alice.performUnion(edge[1], edge[2])
		} else if edge[0] == 2 {
			edgesRequired += Bob.performUnion(edge[1], edge[2])
		}
	}

	if Alice.isConnected() && Bob.isConnected() {
		return len(edges) - edgesRequired
	}

	return -1
}