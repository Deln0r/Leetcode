class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        n = len(s)
        w = sum(1 for i in range(k) if s[i] == "W")
        minw = w
        for i in range(k, n):
            if s[i] == "W": w += 1
            if s[i - k] == "W": w -= 1
            minw = min(minw, w)
        return minw