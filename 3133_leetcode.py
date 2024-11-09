class Solution:
    def minEnd(self, n: int, x: int):
        fill = n - 1
        maskFill = 1
        mask = 1
        ret = x

        while fill > 0:
            while mask & x > 0:
                mask <<= 1
            if maskFill & fill > 0:
                fill ^= maskFill
                ret |= mask

            maskFill <<= 1
            mask <<= 1

        return ret