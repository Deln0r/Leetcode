class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            
            first = helper(n - 3) + 1
            second = helper(n - 2) + 1
            return min(first, second)

        counter = Counter(nums)
        result = 0
        for v in counter.values():
            val = helper(v)
            if val == float('inf'):
                return -1
            result += helper(v)
        return result
