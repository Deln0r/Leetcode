class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        inf = float('inf')
        if n < d:
            return -1
        if d == 1:
            return max(jobDifficulty)

        q = [[max(jobDifficulty[i:j + 1]) if i <= j else inf for j in range(n)]
             for i in range(n)]
        dp = [q[0][i] for i in range(n)]

        for _ in range(1, d - 1):
            dp1 = [inf for _ in range(n)]
            for i in range(n - 1):
                for j in range(i, -1, -1):
                    dp1[i] = min(dp1[i], dp[j - 1] + q[j][i])
            dp = dp1

        ans = inf
        for i in range(n - 1):
            ans = min(ans, dp[i] + q[i + 1][n - 1])
        return ans