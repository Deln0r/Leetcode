class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        c=0
        l=len(w)
        for i in range(l):
            for j in range(i+1,l):
                if w[j].startswith(w[i]) and w[j].endswith(w[i]):
                    c+=1
        return c