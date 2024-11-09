class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        num1_set = set(nums1)

        for num in nums2:
            if num in num1_set:
                return num

        return(-1)

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = 0, 0

        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            elif nums1[l1] > nums2[l2]:
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
        return -1