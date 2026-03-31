class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}
        for i,n in enumerate(nums):
            if target-n in smap:
                return [smap[target-n], i]
            smap[n] = i