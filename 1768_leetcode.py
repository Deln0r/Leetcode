class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        p = 0
        while p < len(word1) and p < len(word2):
            ans.append(word1[p])
            ans.append(word2[p])
            p += 1
        if p == len(word1):
            ans.append(word2[p:])
        if p == len(word2):
            ans.append(word1[p:])
        return "".join(ans)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        sum_len = len(word1) + len(word2)
        for i in range(sum_len):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])
        return "".join(ans)