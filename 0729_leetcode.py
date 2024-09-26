class MyCalendar:

    def __init__(self):
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.slots, (start, end))
        res = True

        if index < len(self.slots): res &= end <= self.slots[index][0]
        
        if index - 1 >= 0: res &= start >= self.slots[index-1][1]

        if res: bisect.insort_left(self.slots, (start, end))
        return res