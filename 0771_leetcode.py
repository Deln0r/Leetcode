class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0

        for s in stones:
            if s in jewels:
                ans += 1
        return ans


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewels_set = set(jewels)

        for s in stones:
            if s in jewels_set:
                ans += 1
        return ans