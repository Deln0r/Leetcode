class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs():
            stack = deque([(0, 0)])
            visited = {0}
            while stack:
                dist, cur = stack.popleft()
                if cur == n - 1:
                    return dist                
                for vertex in graph[cur]:
                    if vertex not in visited:
                        stack.append((dist + 1, vertex))
                        visited.add(vertex)

        graph = defaultdict(list)
        for s, d in pairwise(range(n)):
            graph[s].append(d)
        result = []
        for s, d in queries:
            graph[s].append(d)
            result.append(bfs())
        return result