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
