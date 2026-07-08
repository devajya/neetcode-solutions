class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = int(n*(n+1)/2)
        for j in nums:
            tot-=j
        
        return tot