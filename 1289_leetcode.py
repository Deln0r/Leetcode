class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[grid[i][j] for j in range(n)] for i in range(n)]
    
        def getMin(arr): #O(n)
            res,r = [float('inf')]*n,[float('inf')]*n
            for i in range(1,n):
                res[i] = min(res[i],res[i-1],arr[i-1])
            for i in range(n-2,-1,-1):
                r[i] = min(r[i],r[i+1],arr[i+1])
                res[i] = min(r[i],res[i])
            return res

        for i in range(1,n): #O(n^2)
            minLast = getMin(dp[i-1]) #O(n)
            for j in range(n): #O(n)
                dp[i][j] = grid[i][j] + minLast[j]

        return min(dp[-1])