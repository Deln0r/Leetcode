class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s

        a = ['']*n
        k = index = 0

        for letter in s:
            a[k%n] += letter

            if k == n-1:
                index = 1
            if k == 0:
                index = 0
            k = k+1 if index == 0 else k-1

        result = a[0]
        for i in a[1:]:
            result += i
        return result