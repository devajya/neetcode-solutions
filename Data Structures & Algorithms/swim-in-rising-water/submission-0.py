class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))

        def dfs(node, t):
            row, col = node
            if (row < 0 or col < 0 or row >= n or col >=n or
                visit[row][col] or grid[row][col] > t):
                return False
            if row == (n - 1) and col == (n - 1):
                return True
            visit[row][col] = True
            return (dfs((row + 1, col), t) or
                    dfs((row - 1, col), t) or
                    dfs((row, col + 1), t) or
                    dfs((row, col - 1), t))

        for t in range(minH, maxH):
            if dfs((0, 0), t):
                return t
            for row in range(n):
                for col in range(n):
                    visit[row][col] = False

        return maxH