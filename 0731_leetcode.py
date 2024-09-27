class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlap:
            if max(start, i) < min(end, j):
                return False

        for i, j in self.booking:
            if max(start, i) < min(end, j):
                self.overlap.append([max(start, i), min(end, j)])
        
        self.booking.append([start, end])
        return True