/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distributeCoins(root *TreeNode) int {
	moves := 0

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		leftBalance := dfs(node.Left)
		rightBalance := dfs(node.Right)

		// Calculate the balance for the current node:
		//   - positive balance: excess coins to give away
		//   - negative balance: need coins
		balance := node.Val - 1 + leftBalance + rightBalance

		// Update the total number of moves based on the absolute value of the balance
		moves += abs(balance)

		return balance // Propagate the balance to the parent
	}

	dfs(root)
	return moves
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}