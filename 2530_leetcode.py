class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [-x for x in nums]
        heapq.heapify(q)
        total = 0
        for i in range(k):
            total -= q[0]
            heapq.heapreplace(q, q[0]//3)
        return total