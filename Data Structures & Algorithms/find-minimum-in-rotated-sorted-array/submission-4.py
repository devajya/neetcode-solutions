class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            leftVal = nums[l]
            rightVal = nums[r]
            midIdx= (l+r) // 2

            if nums[midIdx] < rightVal:
                r = midIdx
            else:
                l = midIdx + 1
            
        return nums[l-1]
