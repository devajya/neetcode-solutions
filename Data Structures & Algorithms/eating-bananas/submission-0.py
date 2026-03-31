class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans = r

        while l<=r:
            m = (l+r)//2
            temp = 0

            for pile in piles:
                temp += math.ceil(float(pile)/m)

            if temp <= h:
                ans = m
                r = m-1
            else:
                l = m+1

        return ans