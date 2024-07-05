func nodesBetweenCriticalPoints(head *ListNode) []int {
	if head == nil {
		return []int{-1, -1}
	} else if head.Next == nil {
		return []int{-1, -1}
	}
	var (
		first, last = -1, -1
		node, prev  = head.Next, head
		minDist     = 1 << 32
	)
	for pos := 0; node.Next != nil; pos++ {
		if prev.Val > node.Val && node.Val < node.Next.Val ||
			prev.Val < node.Val && node.Val > node.Next.Val {
			if last != -1 {
				if pos-last < minDist {
					minDist = pos - last
				}
			} else {
				first = pos
			}
			last = pos
		}

		prev, node = node, node.Next
	}

	if last == -1 || first == last {
		return []int{-1, -1}
	}

	return []int{minDist, last - first}
}