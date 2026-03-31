class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lazy way is to reverse and compare still O(n)
        i=0
        j=len(s)-1

        while i<=j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                print(s[i], s[j])
                print("reached")
                return False
            i+=1
            j-=1
        return True
    