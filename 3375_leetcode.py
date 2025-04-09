class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set_nums = set()
        for n in nums:
            if n < k:
                return -1
            set_nums.add(n)
        
        return len(set_nums) - 1 if k in set_nums else len(set_nums)