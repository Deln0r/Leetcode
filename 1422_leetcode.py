class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        n = len(s)
        zero=0
        l=[]
        for i in range(n-1) :
            if s[i]=='0' :
                zero+=1
                l+=[one+zero]
            else:
                one-=1
                l+=[one+zero]
        return max(l)
