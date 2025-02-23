class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        n = len(traversal)
        i = 0
        t = [0]
        z = 0

        while i < n:
            curr = ""
            dash = 0
            while i<n and traversal[i] in nums:
                curr+=traversal[i]
                i+=1
            while i<n and traversal[i] == '-':
                dash+=1
                i+=1
            if curr != "": t.append(int(curr))
            if dash > 0: t.append(dash)

        t = [t[i:i+2] for i in range(0,len(t),2)] # chunking traversal array

        def dfs(i, prev):
            
            if i >= len(t): return None, i

            level = t[i][0]
            val = t[i][1]

            if level <= prev: return None, i

            node = TreeNode(val=val)

            node.left, next_i = dfs(i+1, level)
            node.right, next_i = dfs(next_i, level)
           
            return node, next_i
          
        root, end = dfs(0,-1)
        return root