class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i in range(-1, -len(colors), -1):
            if colors[i] != colors[0]:
                ans = max(ans, len(colors[:i]))
                break
        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                ans = max(ans, len(colors[i:-1]))
                break
        return ans