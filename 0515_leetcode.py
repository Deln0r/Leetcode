from collections import deque

class Solution:
    def largestValues(self, root):
        if not root:
            return []

        ans = []
        maxi = float('-inf')
        q = deque()
        q.append(root)
        q.append(None)

        while q:
            front = q.popleft()
            if front is None:
                ans.append(maxi)
                maxi = float('-inf')
                if q:
                    q.append(None)
            else:
                maxi = max(maxi, front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

        return ans