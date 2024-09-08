/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getLength(head *ListNode) int {
	length := 0
	for head != nil {
		length++
		head = head.Next
	}
	return length
}

func getList(curr *ListNode, head *ListNode, quo, rem int) (*ListNode, *ListNode) {
	if head == nil {
		return nil, nil
	}
	l := 0
	l += quo
	if rem != 0 {
		l += 1
	}
	ref := head
	prev := new(ListNode)
	prev = nil
	for i := 0; i < l; i++ {
		prev = head
		head = head.Next
	}
	curr = ref
	prev.Next = nil
	return curr, head
}

func splitListToParts(head *ListNode, k int) []*ListNode {
	ans := make([]*ListNode, 0)
	n := getLength(head)
	quo := n / k
	rem := n % k
	for i := 0; i < k; i++ {
		curr := new(ListNode)
		curr = nil
		curr, head = getList(curr, head, quo, rem)
		if rem != 0 {
			rem--
		}
		ans = append(ans, curr)
	}
	return ans
}