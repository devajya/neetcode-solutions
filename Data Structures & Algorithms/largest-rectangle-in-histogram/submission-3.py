class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                ans = max(ans, h*(idx-i))
                start = i
            stack.append((start, height))
        

        for i,h in stack:
            ans = max(ans, h * (len(heights)-i))
        return ans