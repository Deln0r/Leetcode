class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = post = 1
        n = len(nums)
        res = [1] * n

        for i in range(n):
            if i > 0:
                pre = pre * nums[i - 1]
            res[i] = pre
        
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res