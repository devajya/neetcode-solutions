class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        
        ans = []
        def dfs(city):
            while graph[city]:
                dest = heapq.heappop(graph[city])
                dfs(dest)
            ans.append(city)
        
        dfs("JFK")
        return ans[::-1]