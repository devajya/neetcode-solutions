class Solution:
    def climbStairs(self, n: int) -> int:
        prev = [1, 2]
        for i in range(2, n):
            prev.append(prev[i-2] + prev[i-1])

        return prev[n-1]