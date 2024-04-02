class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(set(s))
        m=len(set(t))
        z=len(set(zip(s,t)))
        return n==m==z