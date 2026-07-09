class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums) 

    def merge(self, num1, num2) -> List[int]:
        arr = []

        i=0
        j=0

        while i < len(num1) and j < len(num2):
            if num1[i] <= num2[j]:
                arr.append(num1[i])
                i+=1
            else:
                arr.append(num2[j])
                j+=1

        while i < len(num1):
            arr.append(num1[i])
            i+=1

        while j < len(num2):
            arr.append(num2[j])
            j+=1
        
        return arr


    def mergesort(self, nums) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums) // 2

        num1 = nums[0:m]
        num2 = nums[m:]

        left = self.mergesort(num1)
        right = self.mergesort(num2)

        return self.merge(left, right)

        