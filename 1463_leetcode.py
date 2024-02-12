class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        prev = [[0] * m for _ in range(m)]
        curr = [[0] * m for _ in range(m)]

        for r in (range(n-1, -1, -1)):
            for c1 in range(min(m,r+1)):
                for c2 in range(max(c1+1,m-(r+1)), m):
                    pick = grid[r][c1] + grid[r][c2]
                    if r == n-1:
                        curr[c1][c2] = pick
                        continue
                    ans = 0
                    for c1_n in (c1-1, c1, c1+1):
                        if not (0 <= c1_n < m): continue
                        if c1_n > r+1: break
                        for c2_n in (c2+1, c2, c2-1):
                            if c1_n >= c2_n: break
                            if c2_n < m-(r+2): break
                            if not (0 <= c2_n < m): continue
                            ans = max(ans, prev[c1_n][c2_n])
                    curr[c1][c2] = ans + pick
            prev, curr = curr, [[0] * m for _ in range(m)]
        
        return prev[0][m-1]