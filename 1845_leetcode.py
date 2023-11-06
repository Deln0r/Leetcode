class SeatManager:

    # O(logn)
    def __init__(self, n: int):
        self.unres = [i for i in range(1,n+1)]
        

    def reserve(self) -> int:
        return heapq.heappop(self.unres)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres,seatNumber)