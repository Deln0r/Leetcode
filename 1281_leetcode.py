import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [int(i) for i in str(n)]
        return math.prod(arr) - sum(arr)
