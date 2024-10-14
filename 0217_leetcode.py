def containsDuplicate(nums):
    return len(nums) != len(set(nums))


nums = [1, 2, 3, 4]
# nums = [1, 2, 3, 1]
print(containsDuplicate(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
