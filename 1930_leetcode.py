class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        unq_str = set(s)
        for ch in unq_str:
            st = s.find(ch)
            ed = s.rfind(ch)
            if st<ed:
                res+=len(set(s[st+1:ed]))
        
        return res
