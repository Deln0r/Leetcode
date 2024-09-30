class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.size=0
        self.ls=[]
        self.memory=[]

    def push(self, x: int) -> None:
        if (self.size<self.maxSize):
            self.ls.append(x)
            self.memory.append(0)
            self.size+=1

    def pop(self) -> int:
        if (self.size>0):
            self.size-=1
            return self.ls.pop()+self.memory.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        amount=min(k,self.size)
        for i in range(amount):
            self.memory[i]+=val