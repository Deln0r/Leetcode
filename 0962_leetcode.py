class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]

        for i, x in enumerate(nums):
            if stack and x < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for x in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[x]:
                ans = max(ans, x - stack.pop())
        
        return ans