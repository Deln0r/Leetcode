class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        ans = [0, 0]

        for n in nums1:
            if n in num2_set:
                ans[0] += 1
        
        for n in nums2:
            if n in num1_set:
                ans[1] += 1
        
        return ans