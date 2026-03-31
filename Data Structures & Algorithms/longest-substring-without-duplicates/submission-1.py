class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        i=0
        ans=0
        for j in range(0, len(s)):
            while s[j] in store:
                ans = max(ans, j-i)
                store.remove(s[i])
                i+=1
            store.add(s[j])
    
        return max(ans, len(store))

        