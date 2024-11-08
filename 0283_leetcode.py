class Solution:
    def moveZeroes(self, nums):
        arr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[arr] = nums[arr], nums[i]
                arr += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
            else:
                r+=1
