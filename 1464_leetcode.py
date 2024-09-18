class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return ((nums[len(nums)-2]-1)*(nums[len(nums)-1]-1))

#0(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 1
        max2 = 1
        for n in nums:
            if n >= max1 and n >= max2:
                max2 = max1
                max1 = n
            elif n >= max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)