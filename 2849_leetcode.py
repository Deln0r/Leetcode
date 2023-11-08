class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(sy-fy)
        height = abs(sx-fx)
        abshw = abs(width-height)

        minTime = abshw + min(width, height)

        if minTime == 0 and t == 1:
            return False
        
        if minTime <= t:
            return True
        
        return False
