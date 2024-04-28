class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_count = [1] * n
        subtree_sum = [0] * n
        distances = [0] * n

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    subtree_count[node] += subtree_count[child]
                    subtree_sum[node] += subtree_sum[child] + subtree_count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    subtree_sum[child] = subtree_sum[node] - subtree_count[child] + (n - subtree_count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)
        return subtree_sum