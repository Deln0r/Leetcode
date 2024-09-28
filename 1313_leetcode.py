class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0 ,len(nums), 2):
            ans += [nums[i+1]] * nums[i]
        return ans
    

class Solution:
    def decompressRLElist(self, N: List[int]) -> List[int]:
        L, A = len(N), []
        for i in range(0,L,2):
            A.extend(N[i]*[N[i+1]])
        return A