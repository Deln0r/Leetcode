class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap: list = list()
        for i in range(1, len(heights)):
            diff: int = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i - 1
        return len(heights) - 1