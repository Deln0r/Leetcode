class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        left = 0
        right = sum(nums)
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i-1
        return -1