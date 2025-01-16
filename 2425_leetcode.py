class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        if n2%2==1:
            for i in range(n1):
                ans = ans ^ nums1[i]
        
        if n1%2==1:
            for i in range(n2):
                ans = ans ^ nums2[i]
        
        return ans