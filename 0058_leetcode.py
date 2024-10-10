class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        i = len(s)-1
        while i>=0 and s[i]!=' ':
            i-=1

        return len(s)-i-1
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                ans += 1
            elif s[i] == ' ' and ans != 0:
                return ans
        return ans
    

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])