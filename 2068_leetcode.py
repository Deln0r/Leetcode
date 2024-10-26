class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        for char in set(counter1.keys()).union(set(counter2.keys())):
            if abs(counter1[char] - counter2[char]) > 3:
                return False

        return True