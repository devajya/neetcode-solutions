class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def build(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            build(i+1)
            subset.pop()
            build(i+1)
        
        build(0)
        return res
        