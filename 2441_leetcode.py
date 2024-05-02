class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        large = -1
        while start < end:
            negative, positive = nums[start], nums[end]
            if negative > 0:
                break
            if abs(negative) == positive:
                large = positive
                break
            if abs(negative) < positive:
                end -= 1
            else:
                start += 1
        return large