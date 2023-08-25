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
