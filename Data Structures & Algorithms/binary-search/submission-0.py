class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            p = (l+r)//2
            if target > nums[p]:
                l = p+1
            elif target < nums[p]:
                r=p-1
            else:
                return p
        return -1