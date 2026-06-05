class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength = 0
        maxL = 0
        maxR = 0
        for i in range(n):
            #even
            l, r = i, i
            while l>=0 and r<n and s[l] == s[r]:
                length = (r-l+1)
                if length > maxLength :
                    maxLength = length
                    maxL = l
                    maxR = r
                l-=1
                r+=1
            
            # odd
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                length = (r-l+1)
                if length > maxLength :
                    maxLength = length
                    maxL = l
                    maxR = r
                l-=1
                r+=1
        return s[maxL:maxR+1]
            