class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for i in nums:
            if i in s.keys():
                s[i]+=1
            else:
                s[i]=1
        majority_key = max(s, key=s.get)
        return majority_key