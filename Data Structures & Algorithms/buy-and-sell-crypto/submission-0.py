class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cp = 1000
        for p in prices:
            if p < cp:
                cp = p
            ans = max(ans, p - cp)
        return ans