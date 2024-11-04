class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        cnt = 1
        prev = word[0]
        for ind, ch in enumerate(word[1:]):
            if ch == prev and cnt<9:
                cnt += 1
                continue
            res.append(f"{cnt}{prev}")
            cnt = 1
            prev = ch
        res.append(f"{cnt}{prev}")
        return ''.join(res)