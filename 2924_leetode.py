class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        v,ans,c=[0]*n,-1,0
        for i,j in edges:
            v[j]+=1
        for i,j in enumerate(v):
            if not j:
                ans,c=i,c+1
        return  -1 if c>1 else ans