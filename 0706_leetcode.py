class MyHashMap:

    def __init__(self):
        MAX_ARR=10**6+1
        self.arr_map=[-1]*(MAX_ARR)

    def put(self, key: int, value: int) -> None:
        self.arr_map[key]=value

    def get(self, key: int) -> int:
        return self.arr_map[key]

    def remove(self, key: int) -> None:
        self.arr_map[key]=-1
