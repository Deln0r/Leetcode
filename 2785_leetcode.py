class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = "AEIOUaeiou"
        q = deque(sorted(c for c in s if c in VOWELS))
        return "".join(q.popleft() if c in VOWELS else c for c in s)