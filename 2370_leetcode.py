class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l=[0]*128
        for j in s:
            c=ord(j)
            l[c]=max(l[c-k:c+k+1])+1
        
        return max(l)