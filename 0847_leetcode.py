class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = deque([(i, 1<<i) for i in range(len(graph))])
        seen = set(queue)
        ans = 0 
        while queue: 
            for _ in range(len(queue)): 
                u, m = queue.popleft()
                if m == (1<<len(graph)) - 1: return ans 
                for v in graph[u]: 
                    if (v, m | 1<<v) not in seen: 
                        queue.append((v, m | 1<<v))
                        seen.add((v, m | 1<<v))
            ans += 1
