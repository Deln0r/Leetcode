class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n=len(cost)
        @cache
        def f(i, walls):
            if walls>=n: return 0
            if i>=n: 
                return 2**31+1
            ans=cost[i]+f(i+1, walls+1+time[i])
            ans=min(ans, f(i+1, walls))          
            return ans
        return f(0, 0)
