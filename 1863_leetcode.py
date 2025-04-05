from functools import lru_cache
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(index, xor):
            if index >= len(nums):
                return xor
            pick = dfs(index + 1, nums[index] ^ xor)  # include current element
            skip = dfs(index + 1, xor)                # exclude current element
            return pick + skip
        return dfs(0, 0)