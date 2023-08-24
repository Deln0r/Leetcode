def containsDuplicate(nums):
    return len(nums) != len(set(nums))


nums = [1, 2, 3, 4]
# nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
