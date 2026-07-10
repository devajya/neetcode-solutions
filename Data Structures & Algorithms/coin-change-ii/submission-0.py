class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {} # (index, amount_so_far)
        def dfs(i, accum):
            if accum == amount:
                return 1
            
            if accum > amount or i >= len(coins):
                return 0

            if (i, accum) in dp:
                return dp[(i, accum)]

            
            takes = dfs(i, accum+coins[i])
            leaves = dfs(i+1, accum)

            dp[(i, accum)] = takes+leaves

            return dp[(i, accum)]

        return dfs(0, 0)

            