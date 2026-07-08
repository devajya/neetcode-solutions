class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        x, y = intervals[0][0], intervals[0][1]
        writingIdx = 0

        for interval in intervals:
            xn, yn = interval[0], interval[1]
            if xn <= y:
                y = max(y, yn)
            else:
                intervals[writingIdx] = [x, y]
                writingIdx += 1
                x, y = xn, yn
    
        intervals[writingIdx] = [x, y]

        return intervals[:writingIdx+1]