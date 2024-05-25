class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, n in enumerate(nums):
            if n not in seen or abs(seen[n] - i) > k:
                seen[n] = i
            else:
                return True

        return False 