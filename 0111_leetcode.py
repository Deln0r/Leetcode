Class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root,1)])
        while q:
            cur, depth = q.popleft()
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))
