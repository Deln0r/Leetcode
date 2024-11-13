class Solution:
    def sumSmallerK(self, nums, k):
        res = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] <= k:
                res += j - i
                i += 1
            else:
                j -= 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        less_than_upper = self.sumSmallerK(nums, upper)
        less_than_lower = self.sumSmallerK(nums, lower-1)
        return less_than_upper - less_than_lower