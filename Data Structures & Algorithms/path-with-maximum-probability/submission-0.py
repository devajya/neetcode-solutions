class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = self.to_graph(edges, succProb)
        ans = self.dijkstra(graph, start_node, end_node)

        return ans

    def to_graph(self, edges, weights):
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            ing, egr = edge[0], edge[1]
            graph[ing].append((egr, weights[i]))
            graph[egr].append((ing, weights[i]))
            
        return graph
        
    def dijkstra(self, graph, start, target = None):
        probabilities = defaultdict(lambda: float("-inf"))
        probabilities[start] = 1
        pq = [(-1, start)]

        while pq:
            neg_prob, node = heapq.heappop(pq)
            prob = -neg_prob

            if node == target:
                return prob
            if prob < probabilities[node]:
                continue
            
            for n, p in graph[node]:
                possible = p*prob
                if possible > probabilities[n]:
                    probabilities[n] = possible
                    heapq.heappush(pq, (-possible, n))

        return 0

