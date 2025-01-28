class Solution:
    def dfs(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= nrow or j >= ncol:
            return 0
        if grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        return temp + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)

    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        nrow, ncol = len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 0:
                    res = max(res, self.dfs(grid, i, j))
        return res

        