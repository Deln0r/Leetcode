/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
	sum := 0
	dummyHead := &ListNode{}
	prev := dummyHead

	for p := head.Next; p != nil; p = p.Next {
		if p.Val == 0 {
			node := &ListNode{Val: sum}
			prev.Next = node
			prev = node
			sum = 0
		} else {
			sum += p.Val
		}
	}

	return dummyHead.Next
}

// Helper function to create a linked list from a slice of integers.
func createLinkedList(arr []int) *ListNode {
	dummyHead := &ListNode{}
	current := dummyHead
	for _, val := range arr {
		current.Next = &ListNode{Val: val}
		current = current.Next
	}
	return dummyHead.Next
}

// Helper function to print the linked list.
func printLinkedList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, " -> ")
		head = head.Next
	}
	fmt.Println("nil")
}