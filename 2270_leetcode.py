class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_Sum, count, l_sum = sum(nums), 0, 0

        for i in range(len(nums) - 1):
            l_sum += nums[i]
            total_Sum -= nums[i]

            if l_sum >= total_Sum:
                count += 1
        return count
