class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        start = end = nums[0]
        result = []
        for i in range(1, len(nums)):
            
            if nums[i] - nums[i-1] == 1:
                end = nums[i]

            else:
                result.append(f"{start}->{end}" if start != end else f"{start}")
                start = end = nums[i]

        result.append(f"{start}->{end}" if start != end else f"{start}")     
        return result