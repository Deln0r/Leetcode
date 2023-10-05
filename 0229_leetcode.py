class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        n=len(nums)
        for key,value in count.items():
            if value>(n//3):
                ans.append(key)
        return ans
