class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = n * (n + 1) // 2

        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum

        return [duplicate, missing]