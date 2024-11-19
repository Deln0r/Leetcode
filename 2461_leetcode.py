class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        curr=0
        hm={}
        for i in range(len(nums)):
            curr+=nums[i]
            if nums[i] in hm:
                hm[nums[i]]+=1
            else:
                hm[nums[i]]=1
            if i>=k:
                hm[nums[i-k]]-=1
                curr-=nums[i-k]
            if nums[i-k] in hm:
                if hm[nums[i-k]]==0:
                    hm.pop(nums[i-k])
            if len(hm)==k:
                ans=max(ans,curr)
        return ans