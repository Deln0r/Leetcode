class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        prev1 = False
        prev2 = False
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] ^ prev1 ^ prev2:
                prev2 = prev1
                prev1 = False
            else:
                res += 1
                prev2 = prev1
                prev1 = True
        return res if nums[N-1] ^ prev1 and nums[N-2] ^ prev1 ^ prev2 else -1