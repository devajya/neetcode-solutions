class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            memo[i][0] = 1
        
        for j in range(0, n):
            memo[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                for p,q in [(i-1,j), (i,j-1)]:
                    if p<0 or q<0 or p>m or q>n:
                        continue
                    memo[i][j] += memo[p][q]  

        return memo[m-1][n-1]

        