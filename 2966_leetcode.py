class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        l, ind = len(nums)//3, 0
        
        res = [[] for _ in range(l)]

        for i in range(l):
            res[i] = nums[ind: ind+3]
            
            if res[i][2] - res[i][0] > k: 
                return []

            ind += 3

        return res
