class MinStack:

    def __init__(self):
        self.min_arr = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min_arr) == 0:
            self.min_arr.append(val)
        else:
            self.min_arr.append(min(self.min_arr[-1], val))

    def pop(self) -> None:
        self.min_arr.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
        
