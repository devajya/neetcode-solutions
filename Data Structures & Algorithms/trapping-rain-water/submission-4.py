class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        i=0
        j=n-1

        l_max, r_max = height[i], height[j]

        water = 0

        while i<=j:
            l_cur = height[i]
            r_cur = height[j]

            if l_cur <= r_cur:
                i+=1 
                l_max = max(l_max, l_cur)
                water += l_max - l_cur
            else:
                j-=1
                r_max = max(r_max, r_cur)
                water += r_max - r_cur
                  

        return water