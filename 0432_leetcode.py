class AllOne:

    def __init__(self):
        self.c = Counter()
        self.max_heap = []
        self.min_heap = []

    def inc(self, key: str) -> None:
        self.c[key] += 1
        heapq.heappush(self.max_heap, (-self.c[key], key))  
        heapq.heappush(self.min_heap, (self.c[key], key))

    def dec(self, key: str) -> None:
        if key in self.c:
            self.c[key] -= 1
            if self.c[key] == 0:
                del self.c[key]
            else:
                heapq.heappush(self.max_heap, (-self.c[key], key))
                heapq.heappush(self.min_heap, (self.c[key], key))

    def getMaxKey(self) -> str:
        while self.max_heap:
            count, key = self.max_heap[0]
            if -count == self.c[key]:  
                return key
            heapq.heappop(self.max_heap)
        return "" 

    def getMinKey(self) -> str:
        while self.min_heap:
            count, key = self.min_heap[0]
            if count == self.c[key]: 
                return key
            heapq.heappop(self.min_heap)
        return "" 