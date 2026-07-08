class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        ans = 1
        for i in range(abs(n)):
            ans *= x
        
        return ans if n > 0 else 1/ans