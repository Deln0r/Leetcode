class NumberContainers:

    def __init__(self):
        self.system = defaultdict(list)  # Min-heap for each number
        self.getnum = {}  # Direct mapping of index to its current number
        self.valid = {}  # Keeps track of valid indices

    def change(self, index: int, number: int) -> None:
        if index in self.getnum:
            old_number = self.getnum[index]
            if old_number != number:
                self.valid[(old_number, index)] = False  # Mark old index as invalid

        self.getnum[index] = number
        heapq.heappush(self.system[number], index)
        self.valid[(number, index)] = True  # Mark new index as valid

    def find(self, number: int) -> int:
        if number not in self.system:
            return -1

        while self.system[number]:
            min_index = self.system[number][0]
            if self.valid.get((number, min_index), False):
                return min_index
            heapq.heappop(self.system[number])  # Remove invalid indices

        return -1