class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = end = list1
        cnt = 0
        while cnt < b:
            cnt += 1
            if cnt < a:
                start = start.next
            end = end.next

        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = end.next

        start.next = list2

        return list1