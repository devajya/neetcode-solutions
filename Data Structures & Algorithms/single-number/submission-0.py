class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitmask = 0
        for n in nums:
            bitmask ^= n
        return bitmask

         