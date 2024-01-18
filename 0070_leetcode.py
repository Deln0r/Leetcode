class Solution:
    def climbStairs(self, n: int) -> int:
        
        fib_series = [0, 1]
        while len(fib_series) < n:
                fib_series.append(fib_series[-1] + fib_series[-2])
        if n==1:
            return 1  
        return sum(fib_series)+1