import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, value = 0, 0
        while(value <= c):
            if(value == c):
                return True
            x = c - value
            x = math.sqrt(x)
            if(x == int(x)):
                return True
            i += 1
            value = i * i
        return False  