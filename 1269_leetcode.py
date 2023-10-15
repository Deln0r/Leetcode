class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(steps//2 + 1, arrLen)
        dp = [1] + [0]*n
        for _ in range(steps):
            prev=0
            for i in range(n):
                dp[i], prev =(prev + dp[i] + dp[i + 1]), dp[i]
        return dp[0] % (10**9+7)
