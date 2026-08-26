class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        m, n = len(s), len(t)
        while i<m and j<n:
            if t[j] == s[i]:
                j+=1
            i+=1
        
        return n-j