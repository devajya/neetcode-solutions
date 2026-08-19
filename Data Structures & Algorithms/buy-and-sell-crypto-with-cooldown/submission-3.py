class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i, state):
            if i >= len(prices):
                return 0

            if (i, state) in dp:
                return dp[(i, state)]
            
            if state == "buy":
                
                buy_now = dfs(i+1, "sell") - prices[i]
                wait = dfs(i+1, "buy")
                dp[(i, state)] = max(buy_now, wait)
            
            # state == "sell"
            else:
                dp[(i, state)] = max(dfs(i+2, "buy")+prices[i], dfs(i+1, "sell"))
            
            return dp[(i, state)]
            
        return dfs(0, "buy")