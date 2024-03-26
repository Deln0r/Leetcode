class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #  method two using cycle Sort 
        n = len(nums)
        i = 0
        
        while i < n:
            cor_pos = nums[i] - 1
            if nums[i] > n or nums[i] <= 0:
                i += 1
                continue

            if cor_pos != i and cor_pos < n and nums[cor_pos] != nums[i]:
                nums[i] , nums[cor_pos] = nums[cor_pos],nums[i]
                
            else:
                i += 1
        # print(nums)
        for i in range(1,n + 1):
            if i != nums[i - 1]:
                return i 
        return n + 1