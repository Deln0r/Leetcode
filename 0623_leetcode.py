class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(node, cur):
            if not node:
                return
            if cur + 1 == depth:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return
            else:
                dfs(node.left, cur + 1)
                dfs(node.right, cur + 1)
        
        dfs(root, 1)
        
        return root