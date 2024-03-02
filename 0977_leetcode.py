class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i = 0
        n = len(nums)
        j = n - 1
        
        new = [0] * n
        k = n - 1
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                new[k] = nums[j] ** 2
                j -= 1
                
            else:
                new[k] = nums[i] ** 2
                i += 1
            k -= 1
            
        return new
    
    
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (nums[i]**2)
        nums.sort()
        return nums