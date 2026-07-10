class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(index, buying_state):
            if index >= len(prices):
                return 0
            
            if (index, buying_state) in dp:
                return dp[(index, buying_state)]
            
            if buying_state:
                profit_buying = dfs(index+1, False) - prices[index] 
                profit_cooldown = dfs(index+1, buying_state)
                dp[(index, buying_state)] = max(profit_buying, profit_cooldown)
            else:
                profit_selling = dfs(index+2, True) + prices[index] 
                profit_cooldown = dfs(index+1, buying_state)
                dp[(index, buying_state)] = max(profit_selling, profit_cooldown)

            return dp[(index, buying_state)]


        return dfs(0, True)
        
                


