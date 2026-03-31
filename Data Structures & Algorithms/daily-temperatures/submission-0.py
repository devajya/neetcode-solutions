class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack= []
        ans=[0]*len(temps)
        for idx,temp in enumerate(temps):
            while len(stack) > 0 and temp > stack[-1][0]:
                st, si = stack.pop()
                ans[si] = idx - si
            stack.append((temp, idx))
        return ans