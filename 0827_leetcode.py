class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def is_in_bounds(i,j):
            return True if (i>=0 and i<len(grid) and j >= 0 and j < len(grid)) else False

        seen = set()
        max_area = 0
        def bfs(i,j):
            stack = [(i,j)]
            steps = [(0,1),(1,0),(-1,0),(0,-1)]
            count = 1
            seen.add((i,j))
            curr_seen = set()
            island_shore = set()
            while stack:
                curr = stack.pop()
                for step in steps:
                    newi, newj = curr[0]+step[0], curr[1]+step[1]
                    if is_in_bounds(newi, newj) and (newi, newj) not in seen:
                        if grid[newi][newj] == 1:
                            stack.append((newi,newj))
                            seen.add((newi,newj))
                            count+=1
                        else:
                            island_shore.add((newi,newj))
            
            for (shorex, shorey) in island_shore:
                grid[shorex][shorey] -= count

            return count

        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] == 1 and (i,j) not in seen:
                    max_area = max(max_area, bfs(i,j))
        
        if max_area == 0:
            return 1

        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] < 0:
                    max_area = max(max_area, (grid[i][j]*-1)+1)
        
        return max_area