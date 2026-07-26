class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {} # ((i, j), length of lcs)
        m = len(text1)
        n = len(text2)

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            lcs = 0
            if text1[i] == text2[j]:
                lcs += 1 + dfs(i+1, j+1)
            else:
                lcs = max(dfs(i+1, j), dfs(i, j+1))
            
            dp[(i, j)] = lcs
            return lcs

        
        return dfs(0, 0)