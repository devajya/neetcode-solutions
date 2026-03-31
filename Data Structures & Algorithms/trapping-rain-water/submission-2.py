class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        l,r =0,len(height)-1
        lmax,rmax = height[l], height[r]

        while l<r:
            vl = height[l]
            vr = height[r]

            if vl < vr:
                lmax = max(lmax, vl)
                ans+= abs(lmax-vl)
                l+=1
                continue

            rmax = max(rmax, vr)
            ans += abs(rmax-vr)
            r-=1
            
        return ans



        


