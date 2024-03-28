from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        res = 0
        M = {}
        
        for i in range(n):
            M[nums[i]] = M.get(nums[i], 0) + 1
            
            while M[nums[i]] > k:
                M[nums[j]] -= 1
                j += 1
            
            res = max(res, i - j + 1)
        
        return res