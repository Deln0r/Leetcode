class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        l=defaultdict(list)
        def bfs(root,h):
            if root is None:
                return
            l[h].append(root.val)
            bfs(root.left,h+1)
            bfs(root.right,h+1)
        bfs(root,0)
        return l[len(l)-1][0]