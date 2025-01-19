class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water = 0

        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    water += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

        return water