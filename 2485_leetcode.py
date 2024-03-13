class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = sum(range(n + 1))
        for i in range(n + 1):
            left += i
            if left == right:
                return i
            right -= i
        return -1