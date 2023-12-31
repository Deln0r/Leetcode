class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a=[]
        for i in range(0,len(s)-1) :
            b=0
            for j in range(i+1,len(s)) :
                if s[j]==s[i] :
                    b=j-i-1
                    a.append(b)
        return max(a) if len(a)>0 else -1
