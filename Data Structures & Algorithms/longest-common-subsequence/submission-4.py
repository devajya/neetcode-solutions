class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = {}
        def dfs(i, j):
            if i>=m or j>=n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            l_lcs = 0
            if s1[i] == s2[j]:
                l_lcs = 1+dfs(i+1, j+1)
            else:
                l_lcs = max(dfs(i, j+1), dfs(i+1, j))
            
            dp[(i, j)] = l_lcs
            return l_lcs
        
        return dfs(0, 0)