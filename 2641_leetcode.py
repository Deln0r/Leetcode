class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        level_sum = []

        # First BFS to compute level sums
        while q:
            level_size = len(q)
            level_total = 0
            for _ in range(level_size):
                node = q.popleft()
                level_total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(level_total)

        # Second BFS to replace node values
        q.append(root)
        root.val = 0
        level = 0

        while q:
            level_size = len(q)
            next_level_sum = level_sum[level + 1] if level + 1 < len(level_sum) else 0

            for _ in range(level_size):
                node = q.popleft()
                child_sum = 0

                if node.left:
                    child_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    child_sum += node.right.val
                    q.append(node.right)

                if node.left:
                    node.left.val = next_level_sum - child_sum
                if node.right:
                    node.right.val = next_level_sum - child_sum

            level += 1

        return root