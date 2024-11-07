from collections import defaultdict
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d = defaultdict(int)
        for num in candidates:
            n = str(bin(num))[2:]
            n = n[::-1]
            for index , bit in enumerate(n):
                if bit == '1':
                    d[index] += 1
        return max( d.values() )