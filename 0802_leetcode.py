class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = [False] * n
        inPath = [False] * n

        def dfs(node: int) -> bool:
            if visited[node]:
                return not inPath[node]  # If inPath is True, it means there's a cycle.
            
            visited[node] = True
            inPath[node] = True
            
            for neighbor in graph[node]:
                if not dfs(neighbor):  # If a cycle is detected.
                    return False
            
            inPath[node] = False
            safe[node] = True
            return True
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return [i for i in range(n) if safe[i]]