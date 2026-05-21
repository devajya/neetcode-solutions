class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh_count = 0
        ticks = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count+=1

        while fresh_count>0 and q:
            level_count = len(q)
            for i in range(level_count):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = r+dr, c+dc

                    if row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh_count-=1
                        q.append((row, col))

            ticks+=1

        if fresh_count == 0:
            return ticks
        
        return -1
