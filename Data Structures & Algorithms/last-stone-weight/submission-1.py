import heapq as pq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]

        pq.heapify_max(stones)

        while len(stones) >= 2:
            one = pq.heappop_max(stones)
            two = pq.heappop_max(stones)

            if one == two:
                continue

            pq.heappush_max(stones, one-two)

        return stones[0] if stones else 0
        