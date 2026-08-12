class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        has_seen_obstacle = False
        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                has_seen_obstacle = True
            dp[i][0] = 0 if has_seen_obstacle else 1

        has_seen_obstacle = False
        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                has_seen_obstacle = True
            dp[0][j] = 0 if has_seen_obstacle else 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        for i in range(rows):
            for j in range(cols):
                print(dp[i][j])
        return dp[rows-1][cols-1]


        1, 1, 1
        1, 2, 3
        1, 0, 6
