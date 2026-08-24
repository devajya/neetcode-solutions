class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        
        ans = []

        def dfs(airport):
            while graph[airport]:
                next_air = heapq.heappop(graph[airport])
                dfs(next_air)

            ans.append(airport)

        
        dfs("JFK")
        return ans[::-1]