class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]

        while l<=r:
            lhi = height[l]
            rhi = height[r]

            if lhi < rhi:
                lmax = max(lmax, lhi)
                ans += lmax-lhi
                l+=1
                
            else:
                rmax = max(rmax, rhi)
                ans += rmax-rhi
                r-=1

        return ans

