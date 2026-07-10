class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = {} # (indices i first two string to track if it can be made interleavig s1[i:], s2[j:])
        def dfs(i, j, k):
            if k == len(s3):
                return i == (len(s1)) and (j == len(s2))

            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = False
            if i < len(s1) and s3[k] == s1[i]:
                ans = dfs(i+1, j, k+1)
            if not ans and j<len(s2) and s2[j] == s3[k]:
                ans = dfs(i, j+1, k+1)
            
            dp[(i, j)] = ans
            return ans

        return dfs(0, 0, 0)

            