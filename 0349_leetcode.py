class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums1:
            if (i in nums2) and (i not in ans):
                ans.append(i)
        
        return ans
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)