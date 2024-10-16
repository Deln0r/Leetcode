class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            counter = 0
            for num1 in nums:
                if num1 < num:
                    counter += 1
            ans.append(counter)
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        s_nums = sorted(nums)
        for num in nums:
            ans.append(s_nums.index(num))
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        s_nums = sorted(nums)

        d = {}
        for i, n in enumerate(s_nums):
            if n not in d:
                d[n] = i

        for num in nums:
            ans.append(d[num])
        return ans