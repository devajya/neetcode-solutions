class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        q = deque([])
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        step = 0
        while q and fresh > 0:
            step += 1
            q_len = len(q)
            for _ in range(q_len):
                i, j = q.popleft()

                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx, ny = i+dx, j+dy
                    if not (0<=nx<m and 0<=ny<n):
                        continue

                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return step