func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	output := []int{}

	output = append(output, postorderTraversal(root.Left)...)
	output = append(output, postorderTraversal(root.Right)...)
	output = append(output, root.Val)
	return output
}