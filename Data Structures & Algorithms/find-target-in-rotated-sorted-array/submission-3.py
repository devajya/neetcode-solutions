class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
                
        minIdx = l-1

        a = self.helper(0, minIdx, nums, target)
        b = self.helper(minIdx, len(nums)-1, nums, target)

        print(a, b)

        if a >= 0:
            return a

        if b >= 0:
            return b
        
        return -1

    def helper(self, l, r, nums, target):
        while l<=r : 
            m = (l+r) // 2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
            
        return -1
