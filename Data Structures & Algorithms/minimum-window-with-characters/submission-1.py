class Solution:
    def charIndex(self, c:str) -> int:
        if c.islower():
            return ord(c) - ord('a')
        return 26 + ord(c) - ord('A')
    def minWindow(self, s: str, t: str) -> str:
        minimumSubstringSize = float("+inf")
        start = -1
        end = -1
    
        targetCounts = [0]*52
        for c in t:
            targetCounts[self.charIndex(c)] += 1

        windowCounts = [0]*52

        characterTargets = sum(1 for cnt in targetCounts if cnt > 0)
        charactersFilled = 0

        i=0
        for j, c in enumerate(s):
            
            indexOfSubstrEnd = self.charIndex(c)
            windowCounts[indexOfSubstrEnd] += 1

            # if the letter is needed, and is now sufficient
            if targetCounts[indexOfSubstrEnd] > 0 and windowCounts[indexOfSubstrEnd] == targetCounts[indexOfSubstrEnd]:
                charactersFilled += 1

            while charactersFilled == characterTargets:
                indexOfSubstrStart = self.charIndex(s[i])
                if j-i+1 < minimumSubstringSize:
                    start = i
                    end = j
                    minimumSubstringSize = j-i+1
                windowCounts[indexOfSubstrStart] -= 1

                # if the letter was needed but is now deficient
                if targetCounts[indexOfSubstrEnd] > 0 and windowCounts[indexOfSubstrStart] < targetCounts[indexOfSubstrStart]:
                    charactersFilled -= 1
                i+=1 
            
            
        
        return s[start:end+1] if start != -1 else ""

