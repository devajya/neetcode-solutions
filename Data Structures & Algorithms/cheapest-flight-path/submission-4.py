class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        dp = {}

        def dfs(node, steps):
            if node == dst:
                return 0
            if steps < 0:
                return float("inf")

            if (node, steps) in dp:
                return dp[(node, steps)]

            min_cost = float('inf')
            for nei, price in adj[node]:
                sub_cost = dfs(nei, steps-1)
                if sub_cost != float('inf'):
                    min_cost = min(min_cost, price+sub_cost)
            
            dp[(node, steps)] = min_cost
            return min_cost

        ans = dfs(src, k)
        return int(ans) if ans != float('inf') else -1

"""
    
"""