class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        total_subarrays = 0
        start_index = 0
        end_index = 2
        n = len(nums)
        while end_index < n:

            if (nums[start_index] + nums[end_index]) * 2 == nums[start_index + 1]:
                total_subarrays += 1

            start_index += 1
            end_index += 1

        return total_subarrays
        