class Solution:
    sys.setrecursionlimit(3000)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = {}


        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == n:
                dp[(i, j)] = m-j
                return m-j
            if j == m:
                dp[(i, j)] = n-i
                return n-i
            if str1[i] == str2[j]:
                dp[(i, j)] = 1+dfs(i+1, j+1)
            else:
                dp[(i, j)] = 1+min(dfs(i, j+1), dfs(i+1, j))
            
            return dp.get((i, j), -1)

        dfs(0, 0)

        def builder(i, j):
            ans = []
            while i < n or j < m:
                if i == n:
                    ans.extend(str2[j:])
                    break
                if j == m:
                    ans.extend(str1[i:])
                    break
                if str1[i] == str2[j]:
                    ans.append(str1[i])
                    i+=1
                    j+=1
                elif dp.get((i+1, j), -1) < dp.get((i, j+1), -1):
                    ans.append(str1[i])
                    i+=1
                else:
                    ans.append(str2[j])
                    j+=1
            return ans
        
        return ''.join(builder(0, 0))