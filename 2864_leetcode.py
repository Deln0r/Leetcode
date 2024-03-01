class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        s = list(s)

        for i in range(len(s)):
            if s[i] == '1':
                s[i] = '0'
                ones += 1

        if ones > 1:
            for i in range(ones - 1):
                s[i] = '1'
        s[-1] = '1'

        return ''.join(s)