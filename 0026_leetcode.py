class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        x=nums[0]
        i=0
        while i<len(nums)-1:
            if x==nums[1+i]:
                del nums[1+i]
            else:
                x=nums[1+i]
                i+=1
        return i+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer], nums[i] = nums[i], nums[pointer]
        return pointer + 1