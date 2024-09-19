class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        nums = [0]+nums

        ans = 0
        len_ = len(nums)
        for i in range(1, len_):
            if (len_-1) % i == 0:
                ans += nums[i]*nums[i]
        return ans