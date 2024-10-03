class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0  
        result = len(nums)
        prefixsum = 0
        dictremainder = {0: -1}
        for i in range(len(nums)):
            prefixsum += nums[i]
            curremainder = prefixsum % p
            target = (curremainder - remainder) % p
            if target in dictremainder:
                result = min(result, i - dictremainder[target])
            dictremainder[curremainder] = i  
        return result if result < len(nums) else -1