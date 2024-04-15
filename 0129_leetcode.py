class Solution:
  def sumNumbers(self, root: TreeNode | None, res=0) -> int:
    stack = [root]
    while stack:
      node = stack.pop()
      val, l, r = node.val, node.left, node. right
      if not node.left and not node.right:
        res += val
      if node.left:
        l.val = 10 * val + l.val
        stack.append(l)
      if node.right:
        r.val = 10 * val + r.val
        stack.append(r)
          
    return res