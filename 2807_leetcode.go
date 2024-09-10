func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	curr := head
	for curr != nil && curr.Next != nil {
		nextBackup := curr.Next
		curr.Next = &ListNode{Val: GCD(curr.Val, nextBackup.Val), Next: nextBackup}
		curr = nextBackup
	}
	return head
}