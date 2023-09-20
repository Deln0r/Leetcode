class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        targetSum = sum(nums) - x
        if targetSum <= 0:
            return -1 if targetSum < 0 else len(nums)
        
        largestWindow = -1
        curSum = 0
        left = 0
        
        for right, num in enumerate(nums):
            curSum += num
            while curSum > targetSum:
                curSum -= nums[left]
                left += 1
                
            if curSum == targetSum:
                largestWindow = max(largestWindow, right - left + 1)
        
        return len(nums) - largestWindow if largestWindow != -1 else -1
