class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {} # (i, j) -> num unique paths
        def dfs(i, j):
            if i>=m or j >=n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if (i, j) in dp:
                return dp[(i, j)]

            num_paths = 0
            for dx, dy in [[0, 1], [1, 0]]:
                num_paths += dfs(i+dx, j+dy)
            
            dp[(i, j)] = num_paths
            return num_paths
        
        return dfs(0, 0)