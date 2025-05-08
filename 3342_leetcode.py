from bisect import bisect_left

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        offsets = [(1,0),(0,1),(-1,0),(0,-1)]
        n, m = len(moveTime), len(moveTime[0])
        options = [[0,0,0,1]]
        moveTime[0][0] = -1

        while True:
            t, x, y, dt = options.pop(0)
            for dx, dy in offsets:
                x_new, y_new = x+dx, y+dy
                if 0 <= x_new < n and 0 <= y_new < m and moveTime[x_new][y_new] != -1: 
                    t_new = max(t, moveTime[x_new][y_new]) + dt
                    if x_new == n-1 and y_new == m-1:
                        return t_new

                    entry = [t_new, x_new, y_new, dt%2 + 1]
                    idx = bisect_left(options, entry)
                    options.insert(idx, entry)

                    moveTime[x_new][y_new] = -1