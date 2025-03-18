class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        for i, orv in enumerate(nums):
            j = i - 1
            while j >= 0 and (orv & nums[j] == 0):
                orv |= nums[j]
                j -= 1
            ans = max(ans, i - j)
        return ans