class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        max_ = float('-inf')
        min_ = float('inf')

        for i in range(len(nums)):
            if nums[i] > max_:
                max_ = nums[i]
            if nums[i] < min_:
                min_ = nums[i]
        for i in range(len(nums)):
            if nums[i] != max_ and nums[i] != min_:
                return nums[i]
        return -1