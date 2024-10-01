class Solution:
    def isMonotonic(self, nums:list[int]) -> bool:
        increasing_index = True
        decreasing_index = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing_index = False
            elif nums[i] < nums[i - 1]:
                increasing_index = False

        return increasing_index or decreasing_index
    
    

class Solution:
    def isMonotonic(self, nums:list[int]) -> bool:
        inc = True
        dec = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dec = False
            elif nums[i] < nums[i-1]:
                inc = False
        return inc or dec
