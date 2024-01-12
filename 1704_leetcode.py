class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=['a','e','i','o','u','A','E','I','O','U']
        n=len(s)
        cnt1=0
        cnt2=0
        for i in range(n//2):
            if s[i] in l:
                cnt1+=1
        for i in range(n//2):
            if s[n-i-1] in l:
                cnt2+=1  
        return cnt1==cnt2