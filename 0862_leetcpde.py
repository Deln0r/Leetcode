from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        res = float('inf')
        prefix_sum = 0
        q = deque([(0, -1)])

        for r, num in enumerate(nums):
            prefix_sum += num

            while q and prefix_sum - q[0][0] >= k:
                res = min(res, r - q.popleft()[1])

            while q and q[-1][0] >= prefix_sum:
                q.pop()

            q.append((prefix_sum, r))

        return res if res != float('inf') else -1