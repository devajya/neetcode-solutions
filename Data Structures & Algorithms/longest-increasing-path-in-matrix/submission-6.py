class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])        

        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            
            max_len = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i+dx
                nj = j+dy


                if (ni<0 or nj<0 or ni>=m or nj>=n or matrix[ni][nj] <= matrix[i][j]):
                    continue

                max_len = max(max_len, 1+dfs(ni, nj))
            
            dp[(i, j)] = max_len
            return max_len

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return max(dp.values())