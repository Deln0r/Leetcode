class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if (sum(nums) + target) % 2 != 0 or sum(nums) < abs(target):
            return 0
        
        subtarget = (sum(nums) + target)//2

        dp = [0] * (subtarget+1)
        dp[0] = 1

        for num in nums:
            for i in range(subtarget, num-1, -1):
                dp[i] = dp[i-num] + dp[i]
        
        return dp[subtarget]