class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique_set = set(nums)
        li = list(unique_set)
        li.sort()
        n,m = len(nums),len(li)
        res,j = len(nums),0
        for i in range(m):
            while j<m and li[j]<li[i]+n:
                j+=1
            res = min(res,n-j+i)
        return res
