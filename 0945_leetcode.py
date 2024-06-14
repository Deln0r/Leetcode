class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        last = nums[0]
        result = 0
        for x in nums[1:]:
            if x <= last:
                result += last - x + 1
            else:
                last = x
                continue
            last = last + 1
        return result