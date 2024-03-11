class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=defaultdict(int)
        i=0
        for c in order:
            ans[c]=i
            i+=1
        return "".join(sorted(s,key=lambda x:ans.get(x,100)))