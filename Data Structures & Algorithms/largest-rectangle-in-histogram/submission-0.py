class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = -1

        for i in range(0, n+1):
            while len(stack)>0 and (i==n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width =  i if len(stack)==0 else i-stack[-1]-1
                ans = max(ans, height*width)
            stack.append(i)

        return ans