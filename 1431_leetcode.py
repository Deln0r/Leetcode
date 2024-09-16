class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        m = max(candies)
        for c in candies:
            ans.append(c + extraCandies >= m)
        return ans