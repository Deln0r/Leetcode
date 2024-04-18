class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    answer+=(i==0 or grid[i-1][j]==0)+(j==0 or grid[i][j-1]==0)+(i==n-1 or grid[i+1][j]==0)+(j==m-1 or grid[i][j+1]==0)
        return answer