# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(pre,post):
            val = pre.popleft()
            node = TreeNode(val)
            if val == post[0]:
                post.popleft()
            else:
                node.left = helper(pre,post)
                if val == post[0]:
                   post.popleft()
                else:
                    node.right = helper(pre,post)
                    if val == post[0]:
                       post.popleft()
            return node
        
        pre = deque(preorder)
        post = deque(postorder)
        return helper(pre,post)