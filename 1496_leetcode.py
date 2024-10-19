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

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = {(x, y)}

        for step in path:
            if step == 'N':
                y += 1
            elif step == 'S':
                y -= 1
            elif step == 'E':
                x += 1
            elif step == 'W':
                x -= 1
            
            if (x, y) in seen:
                return True
            else:
                seen.add((x,y))
        return False
    
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = {(x, y)}
        d = {'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}

        for step in path:
            dx, dy = d[step]
            x += dx
            y += dy
            
            if (x, y) in seen:
                return True
            else:
                seen.add((x,y))
        return False
