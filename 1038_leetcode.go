func dfs(root *TreeNode, sum *int) {
	if root.Left == nil && root.Right == nil {
		(*sum) += root.Val
		root.Val = *sum
		return
	}
	if root.Right != nil {
		dfs(root.Right, sum)
	}
	(*sum) += root.Val
	root.Val = *sum
	if root.Left != nil {
		dfs(root.Left, sum)
	}
}
func bstToGst(root *TreeNode) *TreeNode {
	sum := 0
	dfs(root, &sum)
	return root
}