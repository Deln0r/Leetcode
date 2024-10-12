class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            cur = num
            new_num = 0
            while cur:
                cur, d = divmod(cur, 10)
                new_num += d
            num = new_num
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        l = sum([int(n) for n in str(num)])
        while l > 9:
            l = sum([int(n) for n in str(l)])
        return l

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            new_num = 0
            temp = num
            while temp:
                temp, d = divmod(temp, 10)
                new_num += d
            num = new_num
        return num