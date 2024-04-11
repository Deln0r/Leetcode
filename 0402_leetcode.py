class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = ""
        for digit in num :
            while len(s) > 0 and k > 0 and s[-1] > digit : 
                k -= 1
                s = s[:-1]

            if len(s) > 0 or digit != '0' :
                s += digit

        while len(s) > 0 and k > 0 :
            k -= 1
            s = s[:-1]

        return '0' if len(s) == 0 else s