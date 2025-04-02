class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        postfix = [0] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], nums[i])
        
        # Monotonic increasing stack
        stack = []

        res = 0

        for i in range(len(nums) - 1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])
            
            if stack:
                res = max(res, (stack[0] - stack[-1]) * postfix[i + 1])
        
        return res