class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def grid_to_graph(grid):
            m, n = len(grid), len(grid[0])
            graph = defaultdict(list)

            for i in range(m):
                for j in range(n):
                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        ni = i+dx
                        nj = j+dy
                        if 0<=ni<m and 0<=nj<n:
                            cost = abs(grid[ni][nj] - grid[i][j])
                            graph[(i, j)].append(((ni, nj), cost))
            return graph
        
        def dijkstra(graph, start, target = None):
            distances = defaultdict(lambda: float("inf"))
            distances[start] = 0
            pq = [(0, start)]

            while pq:
                cost, node = heapq.heappop(pq)

                if node == target:
                    return cost

                if cost > distances[node]:
                    continue

                for u, w in graph[node]:
                    new_cost = max(cost, w)
                    if new_cost < distances[u]:
                        distances[u] = new_cost
                        heapq.heappush(pq, (new_cost, u))

            return distances

        m, n = len(heights), len(heights[0])
        graph = grid_to_graph(heights)
        return dijkstra(graph, start = (0, 0), target = (m-1, n-1))