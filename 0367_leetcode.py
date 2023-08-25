class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num ** 0.5
        return int(n) == float(n)
