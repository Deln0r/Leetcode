class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2, level):
            if not node1 or not node2:
                return
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val

            dfs(node1.left, node2.right, level + 1)
            dfs(node2.left, node1.right, level + 1)

        dfs(root.left, root.right, 1)
        return root