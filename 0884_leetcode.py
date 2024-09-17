class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l = s1.split()
        r = s2.split()
        combined = l+r
        w_count = Counter(combined)
        res = [word for word in w_count if w_count[word]==1]
        
        return res