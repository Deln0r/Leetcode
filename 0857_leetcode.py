class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans=inf
        rsm=0
        stack=[]
        for q,w in sorted(zip(quality,wage),key=lambda x:x[1]/x[0]):
            rsm+=q
            heappush(stack,-q)
            if len(stack)>k:
                rsm+=heappop(stack)
            if len(stack)==k:
                ans=min(ans,rsm*w/q)
        return ans  