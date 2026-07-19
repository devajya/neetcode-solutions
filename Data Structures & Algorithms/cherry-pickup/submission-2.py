class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = {}
        # (k, r1, r2) - steps, row of 1, row of 2
        # We'll model the problem like two peopel going from 0,0 to n-1, n-1 simul

        def dfs(k, r1, r2):
            c1 = k-r1
            c2 = k-r2
            if not (0<=r1<n and 0<=c1<n and 0<=r2<n and 0<=c2<n):
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            if (k, r1, r2) in dp:
                return dp[(k, r1, r2)]
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            ans = max(
                dfs(k+1, r1+1, r2+1), 
                dfs(k+1, r1, r2+1), 
                dfs(k+1, r1+1, r2), 
                dfs(k+1, r1, r2)
            )

            ans += grid[r1][c1]
            if r1!=r2:
                ans += grid[r2][c2]
            
            dp[(k, r1, r2)] = ans
            return ans
        
        return max(0, dfs(0,0,0))
