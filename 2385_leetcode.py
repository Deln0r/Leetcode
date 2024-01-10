class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d = dict()
        self.create(root, None, d)
        c = 0
        visited = set()
        visited.add(start)
        queue = deque([(start, 0)])
        while queue:
            node, lvl = queue.popleft()
            c = max(c, lvl)
            for nxt in d[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, lvl+1))
        return c

    def create(self, root, prev, d):
        if root is None:
            return
        if root.val not in d:
             d[root.val] = []
        if root.left is not None:
            d[root.val].append(root.left.val)
        if root.right is not None:
            d[root.val].append(root.right.val)
        if prev is not None:
            d[root.val].append(prev.val)
        self.create(root.left, root, d)
        self.create(root.right, root, d)