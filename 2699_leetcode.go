func modifiedGraphEdges(n int, edges [][]int, source int, destination int, target int) [][]int {
	adjList := make([][]int, n)
	for i := range adjList {
		adjList[i] = make([]int, n)
	}
	for _, edge := range edges {
		a, b, w := edge[0], edge[1], edge[2]
		if w == -1 {
			continue
		}
		adjList[a][b] = w
		adjList[b][a] = w
	}

	distance := find(adjList, n, source, destination)
	if distance[destination] < target {
		return [][]int{}
	}

	if distance[destination] == target {
		for _, edge := range edges {
			if edge[2] == -1 {
				edge[2] = 2e9
			}
		}
		return edges
	}

	for i, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		if w == -1 {
			edges[i][2] = 1
			adjList[u][v] = 1
			adjList[v][u] = 1
			distance = find(adjList, n, source, destination)
			if distance[destination] <= target {
				edges[i][2] += (target - distance[destination])
				for j := i + 1; j < len(edges); j++ {
					if edges[j][2] == -1 {
						edges[j][2] = 2e9
					}
				}
				return edges
			}
		}
	}
	return [][]int{}
}

func find(adjList [][]int, n int, src int, dst int) []int {
	distance := make([]int, n)
	for i := range distance {
		if i == src {
			continue
		}
		distance[i] = math.MaxInt32
	}
	pq := PriorityQueue{{src, 0}}
	heap.Init(&pq)
	visited := make([]bool, n)
	for pq.Len() > 0 {
		state := heap.Pop(&pq).(*State)
		if visited[state.node] {
			continue
		}

		visited[state.node] = true
		for child, cost := range adjList[state.node] {
			if cost == 0 {
				continue
			}
			if distance[child] > state.cost+cost {
				distance[child] = state.cost + cost
				heap.Push(&pq, &State{child, distance[child]})
			}
		}
	}
	return distance
}

type State struct {
	node int
	cost int
}

type PriorityQueue []*State

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].cost < pq[j].cost }
func (pq PriorityQueue) Swap(i, j int)      { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
	state := x.(*State)
	*pq = append(*pq, state)
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	state := old[n-1]
	*pq = old[0 : n-1]
	return state
}