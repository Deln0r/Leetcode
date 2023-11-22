class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        grid=defaultdict(list)
        res=[]

        for row in range(len(nums)):
            for col in range(len(nums[row])):
                grid[row+col].append(nums[row][col])
        
        for d in sorted(grid.keys()):
            res.extend(grid[d][::-1])
        return res
