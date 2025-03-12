from bisect import bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_non_negative = bisect_left(nums, 0)
        first_positive = bisect_left(nums, 1)

        neg = first_non_negative
        pos = len(nums) - first_positive

        return max(neg,pos)