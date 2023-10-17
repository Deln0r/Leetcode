class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * n

        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                graph[i].append(left)
                indeg[left] += 1
            if right != -1:
                graph[i].append(right)
                indeg[right] += 1

        root = []
        for i in range(n):
            indegree = indeg[i]
            if indegree == 0:
                if root:
                    return False
                root.append(i)
            elif indegree != 1:
                return False

        visited = set()
        while root:
            node = root.pop(0)
            if node in visited:
                return False
            visited.add(node)
            if node in graph:
                for child in graph[node]:
                    indeg[child] -= 1
                    if indeg[child] == 0:
                        root.append(child)
        return len(visited) == n
