class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums)
        return result if result[0] != '0' else '0'