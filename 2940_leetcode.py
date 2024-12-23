class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        deferred_queries = [[] for _ in range(len(heights))]
        
        for idx, (building_a, building_b) in enumerate(queries):
            a, b = min(building_a, building_b), max(building_a, building_b)
            if a == b or heights[a] < heights[b]:
                res[idx] = b
            else:
                deferred_queries[b].append((heights[a], idx))
        
        min_heap = []
        for i, height in enumerate(heights):
            for query in deferred_queries[i]:
                heapq.heappush(min_heap, query)
            while min_heap and min_heap[0][0] < height:
                _, query_index = heapq.heappop(min_heap)
                res[query_index] = i
        
        return res