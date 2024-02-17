class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        ans=0
        for i in sorted(c.values()):
            if i <= k:
                k-=i
                ans+=1
        return len(c)-ans