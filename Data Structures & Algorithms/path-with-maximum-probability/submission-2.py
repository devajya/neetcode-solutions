class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        i = 0
        for u, v in edges:
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
            i+=1

        pq = [(-1.0, start_node)]
        max_p_for_node = defaultdict(int)
        max_p_for_node[start_node] = -1 # negative for max heap version

        while pq:
            curr_p, node = heapq.heappop(pq)
            curr_p = -1*curr_p
            if node == end_node:
                return curr_p
            
            for next_node, prob in graph[node]:
                new_prob = curr_p*prob

                if new_prob > max_p_for_node[next_node]:
                    max_p_for_node[next_node] = new_prob
                    heapq.heappush(pq, (-new_prob, next_node))


        return 0.0