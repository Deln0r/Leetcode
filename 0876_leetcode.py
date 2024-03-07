class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow