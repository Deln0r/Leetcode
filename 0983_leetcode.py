class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        memo = [0] * (max_day + 1)
        travel = [False] * (max_day + 1)
        memo[0] = 0
        for d in days:
            travel[d] = True

        for i in range(1, len(memo)):
            memo[i] = memo[i-1]
            if travel[i]:
                memo[i] = min(memo[i-1] + costs[0], memo[max(0, i-7)] + costs[1], memo[max(0,i-30)] + costs[2])
    
        return memo[-1]