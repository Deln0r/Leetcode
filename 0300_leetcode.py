import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            if not ans or ans[-1] < n:
                ans.append(n)
            else:
                i = bisect.bisect_left(ans, n)
                ans[i] = n
        return len(ans)
