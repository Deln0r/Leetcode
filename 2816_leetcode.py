# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return 0
            
            cur_carry=helper(node.next)
            
            new_val=node.val*2+cur_carry
            node.val=new_val%10
            new_carry=new_val//10
            
            return new_carry

        
        carry=helper(head)
        if carry:
            return ListNode(1,head)
        return head