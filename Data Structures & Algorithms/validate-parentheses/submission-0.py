from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        m = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                p = stack.pop()
                if p != m.get(c):
                    return False
            print(stack)
            
        return len(stack)==0