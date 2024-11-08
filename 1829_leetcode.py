class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [0]*len(nums)
        max_XOR = pow(2,maximumBit)-1
        xor_till_now = 0 
        i = -1
        for n in nums:
            xor_till_now ^= n
            ans[i]=max_XOR ^ xor_till_now
            i-=1
        return ans