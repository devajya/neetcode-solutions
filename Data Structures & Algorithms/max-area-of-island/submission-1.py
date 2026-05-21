class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        areas = [0]*(n*m//2+1)
        ptr=0

        def dfs(grid, r, c, visited, areas, ptr):
            if r<0 or c<0 or r>=n or c>=m or grid[r][c] == 0 or visited[r][c]:
                return
        
            visited[r][c] = True
            areas[ptr] += 1

            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(grid, r+dr, c+dc, visited, areas, ptr)

        for r in range(0, n):
            for c in range(0, len(grid[r])):
                if grid[r][c] == 1 and not visited[r][c]:
                    dfs(grid, r, c, visited, areas, ptr)
                    ptr+=1
        
        return max(areas)
        