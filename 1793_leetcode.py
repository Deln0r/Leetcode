class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn = nums[k]
        lo = hi = k
        while 0 <= lo-1 or hi+1 < len(nums): 
            if lo == 0 or hi+1 < len(nums) and nums[lo-1] < nums[hi+1]: 
                hi += 1
                mn = min(mn, nums[hi])
            else: 
                lo -= 1
                mn = min(mn, nums[lo])
            ans = max(ans, mn * (hi-lo+1))
        return ans
