class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        prev = nums[0]

        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i + 1] < nums[i] > prev:
                ans += 1
            elif nums[i + 1] > nums[i] < prev:
                ans += 1

            prev = nums[i]

        return ans
