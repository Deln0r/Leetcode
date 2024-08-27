type Vertex struct {
	Id   int
	Prob float64
}

func maxProbability(n int, edges [][]int, succProb []float64, start int, end int) float64 {
	adj := make(map[int][]Vertex)
	prob := make([]float64, n)

	for idx, edge := range edges {
		v1 := edge[0]
		v2 := edge[1]
		adj[v1] = append(adj[v1], Vertex{v2, succProb[idx]})
		adj[v2] = append(adj[v2], Vertex{v1, succProb[idx]})
	}
	prob[start] = 1.0
	queue := []int{start}

	for len(queue) > 0 {
		currVertex := queue[0]
		queue = queue[1:]

		currProb := prob[currVertex]
		for _, next := range adj[currVertex] {
			nextVertex := next.Id
			nextProb := next.Prob

			if prob[nextVertex] < currProb*nextProb {
				prob[nextVertex] = currProb * nextProb
				queue = append(queue, nextVertex)
			}
		}
	}

	return prob[end]
}