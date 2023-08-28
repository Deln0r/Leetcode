class Solution:
    def search(self, nums, target: int) -> int:
        left, r = 0, len(nums) - 1
        while left <= r:
            mid = (left + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                r = mid - 1
        return -1
