class Solution:
    def moveZeroes(self, nums):
        arr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[arr] = nums[arr], nums[i]
                arr += 1
