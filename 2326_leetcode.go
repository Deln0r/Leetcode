/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	matrix := make([][]int, m)
	for i := range matrix {
		matrix[i] = make([]int, n)
		for j := range matrix[i] {
			matrix[i][j] = -1
		}
	}

	top, bottom, left, right := 0, m-1, 0, n-1

	current := head

	for current != nil {
		for i := left; i <= right && current != nil; i++ {
			matrix[top][i] = current.Val
			current = current.Next
		}
		top++

		for i := top; i <= bottom && current != nil; i++ {
			matrix[i][right] = current.Val
			current = current.Next
		}
		right--

		for i := right; i >= left && current != nil; i-- {
			matrix[bottom][i] = current.Val
			current = current.Next
		}
		bottom--

		for i := bottom; i >= top && current != nil; i-- {
			matrix[i][left] = current.Val
			current = current.Next
		}
		left++
	}

	return matrix
}