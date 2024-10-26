class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = dict()
        max_height = float("-inf")

        def set_heights(root):
            nonlocal max_height, heights

            if not root:
                return -1

            left_height, right_height = set_heights(root.left), set_heights(root.right)
            
            heights[root.val] = max(left_height, right_height) + 1

            max_height = max(max_height, heights[root.val])

            return heights[root.val]

        set_heights(root)

        cache = dict()

        def set_best_height_without_node(root, depth, best_height_without_node):
            if not root:
                return

            cache[root.val] = best_height_without_node

            left_height = heights[root.left.val] if root.left else -1
            right_height = heights[root.right.val] if root.right else -1

            if left_height > right_height:
                best_height_without_node = max(best_height_without_node, right_height+depth+1)
                set_best_height_without_node(root.left, depth+1, best_height_without_node)
            
            else:
                best_height_without_node = max(best_height_without_node, left_height+depth+1)
                set_best_height_without_node(root.right, depth+1, best_height_without_node)

            return

        set_best_height_without_node(root, 0, 0)

        ans = []

        for query in queries:
            if query in cache:
                ans.append(cache[query])
            else:
                ans.append(max_height)

        return ans