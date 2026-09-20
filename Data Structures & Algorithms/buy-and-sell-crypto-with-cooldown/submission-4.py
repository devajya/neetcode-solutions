class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, has_coin):
            if i >= len(prices):
                return 0
            if (i, has_coin) in dp:
                return dp[(i, has_coin)]

            value = 0
            do_nothing = dfs(i+1, has_coin)
            if has_coin:
                sell = prices[i] + dfs(i+2, not has_coin)
                value = max(sell, do_nothing)
            else:
                buy = dfs(i+1, not has_coin) - prices[i]
                value = max(buy, do_nothing)

            dp[(i, has_coin)] = value
            return value

        return dfs(0, False)
