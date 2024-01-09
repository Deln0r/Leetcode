# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        li1=[]
        li2=[]
        def temp(node,li):
            if node is None:
                return
            if node.left is None and node.right is None:
                li.append(node.val)
            temp(node.left,li)
            temp(node.right,li)
        temp(root1,li1)
        temp(root2,li2)
        if li1==li2:
            return 1
        else:
            return 0
