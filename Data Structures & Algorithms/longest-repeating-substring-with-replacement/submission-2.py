class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxf = 0
        l=0
        ans = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])

            while (r-l+1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)

        return ans

        