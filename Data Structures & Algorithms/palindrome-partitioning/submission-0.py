class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(c):
            return c==c[::-1]

        def backtrack(start_idx, curr_arr):
            if start_idx == len(s): 
                ans.append(list(curr_arr))
                return True
            if start_idx >= len(s): 
                return False

            for i in range(start_idx, len(s)):
                substr = s[start_idx:i+1]
                if isPalindrome(substr):
                    curr_arr.append(substr)
                    backtrack(i+1, curr_arr)
                    curr_arr.pop() 

        backtrack(0, [])
        return ans