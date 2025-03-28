class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        result = [0] * len(queries)

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        sorted_queries = sorted([(val, i) for i, val in enumerate(queries)])

        visited = [[False] * m for _ in range(n)]

        total_points = 0
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        for query, idx in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                cv, r, c = heappop(min_heap)

                total_points += 1

                for row_offset, col_offset in DIRECTIONS:
                    new_row, new_col = (r + row_offset, c + col_offset)
                    if (new_row >= 0 and new_col >= 0 and new_row < n and new_col < m and not visited[new_row][new_col]):
                        heappush(min_heap, (grid[new_row][new_col], new_row, new_col))
                        visited[new_row][new_col] = True
            result[idx] = total_points
        return result