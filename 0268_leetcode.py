class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return next(i for i in range(len(nums) + 1) if i not in nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num2 = set([i for i in range(0, len(nums)+1)])
        return (num2 - set(nums)).pop()

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)