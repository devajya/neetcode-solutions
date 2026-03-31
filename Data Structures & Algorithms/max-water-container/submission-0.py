class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        ans = -1
        while i<j:
            width = j-i
            height = min(heights[i], heights[j])
            ans = max(ans, width*height)

            if height == heights[i]:
                i+=1
            else:
                j-=1
        return ans