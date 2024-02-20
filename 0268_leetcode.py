class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return next(i for i in range(len(nums) + 1) if i not in nums)