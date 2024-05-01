class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        l = word.index(ch)

        return word[:l+1][::-1]+word[l+1:]