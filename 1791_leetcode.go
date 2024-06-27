func findCenter(edges [][]int) int {
	node1, node2 := edges[0][0], edges[0][1]
	node3, node4 := edges[1][0], edges[1][1]
	if node3 == node1 || node3 == node2 {
		return node3
	}
	return node4
}