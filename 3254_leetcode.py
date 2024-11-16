class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n = len(nums)
        ret = [-1] * (n - k + 1)
        cons = 1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                cons += 1
            else:
                cons = 1

            if cons >= k:
                ret[i - k + 2] = nums[i + 1]
        return ret