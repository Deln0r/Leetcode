class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        l = ans = count = 0
        for r,num in enumerate(nums):
            if num==max_:
                count+=1

            while count>=k:
                ans+= len(nums)-r
                if nums[l]==max_:
                    count-=1
                l+=1

        return ans