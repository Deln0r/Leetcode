func modifiedList(nums []int, head *ListNode) *ListNode {
	shadowHead := &ListNode{
		Val:  65535,
		Next: head,
	}
	hash := make(map[int]bool, len(nums))
	for _, v := range nums {
		hash[v] = true
	}
	for prevNode, curNode := shadowHead, shadowHead.Next; curNode != nil; curNode = curNode.Next {
		if hash[curNode.Val] != true {
			prevNode = curNode
			continue
		}
		prevNode.Next = curNode.Next
	}
	return shadowHead.Next
}