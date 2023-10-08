class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        c1 = 0
        c2 = 0
        for i in nums1:
            if i < 0 :
                c1+=1
        for j in nums2 :
            if j < 0 :
                c2+=1
        if c1 == n and c2 != m:
            return max(nums1)*min(nums2)
        if c2 == m and c1 != n :
            return max(nums2)*min(nums1)


        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = max(nums1[i]*nums2[j] + dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
        return dp[0][0]
