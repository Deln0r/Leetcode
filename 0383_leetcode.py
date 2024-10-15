class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mag = Counter(magazine)

        for k in rn:
            if rn[k] > mag[k]:
                return False
        return True