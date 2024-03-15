class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(x):
            if x < 0:
                return 0
            l,prefix_sum = 0, 0
            res = 0
            for r in range(len(nums)):
                prefix_sum += nums[r]
                while prefix_sum>x:
                    prefix_sum = prefix_sum - nums[l]
                    l = l+1
                res += (r-l+1)
            return res
        return helper(goal) - helper(goal-1)