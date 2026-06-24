class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []


        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                ans = max(ans, height*(i-idx))
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            ans = max(ans, h*(len(heights)-i))

        return ans