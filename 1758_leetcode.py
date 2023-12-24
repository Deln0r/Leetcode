class Solution:
    def minOperations(self, s: str) -> int:
        return min(
            sum(int(bit) == i & 1 for i, bit in enumerate(s)),
            sum(int(bit) != i & 1 for i, bit in enumerate(s)),
        )
