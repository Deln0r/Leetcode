from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Calculate the sum of all k-length windows
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        for i in range(1, len(window_sum)):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum

        # Step 2: Find the best left index for each position
        left = [0] * len(window_sum)
        best_idx = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best_idx]:
                best_idx = i
            left[i] = best_idx

        # Step 3: Find the best right index for each position
        right = [0] * len(window_sum)
        best_idx = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best_idx]:  # '=' for lexicographically smaller
                best_idx = i
            right[i] = best_idx

        # Step 4: Find the three indices that maximize the sum
        max_sum = 0
        result = [-1, -1, -1]
        for j in range(k, len(window_sum) - k):
            i, l = left[j - k], right[j + k]
            total = window_sum[i] + window_sum[j] + window_sum[l]
            if total > max_sum:
                max_sum = total
                result = [i, j, l]

        return result