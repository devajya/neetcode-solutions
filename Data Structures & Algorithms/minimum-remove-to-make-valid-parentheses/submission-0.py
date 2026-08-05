class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid_s = ""
        for i, c in enumerate(s):
            if c not in ["(", ")"]:
                continue

            if c == "(":
                stack.append((i, c))    
                continue

            # else, i.e. c == ")"
            if not stack or stack[-1][1] != "(":
                stack.append((i, c))
            else:
                stack.pop()


        while stack:
            i, c = stack.pop()
            s = s[:i] + s[i+1:]
        
        return s

