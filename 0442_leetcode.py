class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            indx= abs(i)-1
            if nums[indx]>0:
                nums[indx]=-nums[indx]
            else:
                l.append(abs(i))
        return l