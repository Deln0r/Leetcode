# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=l1
        last=0
        carry=ListNode()
        while l1 and l2:
            temp=l1.val+l2.val+carry.val
            carry.val=temp//10
            l1.val=temp%10
            last=l1
            l1=l1.next
            l2=l2.next
        if l2: #if l2 has more nodes than l1
            last.next=l2
            l1=l2
        while l1 and carry.val:
            temp=l1.val+carry.val
            carry.val=temp//10
            l1.val=temp%10
            last=l1
            l1=l1.next
        if carry.val:
            last.next=carry
        return res