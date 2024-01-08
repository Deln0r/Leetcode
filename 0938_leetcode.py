# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inOrderTraversal(node):
            nonlocal total_sum
            if not node:
                return
            if low <= node.val <= high:
                total_sum += node.val
            if node.val > low:
                inOrderTraversal(node.left)
            if node.val < high:
                inOrderTraversal(node.right)

        total_sum = 0
        inOrderTraversal(root)
        return total_sum
