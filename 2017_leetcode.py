class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float('inf')
        leftBottom, rightTop = 0, sum(grid[0])
        for a, b in zip(grid[0], grid[1]):
            rightTop -= a
            res = min(res, max(rightTop, leftBottom))
            leftBottom += b
        return res