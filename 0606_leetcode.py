class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
          return ""
        s = [f"{root.val}"]
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if right:
          s += ["(", left, ")"]
          s += ["(", right, ")"]
        elif left and not right:
          s += ["(", left, ")"]
        return "".join(s)


# class Solution(object):
#     def tree2str(self, t):
#         res = []
#         self.dfs(t, res)
#         return ''.join(res)

#     def dfs(self, t, res):
#         if t is None:
#             return

#         res.append(str(t.val))

#         if t.left is None and t.right is None:
#             return

#         res.append('(')
#         self.dfs(t.left, res)
#         res.append(')')

#         if t.right is not None:
#             res.append('(')
#             self.dfs(t.right, res)
#             res.append(')')