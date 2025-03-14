class Solution:
    def check(self, candies, nums, q):
        val = 0
        for num in nums:
            x = num // candies  # From one pile, we give only 'candies' to x children.
            val += x
        return val >= q

    def maximumCandies(self, nums, k):
        start, end = 1, 0
        total_sum = sum(nums)
        if total_sum < k:
            return 0
        end = total_sum // k  # Maximum candies each child can get in the best case.

        ans = 1
        while start <= end:
            mid = (start + end) // 2
            if self.check(mid, nums, k):  # If condition satisfies, proceed further to check beyond 'mid'.
                start = mid + 1
                ans = mid
            else:
                end = mid - 1  # If not satisfied, search in the lower range.
        return ans