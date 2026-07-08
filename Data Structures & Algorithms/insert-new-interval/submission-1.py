class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        if len(intervals) == 0:
            return intervals
        
        x, y = intervals[0][0], intervals[0][1]
        writingIdx = 0

        for i in range(1, len(intervals)):
            xn, yn = intervals[i][0], intervals[i][1]

            if xn <= y:
                y = max(y, yn)
                # x = min(x, xn)
            else:
                intervals[writingIdx] = [x, y]
                writingIdx += 1
                x, y = xn, yn
        intervals[writingIdx] = [x, y]
        return intervals[:writingIdx+1]
