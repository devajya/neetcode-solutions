class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i>=m or j>=n:
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            min_sum = grid[i][j] + min(dfs(i, j+1), dfs(i+1, j))
            dp[(i, j)] = min_sum

            return min_sum
        
        return dfs(0, 0)