class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        large = -1
        while start < end:
            negative, positive = nums[start], nums[end]
            if negative > 0:
                break
            if abs(negative) == positive:
                large = positive
                break
            if abs(negative) < positive:
                end -= 1
            else:
                start += 1
        return large

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1

        while l<r:
            if -nums[l] == nums[r]:
                return nums[r]
            elif -nums[l] > nums[r]:
                l += 1
            elif -nums[l] < nums[r]:
                r -= 1
        return -1

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for n in nums:
            if n < 0:
                if -n in s:
                    ans = max(ans, -n)
        return ans