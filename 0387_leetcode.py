class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        return min([i for i in range(len(s)) if c[s[i]] == 1], default = -1)