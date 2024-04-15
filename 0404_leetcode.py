class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0
        queue = [(root, False)] # (node, isLeft)
        while queue:
            node, isLeft = queue.pop(0)
            if not node.left and not node.right and isLeft:
                sums += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        return sums