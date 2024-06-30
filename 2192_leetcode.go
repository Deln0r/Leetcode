package main

func bfs(start int, graph [][]int, res [][]int, n int) {
	visited := make([]bool, n)
	visited[start] = true
	var queue []int
	queue = append(queue, start)
	for {
		if len(queue) == 0 {
			break
		}
		u := queue[0]
		queue = queue[1:]
		for _, v := range graph[u] {
			if visited[v] == false {
				visited[v] = true
				queue = append(queue, v)
				res[v] = append(res[v], start)
			}
		}
	}
}
func getAncestors(n int, edges [][]int) [][]int {
	res := make([][]int, n)
	graph := make([][]int, n)
	for _, x := range edges {
		graph[x[0]] = append(graph[x[0]], x[1])
	}

	for i := 0; i < n; i++ {
		bfs(i, graph, res, n)
	}
	return res
}
