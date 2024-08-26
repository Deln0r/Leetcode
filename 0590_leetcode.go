func postorder(root *Node) []int {
	result := []int{}
	if root == nil {
		return result
	}

	var traverse func(*Node)
	traverse = func(node *Node) {
		if node == nil {
			return
		}

		for _, child := range node.Children {
			traverse(child)
		}

		result = append(result, node.Val)
	}

	traverse(root)
	return result
}