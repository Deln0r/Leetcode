class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sen in sentences:
            num = sen.count(' ') + 1
            if ans <= num:
                ans = num
        return ans