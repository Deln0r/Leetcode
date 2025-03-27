class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        candidate = nums[0]
        count = 0
        for n in nums:
            if candidate == n:
                count += 1
            else:
                count -= 1

            if count <= 0:
                count = 1
                candidate = n

        if count < 2:
            return -1

        freq = 0
        for n in nums:
            if n == candidate:
                freq += 1

        seen = 0
        for i in range(len(nums)):
            first_window_size = i + 1
            second_window_size = len(nums) - first_window_size

            if nums[i] == candidate:
                seen += 1

            if 2 * seen > first_window_size and 2 * (freq - seen) > second_window_size:
                return i

        return -1