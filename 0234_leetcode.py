class Solution(object):
    def isPalindrome(self, head):
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        # using stack is like reversing linked list 
        while curr and curr.val == stack.pop():
            curr = curr.next
        # reach the end of stack 
        return curr is None