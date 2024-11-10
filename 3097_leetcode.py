class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        if ma >= k: return 1
        size = len(bin(ma)) - 2
        if size  < len(bin(k)) - 2: return -1
        
        counts = [0] * size
        masks = [1<<i for i in range(size+1)] # avoid calculation on the fly
        ans = inf
        l, s = 0, 0

        for r, v in enumerate(nums):
            i = 0
            while masks[i] <= v:
                if v & masks[i]:
                    counts[i] += 1
                i += 1
            s |= v
            while l < r and s >= k:
                if r - l < ans: # the correct size is (r - l + 1) 
                    ans = r - l # but eliminating +1 reduce 2 calculations
                v, i = nums[l], 0
                while masks[i] <= v:
                    m = masks[i]
                    if v & m:
                        counts[i] -= 1
                        if counts[i] == 0:
                            s &= ~m # reset bit i when count becomes 0
                    i += 1
                l += 1
                
        return ans + 1 if ans < inf else -1