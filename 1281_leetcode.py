import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [int(i) for i in str(n)]
        return math.prod(arr) - sum(arr)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        prod = 1

        while n:
            d = n % 10
            n = n // 10
            summ += d
            prod *= d
        
        return prod - summ