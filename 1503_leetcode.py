class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        t=0
        if left:
            t=max(left)
        if right:
            t=max(t,n-min(right))
        return t