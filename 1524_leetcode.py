class Solution:
    def numOfSubarrays(self, arr):
        s, odd, even = 0, 0, 1
        for num in arr:
            s += num 
            if s & 1: odd += 1
            else: even += 1
        
        return (odd * even) % (10**9 + 7)