class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if s == '1':
            return True

        len0 = 0
        len1 = 0

        counter0 = 0
        counter1 = 0

        for n in s:
            if n == '0':
                counter0 += 1
                if counter0 > len0:
                    len0 = counter0
                counter1 = 0
            else:
                counter1 += 1
                if counter1 > len1:
                    len1 = counter1
                counter0 = 0
        return len1 - len0 >= 1