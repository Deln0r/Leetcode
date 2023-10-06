class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        if n == 2:
            return 1
        elif n == 3:
            return 2
        while n > 4:
            res = res * 3
            n-=3
        return res*n
