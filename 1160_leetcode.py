class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=[]
        for i in words:
            for j in i:
                if chars.count(j) < i.count(j): 
                    break
            else:
                length.append(len(i))
        return sum(length)


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        ch = Counter(chars)

        for word in words:
            w = Counter(word)
            good = True
            for c in w:
                if w[c] > ch[c]:
                    good = False
            if good:
                ans += len(word)
        return ans
