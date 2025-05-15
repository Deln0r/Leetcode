class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        curBinary = groups[0]
        ansList = [words[0]]
        for idx in range(1, N):
            if curBinary != groups[idx]:
                ansList.append(words[idx])
                curBinary = groups[idx]

        return ansList