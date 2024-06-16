class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = maxSum = patches = 0
        while maxSum < n:
            if i < len(nums) and nums[i] <= maxSum + 1:
                maxSum += nums[i]
                i += 1
            else:
                maxSum += (maxSum + 1)
                patches += 1
        return patches