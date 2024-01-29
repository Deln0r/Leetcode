class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.temporary_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
    def pop(self) -> int:
        for i in range(1,len(self.main_stack)):
            self.temporary_stack.append(self.main_stack.pop())
        a = self.main_stack.pop()
        for i in range(len(self.temporary_stack)):
            self.main_stack.append(self.temporary_stack.pop())
        return a

    def peek(self) -> int:
        return self.main_stack[0]
    def empty(self) -> bool:
        return len(self.main_stack)==0