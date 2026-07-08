class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        e = intervals[0][1]

        ans = 0

        for start, end in intervals[1:]:
            if start >= e:
                e = end
            else:
                ans += 1
                e = min(e, end)
        
        return ans