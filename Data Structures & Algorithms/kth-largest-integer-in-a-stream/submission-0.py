import heapq as pq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        pq.heapify(self.heap)
        while len(self.heap) > k:
            pq.heappop(self.heap)

    def add(self, val: int) -> int:
        pq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            pq.heappop(self.heap)
        return self.heap[0]
