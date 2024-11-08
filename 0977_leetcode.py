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

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        l = 0
        r = k = len(nums)-1

        while l<=r:
            l2, r2 = nums[l]**2, nums[r]**2
            if l2 > r2:
                ans[k] = l2
                l+=1
            else:
                ans[k] = r2
                r-=1
            k-=1
        return ans