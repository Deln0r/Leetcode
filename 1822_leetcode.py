class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if (n > 0 and ans > 0) or (n < 0 and ans < 0):
                ans = 1
            elif n < 0 or ans < 0:
                ans = -1
            else:
                return 0

        return ans