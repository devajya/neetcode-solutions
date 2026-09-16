class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            adj[eq[0]].append((eq[1], values[i]))
            adj[eq[1]].append((eq[0], 1/values[i]))

        def process(q):
            u, v = q
            if u not in adj or v not in adj:
                return -1.0

            pq = deque([(u, 1)])
            visited = set()
            visited.add(u)

            while pq:
                symbol, val = pq.popleft()
                if symbol == v:
                    return val
                
                for ns, sw in adj[symbol]:
                    if ns not in visited:
                        pq.append((ns, val * sw))
                        visited.add(ns)
                    
            
            return -1.0
                

        
        return [process(q) for q in queries]