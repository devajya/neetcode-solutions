class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        distances = {i:float("inf") for i in range(1, n+1)}
        distances[k] = 0
        heap = [(0, k)]

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            
            for nei, cost in graph[node]:
                new_dist = dist + cost
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        mx = max(distances.values())  
        return -1 if mx == float("inf") else mx

            