class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maps = defaultdict(list)
        for ui, vi, ti in times:
            maps[ui].append((vi, ti))
        ans = {i:float("inf") for i in range(1, n+1)}
        ans[k] = 0
        q = [(k, 0)]
        
        while q:
            node, cost = heapq.heappop(q)
            if cost > ans[node]:
                continue
            for neighbor, time in maps[node]:
                new_time = cost + time
                if new_time < ans[neighbor]:
                    ans[neighbor] = new_time
                    heapq.heappush(q, (neighbor, new_time))
        
        check = max(ans.values())

        return check if check != float("inf") else -1
                    