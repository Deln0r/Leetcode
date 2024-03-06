class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address = []
        curr = head
        while(curr is not None):
            address.append(curr)
            curr = curr.next
            if(curr in address):
                return True
        return False