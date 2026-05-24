from collections import defaultdict
import heapq


class Solution:
    def dijkstra(self, graph, start, n):
        distances = {i: float("inf") for i in range(1, n + 1)}
        distances[start] = 0

        pq = [(0, start)]

        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            if cur_dist > distances[cur_node]:
                continue

            for neighbor, weight in graph[cur_node]:
                new_dist = cur_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances

    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        distances = self.dijkstra(graph, k, n)

        max_dist = max(distances.values())

        return max_dist if max_dist != float("inf") else -1