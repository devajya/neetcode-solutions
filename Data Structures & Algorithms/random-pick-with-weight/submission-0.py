class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        cur = 0
        for i in range(len(self.w)):
            cur += self.w[i]
            if cur > target:
                return i


