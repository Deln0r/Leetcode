class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def traverse(node):
            if node is None:
                return (0,0)
            left=traverse(node.left)
            right=traverse(node.right)
            total=left[0]+right[0]+node.val
            count=left[1]+right[1]+1
            if total//count==node.val:
                nonlocal ans
                ans+=1
            return (total,count)
        traverse(root)
        return ans