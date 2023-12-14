from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[0]*n for _ in range(m)]
        orow, ocol, zrow, zcol = [0]*m, [0]*n, [0]*m, [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    orow[i] += 1
                    ocol[j] += 1
                else:
                    zrow[i] += 1
                    zcol[j] += 1

        for i in range(m):
            for j in range(n):
                diff[i][j] = orow[i] + ocol[j] - zrow[i] - zcol[j]
                
        return diff
