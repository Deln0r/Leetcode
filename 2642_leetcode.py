class Graph:
    def __init__(self, n, edges):
        self.graph = {}
        for edge in edges:
            from_node, to_node, cost = edge
            if from_node not in self.graph:
                self.graph[from_node] = []
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return cost

            if current_node in self.graph:
                for neighbor, edge_cost in self.graph[current_node]:
                    heapq.heappush(heap, (cost + edge_cost, neighbor))

        return -1