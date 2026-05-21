class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def dfs(grird, r, c, dist):
            if (r<0 or c<0 or 
            r>=len(grid) or c>=len(grid[0]) or 
            grid[r][c] == -1 or 
            grid[r][c] < dist):
                return

            grid[r][c] = min(grid[r][c], dist)

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(grid, r+dr, c+dc, dist+1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(grid, r, c, 0)
        return