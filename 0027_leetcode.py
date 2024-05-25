class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = nums.count(val)
        while counter != 0:
            nums.remove(val)
            counter -= 1
        return len(nums)