class Solution:
    def trap(self, h: List[int]) -> int:
        res, stack = 0, []
        
        for r, rightBound in enumerate(h):
            while stack and h[stack[-1]] < rightBound:
                bar = h[stack.pop()]
                if stack:
                    l, leftBound = stack[-1], h[stack[-1]]
                    minBound = min(rightBound, leftBound)
                    res += (r - l - 1) * (minBound - bar)
            stack.append(r)
        
        return res