class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, ocean_set, prev_height):
            if (r < 0 or c < 0 or r >= n or c >= m or 
                (r, c) in ocean_set or heights[r][c] < prev_height):
                return
            
            ocean_set.add((r, c))
            
            dfs(r + 1, c, ocean_set, heights[r][c])
            dfs(r - 1, c, ocean_set, heights[r][c])
            dfs(r, c + 1, ocean_set, heights[r][c])
            dfs(r, c - 1, ocean_set, heights[r][c])

        for j in range(m):
            dfs(0, j, pacific, heights[0][j])       
            dfs(n - 1, j, atlantic, heights[n - 1][j]) 

        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])       
            dfs(i, m - 1, atlantic, heights[i][m - 1]) 
            
        return [list(cell) for cell in pacific.intersection(atlantic)]