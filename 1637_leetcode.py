class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=[]
        for i in range(len(points)):
            l.append(points[i][0])
        l.sort()
        if(len(l)==0 or len(l)==1):
            return 0
        c=0
        for i in range(len(l)-1,0,-1):
            d=l[i]-l[i-1]
            if(c<d):
                c=d
        return c
