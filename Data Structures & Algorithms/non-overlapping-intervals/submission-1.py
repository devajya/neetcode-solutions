class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arrs = sorted(intervals, key = lambda x: x[1])
        stack = [arrs[0]]
        sub_count = 0
        for i in range(1, len(arrs)):
            if stack[-1][1] > arrs[i][0]:
                sub_count += 1
                continue
            stack.append(arrs[i])
        return sub_count