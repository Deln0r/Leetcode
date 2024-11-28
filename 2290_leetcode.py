class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        heapify(q)
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 0
        heappush(q, (0, 0, 0))
        while q:
            wt, x, y = heappop(q)
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                r, c = x + dx, y + dy
                if 0<=r<n and 0<=c<m:
                    if grid[r][c] == 1 and dist[r][c] > wt + 1:
                        dist[r][c] = wt + 1
                        heappush(q, (dist[r][c], r, c))
                    elif grid[r][c] == 0 and dist[r][c] > wt:
                        dist[r][c] = wt
                        heappush(q, (dist[r][c], r, c))
        return dist[n-1][m-1]   