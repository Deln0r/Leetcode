class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            lower_bound = r - l
            upper_bound = min(height[l],height[r])
            area = lower_bound * upper_bound
            max_water = max(max_water,area)
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1
        return max_water