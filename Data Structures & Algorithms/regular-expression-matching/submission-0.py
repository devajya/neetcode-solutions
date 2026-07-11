class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {} # (i, j) to bool
        # s[i:] and p[j:] can b matched

        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in dp:
                return dp[(i, j)]

            res = False

            match = True if i < len(s) and (s[i] == p[j] or p[j] == '.') else False

            if j < len(p) - 1 and p[j+1] == '*':
                # stay s, skip(+2) p or [matching so -> take s(+1) and stay p]
                res = dfs(i, j+2) or (match and dfs(i+1, j))
            
            elif match:
                res = dfs(i+1, j+1)
            else: 
                res = False

            dp[(i, j)] = res
            return res 
         
        return dfs(0,0)