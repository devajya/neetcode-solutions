import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x1, y1 = point[0], point[1]
            dist = sqrt(x1**2 + y1**2)
            ent = [dist, point]
            heapq.heappush(heap, ent)

        ans = []

        while len(ans) < k:
            l = heapq.heappop(heap)
            print(l)
            ans.append(l[1])
        
        return ans

