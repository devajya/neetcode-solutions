"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.end, -1))
            events.append((interval.start, 1))

        events.sort(key=lambda x: (x[0], x[1]))

        ans = 0
        cur = 0

        for event in events:
            cur+= event[1]
            ans = max(ans, cur)
        return ans