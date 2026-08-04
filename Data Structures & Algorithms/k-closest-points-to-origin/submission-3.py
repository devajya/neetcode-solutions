class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, (x, y)))
        
        while k:
            ans.append(list(heapq.heappop(heap)[1]))
            k-=1
        
        return ans