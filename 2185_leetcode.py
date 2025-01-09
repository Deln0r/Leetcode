class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            if word.find(pref) == 0:
                count += 1
        return count