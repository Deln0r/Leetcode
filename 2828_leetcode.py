class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first = []
        for w in words:
            first.append(w[0])
        return ''.join(first) == s