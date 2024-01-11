class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currmax, currmin):
            if not node:
                return currmax - currmin

            currmax = max(currmax, node.val)
            currmin = min(currmin, node.val)
            left = dfs(node.left, currmax, currmin)
            right = dfs(node.right, currmax, currmin)
            return max(left, right)

        return dfs(root, root.val, root.val)