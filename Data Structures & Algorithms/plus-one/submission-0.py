class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        mult = 10**(len(digits)-1)
        for c in digits:
            num += c*mult
            mult /= 10 
        
        num = int(num+1)

        arr = []
        for c in str(num):
            arr.append(int(c))
        
        return arr