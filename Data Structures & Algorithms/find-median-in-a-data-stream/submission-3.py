class MedianFinder:

    def __init__(self):
        self.low = [] # max heap
        self.high = [] # min heap
        self.count = 0

    def addNum(self, num: int) -> None:
        # maintain two heaps
        # by default add to the high heap
        # if the length of the small heap becomes smaller than
        # the length of the big heap by more than 1, theres an imbalace
        # in that case add numbers to the small heap till balace is reached
        self.count += 1

        heapq.heappush(self.high, num)

        if self.low and self.low[0] > self.high[0]:
            heapq.heappush(self.high, heapq.heappop_max(self.low))

        while len(self.high) - len(self.low) >= 2:
            heapq.heappush_max(self.low, heapq.heappop(self.high))

        print(self.low, self.high)


    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return 1.0*(self.low[0] + self.high[0]) / 2
        return float(self.high[0])
        