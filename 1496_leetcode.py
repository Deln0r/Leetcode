class Solution:
    def isPathCrossing(self, path: str) -> bool:
        h=set()
        x=0
        y=0
        h.add((0,0))
        for p in path:
            if p=="N":
                x+=1
            if p=="S":
                x-=1
            if p=="E":
                y-=1
            if p=="W":
                y+=1
            if (x,y) in h:
                return True
            h.add((x,y))
            
        return False
