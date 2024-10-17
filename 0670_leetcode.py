class Solution:
    def maximumSwap(self, num: int) -> int:
        i, j = None, None
        num = list(str(num))
        mx = len(num) - 1
        for n in range(len(num)-1, -1, -1):
            if num[n] > num[mx]:
                mx = n
            elif num[n] < num[mx]:
                i, j = n, mx
        if i is not None and j is not None:
            num[i], num[j] = num[j], num[i]
        return int("".join(num))