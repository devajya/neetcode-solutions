class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # ans variable
        ans = []

        iters = [(start, proc, idx) for idx, (start, proc) in enumerate(tasks)]

        # sort by start time, tie break proc time
        iters.sort(key = lambda x: (x[0], x[1], x[2]))

        # keep track of available options for every idle
        heap = []
        clock = 0
        j = 0

        while len(ans) < len(tasks):
            while j < len(iters) and (clock >= iters[j][0] or not heap):
                s, p, i = iters[j]
                clock = max(clock, s)
                heapq.heappush(heap, (p, i))
                j+=1
            
            p, i = heapq.heappop(heap)
            ans.append(i)
            clock += p

        return ans