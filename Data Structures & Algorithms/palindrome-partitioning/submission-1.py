class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(startIndex, currentPath):
            if startIndex == len(s):
                ans.append(list(currentPath))
                return
            if startIndex > len(s):
                return
            
            for i in range(startIndex, len(s)):
                sub = s[startIndex:i+1]
                if sub == sub[::-1]:
                    currentPath.append(sub)
                    backtrack(i+1, currentPath)
                    currentPath.pop()
                

        backtrack(0, [])
        return ans