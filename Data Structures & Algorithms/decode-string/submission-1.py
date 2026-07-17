class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                so_far = ""
                while stack and stack[-1] != "[":
                    so_far = stack.pop() + so_far
                stack.pop()

                k = self.pop_num(stack)
                fin = so_far * k
                while stack and stack[-1].isalpha():
                    sc = stack.pop()
                    fin = sc+fin
                stack.append(fin)
            else:
                stack.append(c)
        
        ans = ""
        while stack:
            ans = stack.pop() + ans
        return ans
        
    def pop_num(self, stack):
        mult = 1
        num = 0

        while stack and stack[-1].isdigit():
            n = int(stack.pop())
            num += mult*n
            mult *= 10

        return num if num != 0 else 1