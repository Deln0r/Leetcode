class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        sum_map = {}
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current:
            prefix_sum += current.val
            sum_map[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy

        while current:
            prefix_sum += current.val
            current.next = sum_map[prefix_sum].next
            current = current.next

        return dummy.next