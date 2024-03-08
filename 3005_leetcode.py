class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxFreq = max(count.values())
        ans = 0
        
        for val in count.values():
            if val==maxFreq:
                ans+=val
                
        return ans