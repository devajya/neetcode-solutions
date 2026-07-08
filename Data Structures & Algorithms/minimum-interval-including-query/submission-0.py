class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []

        intervals.sort(key=lambda x: (x[1]-x[0]))

        for q in queries:
            found = False
            for i in intervals:
                if q in range(i[0], i[1]+1):
                    found = True
                    output.append(i[1]-i[0]+1)
                    break
            
            if not found:
                output.append(-1)

        return output