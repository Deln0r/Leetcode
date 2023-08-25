class Solution:
    def postorderTraversal(self, root):
        ans = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                ans.append(node.val)
        helper(root)
        return ans
