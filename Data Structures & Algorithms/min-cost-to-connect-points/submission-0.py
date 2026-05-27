class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {node: [] for node in range(N)}

        # Build adjacency list
        for i in range(N):
            x, y = points[i]
            for j in range(i+1, N):
                a, b = points[j]
                man_dist = abs(x-a) + abs(y-b)
                adj[i].append([man_dist, j])
                adj[j].append([man_dist, i])
        

        ans = 0
        visited = set()
        heap = [[0, 0]]
        while len(visited) < N:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            print(cost, node)
            ans += cost

            for edgeCost, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, [edgeCost, neighbor])

        return ans