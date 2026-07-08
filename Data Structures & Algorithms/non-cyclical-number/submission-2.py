class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        
        while n != 1:
            if n in hashset:
                return False
            
            hashset.add(n)

            n = sum(int(i) ** 2 for i in str(n))
        
        return True
        