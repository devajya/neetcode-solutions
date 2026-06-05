class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n
        arr = [1, 2]
        
        for i in range(2, n):
            arr.append(arr[i-2] + arr[i-1])

        return arr[-1]

