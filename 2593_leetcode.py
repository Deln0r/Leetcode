class Solution:
    def findScore(self, nums: List[int]) -> int:
        a = sorted([(i, n) for i, n in enumerate(nums)], key = lambda x: x[1])
        res, s = 0, set()
        for i, n in a:
            if i not in s:
                res += n
                s.add(i)
                s.add(i - 1)
                s.add(i + 1)
        return res
        