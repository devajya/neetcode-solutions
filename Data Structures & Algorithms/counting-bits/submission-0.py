class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            ans = 0
            for j in range(10):
                ans += 1 if i & 1<<j else 0
            arr.append(ans)
        
        return arr
