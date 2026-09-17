class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def explore(i, j):
            if (not (0<=i<m and 0<=j<n)) or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = i+dx, j+dy
                explore(nx, ny)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    explore(i, j)
                    ans += 1

        return ans        