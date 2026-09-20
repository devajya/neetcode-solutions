class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i>=m or j>=n or grid[i][j] == 1:
                return 0
            if i==m-1 and j == n-1:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]
            
            num_paths = 0
            num_paths += dfs(i, j+1)
            num_paths += dfs(i+1, j)

            dp[(i, j)] = num_paths
            return num_paths
        
        return dfs(0, 0)
