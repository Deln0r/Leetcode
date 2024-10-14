class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for i in s:
            if i in seen:
                return i
            seen.add(i)