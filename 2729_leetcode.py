class Solution:
    def isFascinating(self, n: int) -> bool:
        num = str(n) + str(2*n) + str(3*n)
        seen = set()

        for i in str(num):
            if i == '0' or i in seen:
                return False
            seen.add(i)
        return True