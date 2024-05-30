class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        n = len(s)
        total = 0
        for i in range(n):
            total += int(s[i]) * 2 ** (n - 1 - i)
        print(total)

        while total > 1:
            result += 1
            if total % 2 == 0:
                total //= 2
            else:
                total += 1

        return result