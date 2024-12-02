class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        words = sentence.split()
        for i, word in enumerate(words):
            if word[:n] == searchWord:
                return i + 1

        return -1