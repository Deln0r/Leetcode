class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for i in range(0,len(nums)-1):
            for j in range((i+1),len(nums)):
                if nums[i]==nums[j]:
                    c+=1
        return c
    

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        d = {}
        for num in nums:
            if num in d:
                ans += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return ans
