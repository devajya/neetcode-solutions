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

        if nums[-1] < target :
            l = 0
            r = minIdx
        else:
            l = minIdx
            r = len(nums)-1

        while l<=r : 
            m = (l+r) // 2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
            
        return -1
