class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cumsum = 0
        for i in range(len(nums)):
            ans.append(nums[i] + cumsum)
            cumsum += nums[i]
        return ans