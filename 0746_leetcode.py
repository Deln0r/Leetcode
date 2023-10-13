class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0],cost[1]]
        for i in range(2,len(cost)):
            dp[i%2] = cost[i] + min( dp[0] , dp[1])
        return min(dp[0],dp[1])
