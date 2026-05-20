class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def isValid(parens):
            stack = []
            for c in parens:
                if c == "(":
                    stack.append(c)
                else:
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        def backtrack(curr_str, count_open, count_closed):
            if len(curr_str) == 2*n and count_open==count_closed and isValid(curr_str):
                ans.append(curr_str)
                return
            if len(curr_str) > 2*n:
                return

            backtrack(curr_str+"(", count_open+1, count_closed)
            backtrack(curr_str+")", count_open, count_closed+1)
        
        backtrack("", 0, 0)
        return ans
