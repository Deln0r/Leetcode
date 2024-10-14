class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        full_sum = sum(range(1, len(grid)**2+1))
        grid_sum = 0
        ans = [0,0]

        for i in grid:
            for j in i:
                if j in seen:
                    ans[0] = j
                seen.add(j)
                grid_sum += j
        ans[1] = full_sum - (grid_sum - ans[0])
        return ans