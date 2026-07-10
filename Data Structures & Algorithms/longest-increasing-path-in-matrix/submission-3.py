import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(10000 + 100)  # or some safe margin above rows*cols
        # track the lonegest inc path from each index
        dp = defaultdict(int) # (i, j), row/col in matrix

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            max_len = 1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i+dx, j+dy
                
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                    if matrix[i][j] < matrix[ni][nj]:
                        max_len = max(max_len, 1 + dfs(ni, nj))

            dp[(i, j)] = max_len  
            return max_len
        
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)

        return max(dp.values())
