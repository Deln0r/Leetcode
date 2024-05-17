/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
	if root == nil {
		return false // Handle the case where the tree is empty
	}

	// Base case: Leaf node
	if root.Left == nil && root.Right == nil {
		return root.Val == 1
	}

	leftResult := evaluateTree(root.Left)
	rightResult := evaluateTree(root.Right)

	switch root.Val {
	case 2: // OR
		return leftResult || rightResult
	case 3: // AND
		return leftResult && rightResult
	default:
		panic("Invalid node value") // Handle unexpected values
	}
}