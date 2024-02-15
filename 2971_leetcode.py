class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefixsum = sum(nums)
        while nums and 2*nums[-1] >= prefixsum:
            prefixsum -= nums.pop()
        if len(nums) < 3: return -1
        return sum(nums)