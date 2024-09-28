class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.rear = k


    def insertFront(self, value: int) -> bool:
        if self.isFull() == False:
            self.queue = [value] + self.queue
            return True
        else:
            return False

        

    def insertLast(self, value: int) -> bool:
        if self.isFull() == False:
            self.queue.append(value)
            return True
        else:
            return False

        

    def deleteFront(self) -> bool:
        if self.isEmpty() == False:
            self.queue = self.queue[1:]
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.isEmpty() == False:
            self.queue.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.isEmpty() == False:
            return self.queue[0]
        else:
            return -1

        

    def getRear(self) -> int:
        if self.isEmpty() == False:
            return self.queue[-1]
        else:
            return -1

        

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False

        

    def isFull(self) -> bool:
        return True if len(self.queue) == self.rear else False