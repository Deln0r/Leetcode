class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_1 = max(nums)
        nums.remove(max_1)
        max_2 = max(nums)

        min_1 = min(nums)
        nums.remove(min_1)
        min_2 = min(nums)


        return (max_1 * max_2) - (min_1 * min_2)
