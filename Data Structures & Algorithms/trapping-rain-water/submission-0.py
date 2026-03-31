class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        l_max = height[i]
        r_max = height[j]
        ans=0
        while i<j:
            if l_max < r_max:
                i+=1
                l_max = max(l_max, height[i])
                ans+=l_max-height[i]

            else:
                j-=1
                r_max = max(r_max, height[j])
                ans+=r_max-height[j]
        return ans