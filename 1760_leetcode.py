class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(x,maxO):
            cnt = 0
            for n in nums:
            # ceiling of n//x is (n-1)//x+1, we want to add ceiling-1. 
                cnt += (n-1)//x
            return cnt<=maxO
        left = 0
        right = max(nums)+1
        while left+1<right:
            mid = left+(right-left)//2
            if check(mid,maxOperations):
                right = mid
            else:
                left = mid
        return right