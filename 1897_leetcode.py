class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words)
        d = defaultdict(int)
        for w in words: 
            for c in w:
                d[c] += 1
        for key in d: 
            if d[key] % N: 
                return False
        return True
