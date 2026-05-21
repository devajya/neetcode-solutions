class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(grid, r, c, visited):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[r]) or grid[r][c] == "0" or visited[r][c]:
                return 
            
            visited[r][c] = True

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(grid, r+dr, c+dc, visited)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(grid, r, c, visited)
                    ans+=1
        return ans