class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for n in nums:
            ans.append(abs(left - (right - n)))
            left += n
            right -= n
        return ans