class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum1 = sum(nums1)
        zeroCount1 = nums1.count(0)
        
        sum2 = sum(nums2)
        zeroCount2 = nums2.count(0)

        if zeroCount1 == 0 and zeroCount2 == 0:
            if sum1 == sum2:
                return sum1
            else:
                return -1
        if zeroCount2 == 0:
            if sum1 + zeroCount1 > sum2:
                return -1
            else:
                return sum2
        if zeroCount1 == 0:
            if sum2 + zeroCount2 > sum1:
                return -1
            else:
                return sum1

        return max(sum1 + zeroCount1, sum2 + zeroCount2)