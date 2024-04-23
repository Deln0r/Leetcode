class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
        
        while len(graph) > 2:
            new_leaves = []
            for leaf in leaves:
                nei = graph[leaf].pop()
                del graph[leaf]
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        
        return leaves