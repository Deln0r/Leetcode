class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue = [root]
        result = 0

        while queue:
            values = [node.val for node in queue]
            nextQueue = []

            for node in queue:
                if node.left:
                    nextQueue.append(node.left)

                if node.right:
                    nextQueue.append(node.right)

            queue = nextQueue

            graph = sorted(range(len(values)), key=lambda x: values[x])

            for i in range(len(graph)):
                if graph[i] is None or i == graph[i]:
                    continue

                start = i
                v = graph[i]
                graph[i] = None
                count = 0

                while v != start:
                    temp = graph[v]
                    graph[v] = None
                    v = temp
                    count += 1

                result += count

        return result