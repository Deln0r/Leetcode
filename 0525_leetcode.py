class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = { 0 : -1 }

        cur_sum, max_len = 0, 0
        for i, n in enumerate(nums):
            cur_sum += 1 if n else -1
            if cur_sum not in hashMap: hashMap[cur_sum] = i
            else: max_len = max(max_len, i - hashMap[cur_sum])
        
        return max_len