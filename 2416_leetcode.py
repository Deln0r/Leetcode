class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = {}
        for word in words:
            currLevel = d
            for char in word:
                if char not in currLevel:
                    currLevel[char] = [0, {}]
                currLevel[char][0] += 1
                currLevel = currLevel[char][1]

        prefixCounts = []
        for word in words:
            prefixCount = 0
            currLevel = d
            for char in word:
                prefixCount += currLevel[char][0]
                currLevel = currLevel[char][1]
            prefixCounts.append(prefixCount)

        return prefixCounts