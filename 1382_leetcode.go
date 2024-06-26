/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func balanceBST(root *TreeNode) *TreeNode {
	// Шаг 1: Собрать все узлы в отсортированный массив
	nodes := []int{}
	inorderTraversal(root, &nodes)

	// Шаг 2: Построить сбалансированное дерево из отсортированного массива
	return sortedArrayToBST(nodes)
}

// Функция для обхода дерева в порядке возрастания и сборки узлов в массив
func inorderTraversal(root *TreeNode, nodes *[]int) {
	if root == nil {
		return
	}
	inorderTraversal(root.Left, nodes)
	*nodes = append(*nodes, root.Val)
	inorderTraversal(root.Right, nodes)
}

// Функция для построения сбалансированного дерева из отсортированного массива
func sortedArrayToBST(nodes []int) *TreeNode {
	if len(nodes) == 0 {
		return nil
	}
	mid := len(nodes) / 2
	root := &TreeNode{Val: nodes[mid]}
	root.Left = sortedArrayToBST(nodes[:mid])
	root.Right = sortedArrayToBST(nodes[mid+1:])
	return root
}