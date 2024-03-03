class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for i in range(n):
            first = first.next

        if not first:
            return head.next

        while first.next:
            second = second.next
            first = first.next

        second.next = second.next.next

        return head