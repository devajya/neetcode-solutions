class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency_list = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adjacency_list[src].append(dst)

        res = []
        def backtrack(start):
            while adjacency_list[start]:
                dst = adjacency_list[start].pop()
                backtrack(dst)
            res.append(start)
        
        backtrack("JFK")
        return res[::-1]