class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum([k for k in c.keys() if c[k]==1])


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = {}
        for n in nums:
            if n not in c:
                c[n] = 1
            else:
                c[n] += 1
        ans = 0
        for n in nums:
            if c[n] == 1:
                ans += n

        return ans