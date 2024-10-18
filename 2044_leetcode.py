class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        pool = Counter()
        for curr in nums:
            pool[0] = 1
            for prev, times in [*pool.items()]:
                pool[prev|curr] += times
        return pool.most_common(1)[0][1]