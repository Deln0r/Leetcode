class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        num1_set = set(nums1)

        for num in nums2:
            if num in num1_set:
                return num

        return(-1)