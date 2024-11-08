class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i==i[::-1]:
                 return i
        return ""
    

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l, r = 0, len(i)-1
            flag = True
            while l<r:
                if i[l] != i[r]:
                    flag = False
                    break
                l+=1
                r-=1
            if flag:
                return i
        return ""