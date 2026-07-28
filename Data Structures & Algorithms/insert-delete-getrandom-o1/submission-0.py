class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {} #(val to idx in arr)

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.arr)
        self.arr.append(val)


    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        r_idx = self.map[val]
        self.arr[r_idx] = self.arr[-1]
        self.map[self.arr[-1]] = r_idx
        self.arr.pop()

        del self.map[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()