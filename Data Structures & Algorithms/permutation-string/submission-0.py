class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = Counter(s1)
        window = len(s1)
        l=0

        for r in range(len(s2)):
            c = s2[r]
            if counts[c] > 0:
                window-=1
            counts[c] -=1

            if r-l+1 > len(s1):
                lc = s2[l]
                if counts[lc] >=0:
                    window+=1
                counts[lc] +=1
                l+=1
            if window == 0:
                return True

        return False

    